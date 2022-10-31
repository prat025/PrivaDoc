from django.test import TestCase
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle 
import os
import pickle

data=pd.read_csv("insurance.csv",sep=',')
data=data[["age","bmi","smoker","charges"]]
data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})

predict="charges"

X = np.array(data.drop([predict], 1)) # Features
y = np.array(data[predict]) # Labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test) # acc stands for accuracy 
print(acc)

with open("insurance.pickle", "wb") as f:
    pickle.dump(linear, f)


