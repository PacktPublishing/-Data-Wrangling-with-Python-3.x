import csv
with open ('hrdata.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        print (row[0],end = '\t\t')
        print (row[1],end = '\t\t')
        print (row[2],end = '\t\t')
        print (row[3],end = '\n')

import pandas as pd
dataset1 = pd.read_csv('hrdata.csv')
columns1 = list(dataset1.columns)

dataset2 = pd.read_csv('hrdata.csv',header = 0, names = ['Name','HiringDate','wage','paid_leaves_remaining','sick_leaves_remaining','address','working_hours_left','performance_Score'])
columns2 = list(dataset2.columns)
