# src/app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt

from sklearn.metrics import (
    roc_curve, precision_recall_curve, auc,
    confusion_matrix, accuracy_score, recall_score,
    precision_score, f1_score
)

st.set_page_config(page_title="Titanic Logistic Regression", layout="centered")
st.title("🚢 Titanic Survival Prediction (Logistic Regression)")

# fixed threshold from your analysis
BEST_THRESHOLD = 0.36

# Try to load pipeline first (preferred). If not available, load preprocessor + raw model.
PIPE_PATH = "models/pipeline_logistic.pkl"
PRE_PATH = "models/preprocessor.pkl"
MODEL_RAW_PATH = "models/model_logistic_raw.pkl"

use_pipeline = False
pre = None
model_raw = None
pipeline = None

if os.path.exists(PIPE_PATH):
    pipeline = joblib.load(PIPE_PATH)
    use_pipeline = True
elif os.path.exists(PRE_PATH) and os.path.exists(MODEL_RAW_PATH):
    pre = joblib.load(PRE_PATH)
    model_raw = joblib.load(MODEL_RAW_PATH)
    use_pipeline = False
else:
    st.error("Model artifacts not found. Run src/train.py to create 'models/pipeline_logistic.pkl' or both preprocessor/model files.")
    st.stop()

# helper to predict from dataframe (multiple rows)
def predict_from_df(df_in):
    if use_pipeline:
        probs = pipeline.predict_proba(df_in)[:, 1]
    else:
        X_trans = pre.transform(df_in)
        probs = model_raw.predict_proba(X_trans)[:, 1]
    return probs

# UI mode: single input or CSV
mode = st.radio("Mode", ["Single passenger (manual input)", "Batch (upload CSV)"])

needed = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

if mode == "Single passenger (manual input)":
    st.subheader("Enter passenger details")
    with st.form("single_form"):
        pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], index=2)
        sex = st.selectbox("Sex", ["male", "female"])
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        sibsp = st.number_input("SibSp", min_value=0, max_value=10, value=0)
        parch = st.number_input("Parch", min_value=0, max_value=10, value=0)
        fare = st.number_input("Fare", min_value=0.0, max_value=1000.0, value=32.2)
        embarked = st.selectbox("Embarked", ["C", "Q", "S"], index=2)
        submitted = st.form_submit_button("Predict")

    if submitted:
        row = pd.DataFrame([{
            "Pclass": pclass,
            "Sex": sex,
            "Age": age,
            "SibSp": sibsp,
            "Parch": parch,
            "Fare": fare,
            "Embarked": embarked
        }])
        # ensure column order
        row = row[needed]

        prob = predict_from_df(row)[0]
        pred = int(prob >= BEST_THRESHOLD)

        st.write("**Probability of survival:**", f"{prob:.3f}")
        if pred == 1:
            st.success(f"✅ Predicted: Survived (threshold = {BEST_THRESHOLD})")
        else:
            st.error(f"❌ Predicted: Died (threshold = {BEST_THRESHOLD})")

        # small gauge: progress bar
        st.progress(min(max(prob, 0.0), 1.0))

else:
    st.subheader("Upload CSV (must contain columns: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)")
    uploaded = st.file_uploader("Upload CSV", type=['csv'])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        missing = [c for c in needed if c not in df.columns]
        if missing:
            st.error(f"Missing columns in CSV: {missing}")
        else:
            # Preprocess missingness same as training
            df = df.copy()
            if 'Age' in df.columns:
                df['Age'] = df['Age'].fillna(df['Age'].median())
            if 'Fare' in df.columns:
                df['Fare'] = df['Fare'].fillna(df['Fare'].median())
            if 'Embarked' in df.columns:
                df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

            df_input = df[needed]
            probs = predict_from_df(df_input)
            preds = (probs >= BEST_THRESHOLD).astype(int)

            out = df_input.copy()
            out['prob_survived'] = probs
            out['pred_survived'] = preds
            st.write(out.head(20))

            # If the upload includes ground truth Survived, show aggregate metrics and curves
            if 'Survived' in df.columns:
                y = df['Survived']
                try:
                    st.write("ROC AUC:", round(auc(*roc_curve(y, probs)[:2]), 3))
                except Exception:
                    pass

                # Show counts
                st.write("Prediction counts:", out['pred_survived'].value_counts().to_dict())

                # If there are enough samples, show metrics-vs-threshold plot
                if len(df) >= 30:
                    thresholds = np.linspace(0.01, 0.99, 99)
                    accs = []; sens = []; specs = []; f1s = []
                    for t in thresholds:
                        p = (probs >= t).astype(int)
                        tn, fp, fn, tp = confusion_matrix(y, p).ravel()
                        accs.append((tp + tn) / (tp + tn + fp + fn))
                        sens.append(tp / (tp + fn) if (tp + fn) else 0)
                        specs.append(tn / (tn + fp) if (tn + fp) else 0)
                        f1s.append(f1_score(y, p))
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.plot(thresholds, accs, label='Accuracy')
                    ax.plot(thresholds, sens, label='Sensitivity')
                    ax.plot(thresholds, specs, label='Specificity')
                    ax.plot(thresholds, f1s, label='F1')
                    ax.axvline(BEST_THRESHOLD, color='k', linestyle='--', label=f'Fixed threshold {BEST_THRESHOLD}')
                    ax.legend()
                    ax.set_xlabel('Threshold')
                    ax.set_ylabel('Metric')
                    st.pyplot(fig)

st.caption("Model uses saved encoder & scaler (preprocessor) so input is transformed exactly as during training.")
