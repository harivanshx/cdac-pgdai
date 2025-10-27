
# train.py
"""Train SVM on Pima Indians Diabetes dataset, tune hyperparameters, visualize results,
and save final pipeline and cv results."""

import os, json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = 'data/diabetes.csv'  # ensure downloaded from Kaggle and saved here
MODELS_DIR = 'models'
os.makedirs(MODELS_DIR, exist_ok=True)

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    # target column
    tgt_candidates = [c for c in df.columns if c.lower() in ('outcome','target','class')]
    if len(tgt_candidates)==0 and 'Outcome' in df.columns:
        tgt = 'Outcome'
    elif len(tgt_candidates)>0:
        tgt = tgt_candidates[0]
    elif 'Outcome' in df.columns:
        tgt = 'Outcome'
    else:
        tgt = df.columns[-1]
    X = df.drop(columns=[tgt])
    y = df[tgt]

    zero_nan_cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for col in zero_nan_cols:
        if col in X.columns:
            X[col] = X[col].replace(0, np.nan)

    imputer = SimpleImputer(strategy='median')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    return X_imputed, y, imputer

def plot_c_vs_scores(results, C_list, out_dir):
    plt.figure(figsize=(8,6))
    plt.plot(C_list, results['train_scores'], marker='o', label='Train Accuracy')
    plt.plot(C_list, results['val_scores'], marker='s', label='Validation Accuracy')
    plt.xscale('log')
    plt.xlabel('C (log scale)')
    plt.ylabel('Accuracy')
    plt.title('Effect of C on under/overfitting (Train vs Val)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, 'c_vs_accuracy.png'))
    plt.close()

def main():
    print('Loading dataset from', DATA_PATH)
    X, y, imputer = load_and_preprocess(DATA_PATH)
    print('Data shape:', X.shape, 'Target distribution:\n', y.value_counts(normalize=True))

    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.25, stratify=y_train_full, random_state=42)
    print('Splits:', X_train.shape, X_val.shape, X_test.shape)

    scaler = StandardScaler()
    svc = SVC(kernel='rbf', probability=True)

    baseline_pipe = Pipeline([('scaler', scaler), ('svc', svc)])
    baseline_pipe.fit(X_train, y_train)
    y_pred = baseline_pipe.predict(X_val)
    print('Baseline val accuracy:', accuracy_score(y_val, y_pred))

    param_grid = {
        'svc__C': [0.01, 0.1, 1, 10, 100],
        'svc__gamma': ['scale', 'auto', 0.01, 0.1, 1]
    }
    pipe = Pipeline([('scaler', scaler), ('svc', svc)])
    grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy', n_jobs=-1, return_train_score=True)
    grid.fit(X_train, y_train)
    print('Best params:', grid.best_params_)
    print('Best CV score:', grid.best_score_)

    C_list = [0.01, 0.1, 1, 10, 100, 1000]
    train_scores = []
    val_scores = []
    for C in C_list:
        tmp_pipe = Pipeline([('scaler', scaler), ('svc', SVC(kernel='rbf', C=C, gamma='scale', probability=True))])
        tmp_pipe.fit(X_train, y_train)
        train_scores.append(tmp_pipe.score(X_train, y_train))
        val_scores.append(np.mean(cross_val_score(tmp_pipe, X_train, y_train, cv=5)))
    results = {'train_scores': train_scores, 'val_scores': val_scores}
    os.makedirs('outputs', exist_ok=True)
    plot_c_vs_scores(results, C_list, out_dir='outputs')

    cv_results = pd.DataFrame(grid.cv_results_)
    cv_results.to_csv(os.path.join(MODELS_DIR, 'cv_results.csv'), index=False)

    df_heat = cv_results.copy()
    df_heat['param_svc__C'] = df_heat['param_svc__C'].astype(str)
    df_heat['param_svc__gamma'] = df_heat['param_svc__gamma'].astype(str)
    pivot = df_heat.pivot_table(values='mean_test_score', index='param_svc__gamma', columns='param_svc__C')
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, annot=True, fmt='.3f', cmap='viridis')
    plt.title('GridSearchCV mean_test_score (gamma x C)')
    plt.tight_layout()
    plt.savefig('outputs/grid_heatmap.png')
    plt.close()

    best = grid.best_estimator_
    y_test_prob = best.predict_proba(X_test)[:,1]
    y_test_pred = (y_test_prob >= 0.5).astype(int)
    print('\nTest Set Classification Report:\n', classification_report(y_test, y_test_pred))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_test_pred))

    joblib.dump({'pipeline': best, 'imputer': imputer}, os.path.join(MODELS_DIR, 'svm_pima_pipeline.joblib'))
    with open(os.path.join(MODELS_DIR, 'best_params.json'), 'w') as fh:
        json.dump({'best_params': grid.best_params_, 'best_score': grid.best_score_}, fh)

    print('Saved pipeline and results to', MODELS_DIR)
    print('Outputs (plots) saved to outputs/')


if __name__ == '__main__':
    main()
