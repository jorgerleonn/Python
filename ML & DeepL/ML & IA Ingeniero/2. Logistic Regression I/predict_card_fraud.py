import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
transactions = pd.read_csv('transactions_modified.csv')
transactions = pd.DataFrame(transactions)
print(transactions.head())
print(transactions.info())
# How many fraudulent transactions?
amount_of_Frauds = transactions.groupby('isFraud').apply(lambda group: group['isFraud'][group['isFraud'] == 1].sum())

# Summary statistics on amount column
# print(transactions['amount'].describe())
# Create isPayment field
transactions['isPayment'] = transactions['type'].apply(lambda x: 1 if x in ['PAYMENT','DEBIT'] else 0)

# Create isMovement field
transactions['isMovement'] = transactions['type'].apply(lambda x: 1 if x in ['CASH_OUT','TRANSFER'] else 0)

# Create accountDiff field
transactions['accountDiff'] = abs(transactions['oldbalanceOrg'] - transactions['oldbalanceDest'])

# Create features and label variables
features = transactions[['amount','isPayment','isMovement','accountDiff']]
label = transactions[['isFraud']]
# Split dataset
features_train,features_test,label_train,label_test = train_test_split(features, label,test_size = 0.3)

# Normalize the features variables
std_scaler = StandardScaler()
features_train_scaled = std_scaler.fit_transform(features_train)
features_test_scaled = std_scaler.transform(features_test)
std_scaler.fit(features_test)
# Fit the model to the training data
lr = LogisticRegression()
model = lr.fit(features_train_scaled, label_train)

# Score the model on the training data
print(model.score(features_train_scaled, label_train))

# Score the model on the test data
print(model.score(features_test_scaled, label_test))

# Print the model coefficients
print(model.coef_)

# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction
your_transaction = np.array([1131750.38, 0.0,1.0, 818679.8499999999])

# Combine new transactions into a single array
sample_transactions = np.array([transaction1,transaction2,transaction3,your_transaction])

# Normalize the new transactions
sample_transactions = std_scaler.transform(sample_transactions)

# Predict fraud on the new transactions
predictions = model.predict(sample_transactions)
print(predictions)

# Show probabilities on the new transactions
probabilities = model.predict_proba(sample_transactions)
print(probabilities)