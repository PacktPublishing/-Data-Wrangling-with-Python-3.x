import pandas as pd
dataset = pd.read_csv('iris.csv')
dataset.boxplot(column = 'sepal_width',by = 'species')

import matplotlib.pyplot as plt

hours_slices = [8,16]
activities = ['work','sleep']
colors = ['g','r']

plt.pie(hours_slices,labels=activities,colors=colors,startangle=90,autopct='%.1f%%')
plt.show()
































