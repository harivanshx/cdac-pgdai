
SVM - Pima Indians Diabetes (Teaching Project)
=============================================

Dataset (download from Kaggle):
- Pima Indians Diabetes Database (Kaggle): https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
Save the CSV file as: data/diabetes.csv

Files included:
- train.py        : training script (preprocessing, SVM, grid search, save model & results)
- predict.py      : load saved model & predict single example
- app.py          : Streamlit app for interactive predictions and visualizations
- notebooks/      : Jupyter notebook with full analysis (svm_pima_notebook.ipynb)
- requirements.txt: Python dependencies
- models/         : (empty) will contain saved model after running train.py
- data/           : place diabetes.csv here before running

How to run:
1) Create conda env and install deps:
   conda create -n svmpy python=3.10 -y
   conda activate svmpy
   pip install -r requirements.txt


2) Train model:
   python train.py

3) Run Streamlit app:
   streamlit run app.py

Notes:
- The project includes missing-value handling (zeros treated as missing for certain features),
  scaling, SVM with RBF kernel, hyperparameter tuning (C, gamma), and visualizations to show
  underfitting vs overfitting.
