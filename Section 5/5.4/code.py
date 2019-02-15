import pandas as pd
dataset = pd.read_csv('employees.csv')
dataset.rename (columns = {"Bonus %" : "Bonus" ,"First Name" : "Name"},inplace = True)

from sklearn import preprocessing

df1 = dataset.copy()
df2 = dataset.copy()

min_max = preprocessing.MinMaxScaler(feature_range = (0,1))
df1[['Salary']] = min_max.fit_transform(df1[['Salary']])

sc = preprocessing.StandardScaler()
df2[['Salary']] = sc.fit_transform(df2[['Salary']])
