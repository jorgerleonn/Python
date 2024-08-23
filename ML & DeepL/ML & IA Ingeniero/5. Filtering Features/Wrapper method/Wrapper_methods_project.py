import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE

os.system('cls')
obesity = pd.read_csv('Filtering Features/Wrapper method/obesity.csv')

# print(obesity.head())
 
features = obesity.iloc[:,:-1]
labels = obesity.iloc[:,-1]
 
#--------------------------SEQUENTIAL FORWARD SELECTION-----------------------------------#
 
lr = LogisticRegression(max_iter=1000)

lr.fit(features,labels)

print(lr.score(features,labels))

sfs = SFS(estimator=lr, k_features=9, forward=True, floating=True, scoring='accuracy', cv=0)

sfs.fit(features,labels)

print(sfs.subsets_[9])
print(sfs.subsets_[9]['feature_names'])
print(sfs.subsets_[9]['avg_score'])

plot_sfs(sfs.get_metric_dict())

#---------------------------SEQUENTIAL BACKWARD SELECTION---------------------------------#

sbs = SFS(estimator=lr, k_features=7, forward=False, floating=False, scoring='accuracy', cv=0)
sbs.fit(features,labels)

print(sbs.subsets_[7])
print(sbs.subsets_[7]['feature_names'])
print(sbs.subsets_[7]['avg_score'])

plot_sfs(sbs.get_metric_dict())
plt.show()

#--------------------------RECURSIVE FEATURE ELIMINATION---------------------------------#  

# Get feature names
feature_columns = features.columns

# Standardize the data
scaler = StandardScaler()
features = pd.DataFrame(scaler.fit_transform(features))
# Create a recursive feature elimination model
rfe = RFE(estimator=lr, n_features_to_select=8)

# Fit the recursive feature elimination model to X and y
rfe.fit(features,labels)

# See which features recursive feature elimination chose
rfe_features = [f for (f,support) in zip(feature_columns, rfe.support_) if support]

# Print the model accuracy after doing recursive feature elimination
print(rfe.score(features, labels))
