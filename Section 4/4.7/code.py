import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,3), columns = list('ABC'))

df.iloc[4:7,0] = np.nan
df.iloc[3:5,1] = np.nan
df.iloc[5:8,2] = np.nan

df1 = df.copy()
df2 = df.copy()
df3 = df.copy()

df1.dropna(axis = 0, inplace = True)
df2.fillna("none",inplace = True)
df3['B'].fillna(df3.mean()['B'],inplace = True)