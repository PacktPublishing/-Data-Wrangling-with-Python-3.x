import pandas as pd
dataset = pd.read_csv('zoo.csv')

group_by_result = dataset.groupby('animal',as_index = False).size().reset_index(name = 'count')

group_by_result1 = dataset['water_need'].groupby(dataset['animal'])
result = group_by_result1.mean()



