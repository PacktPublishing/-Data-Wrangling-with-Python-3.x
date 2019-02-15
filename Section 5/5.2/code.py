import pandas as pd
dataset = pd.read_csv('employees.csv')

dataset.dropna(axis = 0, inplace = True)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(dataset['Gender'])
gender_encoded = le.transform(dataset['Gender'])
dataset['Gender_encoded'] = gender_encoded

