import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load and train the model
df = pd.read_csv(r'C:\Users\DELL\Downloads\heart_disease_data.csv')
X = df.drop(columns='target', axis=1)
Y = df['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Model trained and saved successfully!')
