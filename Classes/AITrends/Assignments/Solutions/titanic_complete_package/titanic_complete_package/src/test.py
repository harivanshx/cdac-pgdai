import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, precision_recall_curve, auc, confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
import joblib
import os

def load_and_split(path='data/train.csv'):
    df = pd.read_csv(path)
    df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, stratify=y, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)
    return X_val, X_test, y_val, y_test

def evaluate(model_path='models/model_logistic.pkl', plot_dir='plots'):
    os.makedirs(plot_dir, exist_ok=True)
    pipe = joblib.load(model_path)
    X_val, X_test, y_val, y_test = load_and_split()
    probs = pipe.predict_proba(X_val)[:,1]

    fpr, tpr, _ = roc_curve(y_val, probs)
    pr_prec, pr_rec, _ = precision_recall_curve(y_val, probs)
    roc_auc, pr_auc = auc(fpr,tpr), auc(pr_rec,pr_prec)

    print(f"ROC AUC: {roc_auc:.3f}")
    print(f"PR AUC: {pr_auc:.3f}")

    thresholds = np.linspace(0.01, 0.99, 99)
    accs, sens, specs, f1s = [], [], [], []
    for t in thresholds:
        preds = (probs >= t).astype(int)
        tn, fp, fn, tp = confusion_matrix(y_val, preds).ravel()
        accs.append((tp+tn)/(tp+tn+fp+fn))
        sens.append(tp/(tp+fn))
        specs.append(tn/(tn+fp))
        f1s.append(f1_score(y_val, preds))
    best_t = thresholds[np.argmax(f1s)]
    print(f"Best threshold by F1: {best_t:.2f}")

    plt.figure(figsize=(8,5))
    plt.plot(thresholds, accs, label='Accuracy')
    plt.plot(thresholds, sens, label='Sensitivity')
    plt.plot(thresholds, specs, label='Specificity')
    plt.plot(thresholds, f1s, label='F1')
    plt.legend(); plt.xlabel('Threshold'); plt.ylabel('Metric'); plt.title('Metrics vs Threshold')
    plt.savefig(f'{plot_dir}/metrics.png')

    probs_test = pipe.predict_proba(X_test)[:,1]
    preds = (probs_test >= best_t).astype(int)
    print("\\nTest set performance:")
    print('Accuracy:', accuracy_score(y_test, preds))
    print('Precision:', precision_score(y_test, preds))
    print('Recall:', recall_score(y_test, preds))
    print('F1:', f1_score(y_test, preds))
    print('Confusion matrix:\\n', confusion_matrix(y_test, preds))

if __name__ == '__main__':
    evaluate()
