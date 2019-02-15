import pandas as pd
dataset = pd.read_csv('employees.csv')

dataset.rename(columns = {"Bonus %" : "Bonus","First Name":"Name"}, inplace = True)
dataset.sort_values('Name',ascending = False, inplace = True)

df = dataset[(dataset.Gender == 'Male') & (dataset.Team == 'Finance')]
df1 = dataset.query("Salary > 100000 and Bonus > 10")
df2 = dataset[dataset.Name.isin(['Aaron','Donna'])]






