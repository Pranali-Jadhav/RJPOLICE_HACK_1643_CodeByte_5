# -*- coding: utf-8 -*-
"""FakeURLDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QYHuybrpVckLzQuvbudX3JqLXbt6sTSd
"""



from google.colab import drive
drive.mount('/content/drive')

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

df = pd.read_csv("/content/drive/MyDrive/Hackathon/dataset_phishing.csv")

print(df.head())

# Select features and target variable
features = df[['length_url', 'length_hostname', 'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm', 'nb_and', 'nb_or']]
target = df['status']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print(classification_report(y_test, y_pred))

# example 1
new_url = "https://zapatopi.net/treeoctopus/"

# Extract features for the new URL
new_features = [len(new_url), len(new_url.split('//')[-1].split('/')[0]), new_url.count('.'), new_url.count('-'),
                new_url.count('@'), new_url.count('?'), new_url.count('&'), new_url.count('|')]

# Reshape the feature array to match the input format expected by the model
new_features_reshaped = [new_features]

# Use the trained model to make predictions
prediction = model.predict(new_features_reshaped)

# Print the prediction
print(f"The URL '{new_url}' is classified as: {prediction[0]}")

# Example 2
new_url = "https://www.amazon.in/"

# Extract features for the new URL
new_features = [len(new_url), len(new_url.split('//')[-1].split('/')[0]), new_url.count('.'), new_url.count('-'),
                new_url.count('@'), new_url.count('?'), new_url.count('&'), new_url.count('|')]

# Reshape the feature array to match the input format expected by the model
new_features_reshaped = [new_features]

# Use the trained model to make predictions
prediction = model.predict(new_features_reshaped)

# Print the prediction
print(f"The URL '{new_url}' is classified as: {prediction[0]}")