
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load the dataset
data = pd.read_csv('creditcard.csv')
print("Dataset loaded. Shape:", data.shape)

# Features (all columns except 'Class') and target ('Class': 0 = legit, 1 = fraud)
X = data.drop('Class', axis=1)
y = data['Class']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Performance:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'fraud_model.pkl')
print("Model saved as 'fraud_model.pkl'")