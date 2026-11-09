import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, '..', 'models', 'churn_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, '..', 'models', 'scaler.pkl'))

def predict_churn(customer_dict):
    df = pd.DataFrame([customer_dict])
    df_scaled = scaler.transform(df)
    probability = model.predict_proba(df_scaled)[0][1]
    return round(probability * 100, 2)



if __name__ == "__main__":
    sample_customer = {
        'Tenure': 3,
        'WarehouseToHome': 25,
        'NumberOfDeviceRegistered': 4,
        'SatisfactionScore': 2,
        'NumberOfAddress': 5,
        'Complain': 1,
        'DaySinceLastOrder': 15,
        'CashbackAmount': 120,
        'PreferedOrderCat_Grocery': False,
        'PreferedOrderCat_Laptop & Accessory': False,
        'PreferedOrderCat_Mobile': True,
        'PreferedOrderCat_Mobile Phone': False,
        'PreferedOrderCat_Others': False,
        'MaritalStatus_Married': False,
        'MaritalStatus_Single': True
    }

    result = predict_churn(sample_customer)
    print(f"Churn probability: {result}%")