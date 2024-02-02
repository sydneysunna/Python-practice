import sklearn
from sklearn import datasets
iris= datasets.load_iris()
print(iris.data.shape)
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.decomposition import PCA 
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as StandardScaler
import random

######## Plotting a test scatter plot with matplotlib########
#plt.style.use('_mpl-gallery')

# make the data
#np.random.seed(3)
#x = 4 + np.random.normal(0, 2, 24)
#y = 4 + np.random.normal(0, 2, len(x))
# size and color:
#sizes = np.random.uniform(15, 80, len(x))
#colors = np.random.uniform(15, 80, len(x))

# plot
#fig, ax = plt.subplots()

#ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       #ylim=(0, 8), yticks=np.arange(1, 8))

#plt.show()
########################################################

###Plot the Iris database

import matplotlib.pyplot as plt

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()