import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

iris = datasets.load_iris()

samples = iris.data
model = KMeans(n_clusters=3)
model.fit(samples)

labels = model.predict(samples)
# print(labels)

# Store the new Iris measurements
# new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
#    [6.5, 3. , 5.5, 0.4],
#    [5.8, 2.7, 5.1, 1.9]])
# # Predict labels for the new_samples
# labels = model.predict(new_samples)
# print(labels)

# new_names = [iris.target_names[label] for label in labels]
# print(new_names)
target = iris.target

x = samples[:,0]
y = samples[:,1]

plt.scatter(x,y,c=labels,alpha = 0.5)
plt.show()

labels = [iris.target_names[s] for s in model.predict(samples)]

# Code starts here:
species = [iris.target_names[t] for t in list(target)]

df = pd.DataFrame({'labels': labels, 'species': species})

# print(df)

ct = pd.crosstab(df['labels'], df['species'])
print(ct)
