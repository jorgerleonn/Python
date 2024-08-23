import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

dataset = pd.read_csv('Unsupervised Learning\K-Means Clustering\openpowerlifting.csv')

features = pd.concat([dataset.iloc[:, 1:22], dataset.iloc[:, 24:36]], axis=1)
labels = dataset.iloc[:,24]

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)

num_clusters = list(range(1,9))
inertias = []
for i in num_clusters:
  model = KMeans(n_clusters = i)
  model.fit(features_train, labels_train)
  inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()


#----------------habría que pasar los datos categoricos a numéricos----------------------#