import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.cluster import KMeans

digits = sklearn.datasets.load_digits()

samples = digits.data
# print(digits)
# print(digits.DESCR)
# print(digits.data)
# print(digits.target)

# plt.gray()
# plt.matshow(digits.images[100])
# plt.show()
# print(digits.target[100])

num_clusters = list(range(1,9))
inertias = []
for i in num_clusters:
    model = KMeans(n_clusters=i, random_state=42)
    model.fit(samples)
    inertias.append(model.inertia_)
    
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')
 
best_num_clusters = np.argmin(inertias) + 1

for i in range(best_num_clusters):
    # Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)
    # Display images
    ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()


new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.13,4.65,0.00,0.00,0.00,0.00,0.00,1.68,7.32,7.03,0.00,0.00,0.00,0.00,2.75,7.40,7.62,7.62,0.00,0.00,0.00,5.10,7.62,5.72,3.66,7.63,0.76,0.00,0.00,4.57,3.43,0.08,3.05,7.63,0.76,0.00,0.00,0.00,0.00,0.00,2.67,7.63,1.37,0.00,0.00,0.00,0.00,0.00,0.23,2.75,0.08,0.00],
[0.00,0.00,0.69,0.23,0.00,0.00,0.00,0.00,0.15,5.79,7.64,6.72,0.69,0.00,0.00,0.00,1.07,7.39,4.20,7.63,3.44,0.00,0.00,0.00,0.00,0.00,1.99,7.63,2.98,0.00,0.00,0.00,0.00,2.44,7.17,6.41,0.31,0.00,0.00,0.00,4.50,7.63,7.02,1.52,0.76,0.76,0.31,0.00,6.48,7.63,7.63,7.63,7.63,7.63,7.17,0.00,0.00,0.38,1.91,2.29,2.29,2.44,2.60,0.00],
[0.00,0.00,0.61,1.53,0.61,0.00,0.00,0.00,0.00,2.14,7.33,7.63,6.87,0.92,0.00,0.00,0.00,5.88,6.11,3.97,7.63,3.05,0.00,0.00,0.00,0.38,3.21,7.56,7.18,1.07,0.00,0.00,0.00,0.00,2.29,7.48,7.10,0.92,0.00,0.00,0.00,0.46,2.29,5.12,7.63,2.29,0.00,0.00,0.00,2.82,7.62,7.63,5.65,0.69,0.00,0.00,0.00,0.08,0.77,0.54,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.15,3.51,0.69,0.15,5.64,2.44,0.00,0.00,0.92,7.63,3.05,0.76,7.63,3.81,0.00,0.00,0.08,7.40,5.73,5.42,7.63,4.20,0.00,0.00,0.00,4.81,6.87,6.41,7.40,4.58,0.00,0.00,0.00,0.00,0.00,0.00,6.41,5.11,0.00,0.00,0.00,0.00,0.00,0.00,5.11,5.95,0.00,0.00,0.00,0.00,0.00,0.00,0.53,0.76,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  print(new_labels[i])