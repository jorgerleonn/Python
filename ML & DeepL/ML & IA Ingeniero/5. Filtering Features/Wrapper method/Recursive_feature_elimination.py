import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
  
# Load the data
health = pd.read_csv("Filtering Features/Wrapper method/dataR2.csv")
x = np.array(health.iloc[:,:-1])
y = np.array(health.iloc[:,-1])
  
# Standardize the data
x = StandardScaler().fit_transform(x)
  
# Logistic regression model
lr = LogisticRegression(max_iter=1000)
  
# Recursive feature elimination
rfe = RFE(lr, n_features_to_select = 3)
rfe.fit(x,y)

# List of features chosen by recursive feature elimination
rfe_features = [f for (f,support) in zip(x, rfe.support_) if support]
print(rfe_features)
# Print the accuracy of the model with features chosen by recursive feature elimination
print(rfe.score(x,y))