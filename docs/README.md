# ChurnGuard — E-Commerce Customer Churn Predictor

A machine learning project that predicts whether an e-commerce customer is
likely to churn, based on their behavior — built as a portfolio project for
Data Analyst / Data Scientist / ML job applications.

## Overview
Given a customer's tenure, order history, satisfaction score, complaints, and
other behavioral data, ChurnGuard predicts the probability that customer will
stop using the platform. The trained model is served through a simple web
form for live predictions.

## Dataset
- Source: [Kaggle — E-commerce Customer Churn](https://www.kaggle.com/datasets/samuelsemaya/e-commerce-customer-churn/data) by samuelsemaya
- 3,941 customers, 11 columns
- Target: `Churn` (1 = left, 0 = stayed) — an imbalanced target (~15% churn rate)

## Approach
1. Cleaned missing values (median imputation) in `Tenure`, `WarehouseToHome`,
   and `DaySinceLastOrder`
2. One-hot encoded categorical features (`PreferedOrderCat`, `MaritalStatus`)
3. Explored churn patterns — customers who complained churned at ~34% vs ~11%
   for those who didn't
4. Trained and compared two models on standardized features:

| Metric | Logistic Regression | Random Forest |
|---|---|---|
| Accuracy | 88.8% | **94.0%** |
| Precision | 74.7% | **86.6%** |
| Recall | 48.1% | **75.2%** |

   Random Forest was selected as the final model — recall (the most important
   metric given the churn imbalance) improved from 48% to 75%.
5. Reviewed feature importance — `Tenure`, `CashbackAmount`, and
   `WarehouseToHome` were the strongest predictors
6. Saved the trained model and scaler, and built a reusable prediction function
7. Built a Flask + Tailwind web app for live predictions

## Tech stack
Python, pandas, numpy, scikit-learn, matplotlib, seaborn, Flask, Tailwind CSS

## Project structure

ChurnGuard/
├── data/ → raw dataset
├── notebooks/ → data exploration and model training
├── src/ → predict.py — reusable prediction function
├── models/ → saved trained model and scaler
├── app/ → Flask backend + Tailwind front end
└── docs/ → this README



## Key takeaway
Switching from Logistic Regression to Random Forest significantly improved
the model's ability to catch actual churners (+27 points of recall), at the
cost of some interpretability — a trade-off worth explicitly calling out, since
plain accuracy alone would have hidden how weak the baseline really was on an
imbalanced target.