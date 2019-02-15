import pandas as pd
dataset = pd.read_csv('employees.csv')
dataset.dropna(axis = 0, inplace = True)

dataset.reset_index(inplace = True)
del dataset['index']

dataset.columns = map(str.lower,dataset.columns)

dataset['first name'] = dataset['first name'].str.strip()

dataset['salary'] = dataset['salary'].astype('int')
dataset['salary'] = dataset['salary'].apply(lambda x:x-1000)

