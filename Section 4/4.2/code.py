import pandas as pd
dataset = pd.read_csv('dataset.csv')

columns_name = list(dataset.columns)
dataset.shape

dataset.dtypes

dataset['id'] = dataset['id'].astype('float')

dataset.dtypes

rows = dataset[10:17]
