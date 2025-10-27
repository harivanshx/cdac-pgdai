
# predict.py
"""Load saved SVM pipeline and make predictions for single examples or batch CSV."""
import joblib, os, json
import pandas as pd

MODEL_PATH = 'models/svm_pima_pipeline.joblib'

def load_pipeline():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError('Model not found. Run train.py first.')
    data = joblib.load(MODEL_PATH)
    pipeline = data['pipeline']
    imputer = data['imputer']
    return pipeline, imputer

def predict_single(example: dict):
    pipeline, imputer = load_pipeline()
    df = pd.DataFrame([example])
    df_imputed = pd.DataFrame(imputer.transform(df), columns=df.columns)
    prob = pipeline.predict_proba(df_imputed)[:,1][0]
    pred = int(prob >= 0.5)
    return {'prediction': pred, 'probability': float(prob)}

if __name__ == '__main__':
    example = {
        'Pregnancies': 2,
        'Glucose': 120,
        'BloodPressure': 70,
        'SkinThickness': 20,
        'Insulin': 79,
        'BMI': 25.0,
        'DiabetesPedigreeFunction': 0.5,
        'Age': 33
    }
    out = predict_single(example)
    print('Prediction (1=diabetes):', out['prediction'], 'Prob:', out['probability'])
