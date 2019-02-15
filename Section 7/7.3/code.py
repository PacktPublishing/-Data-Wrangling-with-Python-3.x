import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('iris.csv')

sepal_length = list(dataset['sepal_length'])
sepal_width = list(dataset['sepal_width'])

_,ax = plt.subplots()

ax.scatter(sepal_length,sepal_width,s = 10,color = 'red',alpha = 0.75)
ax.set_title('Scatter Plot')
ax.set_xlabel('Sepal lenght')
ax.set_ylabel('Sepal Width')

_,ax1 = plt.subplots()

ax1.plot(sepal_length,lw = 2,color = 'red',alpha = 0.75)
ax1.set_title('Line Plot')
ax1.set_xlabel('Sepal lenght')

x = np.random.random_integers(1,100,5)
plt.hist(x , bins = 20)
plt.ylabel('Number of Times')
plt.show()


