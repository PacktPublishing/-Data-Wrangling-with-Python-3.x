import pandas as pd
from scipy import stats

#Create a Dictionary of series
d = {'Name':['Jamshaid','Hammas','Shiza','Rimsha','Hammad','Aliza','Adeel',
   'Sana','Khizar','Haris','Zainab','Awais'],
   'Age':[18,16,25,30,23,45,39,31,29,19,35,20],
   'JobRating':[2.2,9.9,3.8,7.0,8.8,1.1,9.8,6.9,5.2,5.9,7.9,3.4]}


#Create a DataFrame
df = pd.DataFrame(d)

job_rating = list(df['JobRating'])

gmean = stats.gmean(job_rating)
hmean = stats.hmean(job_rating)
trim_mean = stats.trim_mean(job_rating,0.1)















