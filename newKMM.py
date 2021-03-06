

#from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
#from numpy import random, float
import numpy as np
import pandas as pd



in_file = "Dataset.txt"
colnames = [ 'area A', 'perimeter P', 'compactness C = 4*pi*A/P^2','length of kernel','width of kernel','asymmetry coefficient', 'length of kernel groove', 'class']
wheatData = pd.read_csv(in_file,sep='\t', names = colnames);
[row,col] = wheatData.shape
print('Dataset has {0} columns and {1} rows'.format(col, row))
# 2. print top 5 lines
print(wheatData.head(5))
df = wheatData.values

featureX = 0
featureY = 3
data = df[:,[featureX,featureY]]
target = 7
Y = df[:, target]
X = np.array(df[:, [featureX, featureY]])
 

#data = createClusteredData(100, 5)

model = KMeans(n_clusters=3,init='random', max_iter=100, n_init=1, verbose=1)

# Note I'm scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# We can look at the clusters each data point was assigned to
print('model.labels_', model.labels_)


#dict={str(Kama), str(Rosa), str(Canadian)}
# And we'll visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.title('kMeans scatter plot')
plt.legend(scatterpoints = 10, loc ='lower right', prpp = dict(size =3)) # to do legend
plt.xlabel(str(colnames[featureX]))
plt.ylabel(str(colnames[featureY]))
plt.show()
colors = ['navy', 'turquoise', 'darkorange']
for n, color in enumerate(colors):
    data = X[Y == n+1]
    plt.scatter(data[:, 0], data[:, 1], marker='x', color=color)
    plt.title('kMeans scatter plot')
    plt.xlabel(str(colnames[featureX]))
    plt.ylabel(str(colnames[featureY]))
