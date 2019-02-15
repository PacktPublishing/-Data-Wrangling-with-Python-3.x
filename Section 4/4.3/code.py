import pandas as pd
dataset = pd.read_csv('dataset.csv')

columns_name = list(dataset.columns)
dataset.rename(columns = {"Full Name":"Name", "email": "Email Address"},inplace = True)

dataset.drop(columns = ['Income'], inplace = True)

names = list(dataset['Name'])
first_letter = list()

for i in names:
    first_letter.append(i[0])

dataset['first_letter'] = first_letter



























