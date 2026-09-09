import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('train.csv')

print("="*50)
print("PHASE 3: DATA CLEANING & PREPROCESSING")
print("="*50)

# 1. Missing Values Analysis
print("\n1. Missing Values Before Cleaning:")
print(df.isnull().sum())

# Clean 'Dependents' column (remove '+')
df['Dependents'] = df['Dependents'].str.replace('+', '')

# Handle Missing Values (Imputation)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

print("\n2. Missing Values After Cleaning:")
print(df.isnull().sum())

# Feature Engineering: Total Income
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

# Clean dataset save karein
df.to_csv('cleaned_loan_data.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_loan_data.csv'")

print("\n"+"="*50)
print("PHASE 4: EXPLORATORY DATA ANALYSIS (EDA)")
print("="*50)

# Plots Create & Save Karein
plt.figure(figsize=(12, 4))

# Plot 1: Credit History vs Loan Status
plt.subplot(1, 3, 1)
sns.countplot(data=df, x='Credit_History', hue='Loan_Status')
plt.title('Credit History vs Approval')

# Plot 2: Education vs Loan Status
plt.subplot(1, 3, 2)
sns.countplot(data=df, x='Education', hue='Loan_Status')
plt.title('Education vs Approval')

# Plot 3: Total Income vs Loan Amount
plt.subplot(1, 3, 3)
sns.scatterplot(data=df, x='TotalIncome', y='LoanAmount', hue='Loan_Status')
plt.title('Income vs Loan Amount')

plt.tight_layout()
plt.savefig('eda_plots.png')
print("EDA plots saved as 'eda_plots.png'")