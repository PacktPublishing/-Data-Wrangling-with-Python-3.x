import pandas as pd

d = {'Name':['Jamshaid','Hammas','Shiza','Rimsha','Hammad','Aliza','Adeel',
   'Sana','Khizar','Haris','Zainab','Awais'],
   'Age':[18,16,25,30,23,45,39,31,29,19,35,20],
   'JobRating':[2.2,9.9,3.8,7.0,8.8,1.1,9.8,6.9,5.2,5.9,7.9,3.4]}

df = pd.DataFrame(d)

sum_of_ratings = df['JobRating'].sum()
mean_of_ratings = df['JobRating'].mean()
median_of_ratings = df['JobRating'].median()
mode_of_ratings = df['JobRating'].mode()
std_of_ratings = df['JobRating'].std()

minimum = df['JobRating'].min()
maximum = df['JobRating'].max()

rang = maximum- minimum

































