# problem preperation
#Load Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.preprocessing import Normalizer
from pandas.plotting import scatter_matrix

# load dataset
df = pd.read_csv("Emotions.csv")

#Data Summarization

#shape
print(df.shape)
print(df.columns)
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

#types
print(df.dtypes)

#head
df.head()

#Descriptive statistics
print(df.describe())
df.info()

#histogram
df.hist()
plt.show()

#how many categories we have?
df['EMOTIONAL AFFIRM'].unique()
plt.figure(figsize = (6,3))
sns.countplot(df['EMOTIONAL AFFIRM'])
plt.show()
df['EMOTIONAL AFFIRM'].value_counts()
df.isnull().sum() #no missing values

#split into features and labels sets
X = df.drop(['Computer Time','EMOTIONAL AFFIRM'],axis = 1) #features
y = df['EMOTIONAL AFFIRM'] #labels
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 1)

#LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression
m1 = LogisticRegression()
m1.fit(X_train, y_train)
pred1=m1.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, pred1))
labels = ['Relaxed','Happy','Sad','Angry']
cm1 = pd.DataFrame(confusion_matrix(y_test, pred1), index = labels, columns = labels)
plt.figure(figsize = (10, 8))
sns.heatmap(cm1, annot = True, cbar = False, fmt = 'g')
plt.ylabel('Actual values')
plt.xlabel('Predicted values')
plt.show()

#SUPPORT VECTOR MACHINE

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
grid = {
    'C': [1, 5, 50],
    'gamma': [0.05, 0.1, 0.5, 1, 5]
}

m5 = GridSearchCV(SVC(), grid)
m5.fit(X_train, y_train)

m5.best_params_ 
pred5 = m5.predict(X_test)
print(classification_report(y_test, pred5))
cm5 = pd.DataFrame(confusion_matrix(y_test, pred5), index = labels, columns = labels)

plt.figure(figsize = (10, 8))
sns.heatmap(cm5, annot = True, cbar = False, fmt = 'g')
plt.ylabel('Actual values')
plt.xlabel('Predicted values')
plt.show()

#Naive Bayes Algorithm

from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.calibration import CalibratedClassifierCV
m4=GaussianNB()
m4.fit(X_train, y_train)
pred4=m4.predict(X_test)
print(classification_report(y_test, pred4))
cm6 = pd.DataFrame(confusion_matrix(y_test, pred4), index = labels, columns = labels)

plt.figure(figsize = (10, 8))
sns.heatmap(cm6, annot = True, cbar = False, fmt = 'g')
plt.ylabel('Actual values')
plt.xlabel('Predicted values')
plt.show()

