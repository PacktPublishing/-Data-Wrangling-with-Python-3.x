import pandas as pd
dataset = pd.read_csv('employees.csv')

dataset.sort_values("First Name",inplace = True)

df = dataset.copy()

df.drop_duplicates(subset = "First Name",keep = False,inplace = True)

df1 = dataset.copy()
df2 = dataset.copy()

df1.drop_duplicates(subset = "First Name",keep = 'first',inplace = True)
df2.drop_duplicates(subset = "First Name",keep = 'last',inplace = True)
