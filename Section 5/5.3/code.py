import pandas as pd
dataset = pd.read_csv('employees.csv')
dataset.dropna(axis = 0,inplace = True)

teams = list(dataset['Team'])
unique_teams = list(set(teams))

team_mapper = {"Distribution" : 1,
               "Marketing" : 2,
               "Client Services" :3,
               "Product" : 4,
               "Human Resources" : 5,
               "Engineering" :6,
               "Sales" :7,
               "Finance" :8,
               "Legal" : 9,
               "Business Development" : 10}

dataset['Team'] = dataset['Team'].replace(team_mapper)
