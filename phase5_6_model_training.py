import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load Cleaned Dataset
df = pd.read_csv('cleaned_loan_data.csv')

print("="*50)
print("PHASE 5 & 6: MODEL TRAINING & EVALUATION")
print("="*50)

# Drop ID column
df = df.drop(columns=['Loan_ID'])

# Convert Target Variable (Y -> 1, N -> 0)
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# One-Hot Encoding for Categorical Features
df = pd.get_dummies(df, drop_first=True)

# Separate Features (X) and Target (y)
X = df.drop(columns=['Loan_Status'])
y = df['Loan_Status']

# Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Save Trained Model & Columns for Web UI
joblib.dump(model, 'loan_model.pkl')
joblib.dump(X.columns.tolist(), 'model_columns.pkl')

print("\nModel saved successfully as 'loan_model.pkl'")
print("Model columns saved as 'model_columns.pkl'")