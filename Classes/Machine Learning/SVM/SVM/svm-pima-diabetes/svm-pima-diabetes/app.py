
# app.py - Streamlit app for SVM Pima Diabetes demo
import streamlit as st
import pandas as pd, numpy as np, joblib, os, json
from sklearn.pipeline import Pipeline

st.set_page_config(page_title='SVM - Pima Diabetes Demo', layout='centered')

st.title('SVM on Pima Indians Diabetes Dataset - Demo')
st.markdown('Upload dataset (optional) or ensure data/diabetes.csv exists. Run train.py to create model before using app.')

MODEL_PATH = 'models/svm_pima_pipeline.joblib'
BEST_PARAMS_PATH = 'models/best_params.json'

def load_model():
    if os.path.exists(MODEL_PATH):
        data = joblib.load(MODEL_PATH)
        return data['pipeline'], data['imputer']
    return None, None

pipeline, imputer = load_model()

st.sidebar.header('Predict single sample')
cols = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
sample = {}
for c in cols:
    default = 0.0 if c in ['BMI','DiabetesPedigreeFunction'] else 0
    sample[c] = st.sidebar.number_input(c, value=float(default))

if st.sidebar.button('Predict sample'):
    if pipeline is None:
        st.error('No trained model found. Run train.py first.')
    else:
        df = pd.DataFrame([sample])
        df_imputed = pd.DataFrame(imputer.transform(df), columns=df.columns)
        prob = pipeline.predict_proba(df_imputed)[:,1][0]
        pred = int(prob>=0.5)
        st.write('Prediction:', '**Diabetes**' if pred==1 else '**No Diabetes**')
        st.write('Probability:', f'{prob:.3f}')

st.markdown('---')
st.header('Model & Grid Search Results')
if os.path.exists(BEST_PARAMS_PATH):
    with open(BEST_PARAMS_PATH,'r') as fh:
        info = json.load(fh)
    st.write('Best params found during training:')
    st.json(info)
else:
    st.info('No training results found. Run train.py to produce best_params.json')

st.markdown('## Visualizations produced by train.py (saved to outputs/)')
if os.path.exists('outputs/c_vs_accuracy.png'):
    st.image('outputs/c_vs_accuracy.png', caption='C vs Train/Val Accuracy (log scale)')
if os.path.exists('outputs/grid_heatmap.png'):
    st.image('outputs/grid_heatmap.png', caption='GridSearch heatmap (mean_test_score)')
