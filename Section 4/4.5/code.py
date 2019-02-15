import pandas as pd
dataset = pd.read_csv('employees.csv')

first_row = dataset.iloc[[0]]
last_row = dataset.iloc[[-1]]

first_column = dataset.iloc[:,0]
last_column = dataset.iloc[:,-1]

first_five_rows = dataset.iloc[0:5]
first_five_columns = dataset.iloc[:, 0:5]

df = dataset.iloc[[0,4,6],[0,1,2]]

df1 = dataset.loc[dataset['First Name'] == 'Aaron']
