from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp
#Read in csv file
data =pd.read_csv('CSV.csv')
print("Data from file")
print(data)
#data to matrix
dataMatrix=np.asmatrix(data)
print(dataMatrix[:,0])
#create clusters
kmeans = KMeans(n_clusters=2,max_iter=100, random_state=0).fit(dataMatrix)
colors=[]
for labels in (kmeans.labels_):
    if labels == 0:
        colors.append('r')
    elif labels == 1:
        colors.append('b')
print("Kmeans")
print(kmeans.labels_)
print(kmeans.cluster_centers_)
pp.figure(figsize=(8, 6))
pp.scatter([dataMatrix[:,0]], [dataMatrix[:,1]], c=colors)
pp.show()