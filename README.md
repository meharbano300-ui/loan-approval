# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on financial and demographic features using **Logistic Regression**.

---

## 📌 Project Overview

Loan approval processing is a critical financial task. Manually assessing creditworthiness can be time-consuming and prone to bias. This project builds a binary classification machine learning pipeline trained on historical financial data to automate and assist in loan eligibility assessment.

### Key Objectives:
- Analyze financial parameters influencing loan approvals.
- Perform thorough data cleaning, feature engineering, and EDA.
- Train a **Logistic Regression** classification model.
- Deploy an interactive, modern web application built with **Streamlit**.

---

## 🛠️ Tech Stack & Tools

- **Programming Language:** Python
- **Data Analysis & Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn (Logistic Regression, Train/Test Split, Metrics)
- **Model Serialization:** Joblib
- **Web Interface:** Streamlit

---

## 📂 Dataset Specification & Features

The model processes applicant financial attributes including:

| Feature Name | Description | Type |
|---|---|---|
| `Gender` | Male / Female | Categorical |
| `Married` | Applicant marital status | Categorical |
| `Dependents` | Number of dependents (0, 1, 2, 3+) | Categorical |
| `Education` | Graduate / Not Graduate | Categorical |
| `Self_Employed` | Self-employed status (Yes / No) | Categorical |
| `ApplicantIncome` | Primary applicant income | Numerical |
| `CoapplicantIncome` | Co-applicant income | Numerical |
| `TotalIncome` | Feature engineered combined income | Numerical |
| `LoanAmount` | Requested loan amount ($ in thousands) | Numerical |
| `Loan_Amount_Term` | Term duration in months | Numerical |
| `Credit_History` | Credit history guidelines met (1.0 / 0.0) | Numerical/Binary |
| `Property_Area` | Urban / Semiurban / Rural | Categorical |
| **`Loan_Status` (Target)** | **Y (Approved) / N (Rejected)** | **Binary Target** |

---

## 🚀 ML Pipeline Architecture

1. **Phase 1: Problem Definition** — Defined as a binary classification task ($Y \in \{0, 1\}$).
2. **Phase 2: Exploratory Data Analysis** — Evaluated dataset shape, target distribution, and missing values.
3. **Phase 3: Data Cleaning & Preprocessing** — Mode/Median imputation, string cleaning, total income creation, and One-Hot Encoding.
4. **Phase 4: EDA Visualizations** — Generated relationship plots saved as `eda_plots.png`.
5. **Phase 5 & 6: Model Training & Evaluation** — Trained Logistic Regression model and exported weights (`loan_model.pkl`).
6. **Phase 7: Web Application** — Interactive UI constructed using Streamlit (`app.py`).

---

## 💻 Local Installation & Setup Instructions

Follow these steps to run the application locally:

### 1. Clone Repository
```bash
https://github.com/meharbano300-ui/loan-approval
cd loan-approval-prediction