# -*- coding: utf-8 -*-
"""NYC2017Training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VM1T3DzGJcQg7ueg6m2uDdYyxlN-Y32r
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

#!ls "/content/drive/My Drive"

#!cp "/content/drive/My Drive/segmentdata.csv" "segmentdata.csv"

import pandas as pd
data = pd.read_csv('segmentdata.csv', index_col=0)

data.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data[['Registration State','Plate Type','Issue Date','Violation Code','Vehicle Body Type','Vehicle Make', 'Issuing Agency','Street Code1','Street Code2','Street Code3','Issuer Precinct','Issuer Command','Violation In Front Of Or Opposite','Violation County']], data[['Violation Location']], test_size = 0.2)

from xgboost import XGBClassifier

xgboost_model = XGBClassifier(tree_method = 'gpu_hist' , max_depth=7, n_estimators=100, objective='multi:softprob')

xgboost_model.fit(X_train, y_train)

y_pred_train = xgboost_model.predict(X_train)

print("For train\nAccuracy score:{},Balanced accuracy score:{},f1 score:{}".format(accuracy_score(y_train,y_pred_train),balanced_accuracy_score(y_train,y_pred_train),f1_score(y_train,y_pred_train, average='weighted')))

pickle.dump(xgboost_model, open('model.bin', 'wb'))

import pickle

"""# New Section"""

from sklearn.metrics import accuracy_score, f1_score ,balanced_accuracy_score

print("For train\nAccuracy score:{},Balanced accuracy score:{},f1 score:{}".format(accuracy_score(y_train,y_pred_train),balanced_accuracy_score(y_train,y_pred_train),f1_score(y_train,y_pred_train, average='weighted')))