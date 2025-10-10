# src/train.py
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

NUMERIC_FEATURES = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
CATEGORICAL_FEATURES = ['Sex', 'Embarked']

def load_data(path='data/train.csv'):
    df = pd.read_csv(path)
    df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']].copy()
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    X = df.drop(columns=['Survived'])
    y = df['Survived']
    return X, y

def build_preprocessor():
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, NUMERIC_FEATURES),
        ('cat', categorical_transformer, CATEGORICAL_FEATURES)
    ])
    return preprocessor

def train_and_save(outdir='models'):
    os.makedirs(outdir, exist_ok=True)

    # Load and split
    X, y = load_data()
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)

    # Build preprocessor and fit on training data
    pre = build_preprocessor()
    X_train_trans = pre.fit_transform(X_train)

    # Train logistic regression on transformed data
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_trans, y_train)

    # Save preprocessor and model separately
    joblib.dump(pre, os.path.join(outdir, 'preprocessor.pkl'))
    joblib.dump(model, os.path.join(outdir, 'model_logistic_raw.pkl'))

    # Also save a convenience pipeline (pre + model) for easy inference
    pipeline = Pipeline([('pre', pre), ('model', model)])
    joblib.dump(pipeline, os.path.join(outdir, 'pipeline_logistic.pkl'))

    # Save feature names (best-effort)
    try:
        # sklearn >= 1.0: ColumnTransformer has get_feature_names_out
        feat_names = pre.get_feature_names_out()
        feat_list = feat_names.tolist()
    except Exception:
        # fallback: attempt to combine numeric + ohe categories
        try:
            ohe = pre.named_transformers_['cat']
            ohe_names = ohe.get_feature_names_out(CATEGORICAL_FEATURES).tolist()
            feat_list = NUMERIC_FEATURES + ohe_names
        except Exception:
            # last resort: store the raw names (not expanded)
            feat_list = NUMERIC_FEATURES + CATEGORICAL_FEATURES

    joblib.dump(feat_list, os.path.join(outdir, 'feature_names.pkl'))

    print(f"Saved: {outdir}/preprocessor.pkl")
    print(f"Saved: {outdir}/model_logistic_raw.pkl")
    print(f"Saved: {outdir}/pipeline_logistic.pkl")
    print(f"Saved: {outdir}/feature_names.pkl")

if __name__ == '__main__':
    train_and_save()
