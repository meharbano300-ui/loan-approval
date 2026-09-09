import pandas as pd

# Phase 1: Problem Definition & Variables
print("="*50)
print("PHASE 1: PROBLEM UNDERSTANDING")
print("="*50)
print("Target Variable: Loan_Status (Y = Approved, N = Rejected)")
print("Input Features: Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area")
print("Model Type: Classification (Binary Prediction)\n")

# Phase 2: Dataset Loading & Exploration
print("="*50)
print("PHASE 2: DATASET EXPLORATION")
print("="*50)

# Load dataset
df = pd.read_csv('train.csv')

print("\n1. Dataset Preview (First 5 rows):")
print(df.head())

print("\n2. Dataset Shape (Rows, Columns):")
print(df.shape)

print("\n3. Data Types & Info:")
print(df.dtypes)

print("\n4. Approval Distribution (Target Count):")
print(df['Loan_Status'].value_counts())