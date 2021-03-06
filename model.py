# -*- coding: utf-8 -*-
"""Students_mark_predictor.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v9YzmpWaj6Q8Z3P0jcFVIViiWWvomx7m

## Business Problem
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Load dataset"""

path = "C:\\Users\\susha\Dropbox\\My PC (LAPTOP-HIGBGETI)\\Downloads\\student_info.csv"
df = pd.read_csv(path)

df.head()

df.tail()

df.shape

"""## Discover and visualize the data to gain insights"""

df.info()

df.describe()

plt.scatter(x=df.study_hours, y=df.student_marks)
plt.xlabel("Students study hours")
plt.ylabel("Students marks")
plt.title("Scatter plot of students study hours vs students marks")
plt.show()

"""## Prepare the data for Machine Learning algorithms"""

# Data Cleaning..

df.isnull()

df.isnull().sum()

df.mean()

df2 = df.fillna(df.mean())
df2.head()

# Split datasets..

X = df2.drop("student_marks", axis="columns")
y = df2.drop("study_hours", axis="columns")
print("shape of X = ", X.shape)
print("shape of y = " ,y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2, random_state = 51)
print("shape of X_train = ", X_train.shape)
print("shape of y_train = " ,y_train.shape)
print("shape of X_test = ", X_test.shape)
print("shape of y_test = " ,y_test.shape)

"""## Select a model and train it.."""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train,y_train)

lr.intercept_

lr.coef_

lr.predict([[6]])[0][0].round(2)

y_pred = lr.predict(X_test)
y_pred

pd.DataFrame(np.c_[X_test,y_test,y_pred],columns = ["study_hours","student_marks_original","students_marks_predictor"])

"""## Fine-tune your model"""

lr.score(X_test,y_test).round(2)

plt.scatter(X_train,y_train)

plt.scatter(X_test,y_test)
plt.plot(X_train,lr.predict(X_train),color="r")

"""## Present your Solution

## Save ML Model
"""

import joblib
joblib.dump(lr, "Students_marks_predictor_model.pkl")


# Saving model to disk
import pickle
pickle.dump(lr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2]]))






