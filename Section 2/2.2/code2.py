import pandas as pd
sheet1 = pd.read_excel('SampleSuperstore.xls',sheet_name = 'Orders')
sheet2 = pd.read_excel('SampleSuperstore.xls',sheet_name = 'People')
sheet3 = pd.read_excel('SampleSuperstore.xls',sheet_name = 'Returns')

df1 = sheet1.head()
df2 = sheet1.tail()

for i in sheet1.index:
    print(sheet1['Ship Date'][i])

columns = list(sheet1.columns)
dimentions = sheet1.shape

sheet1['Profit'].mean()
sheet1['Profit'].sum()
