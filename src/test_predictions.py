from predict import predict_churn

low_risk_customer = {
    'Tenure': 36,
    'WarehouseToHome': 8,
    'NumberOfDeviceRegistered': 2,
    'SatisfactionScore': 5,
    'NumberOfAddress': 1,
    'Complain': 0,
    'DaySinceLastOrder': 2,
    'CashbackAmount': 280,
    'PreferedOrderCat_Grocery': False,
    'PreferedOrderCat_Laptop & Accessory': True,
    'PreferedOrderCat_Mobile': False,
    'PreferedOrderCat_Mobile Phone': False,
    'PreferedOrderCat_Others': False,
    'MaritalStatus_Married': True,
    'MaritalStatus_Single': False
}

high_risk_customer = {
    'Tenure': 1,
    'WarehouseToHome': 35,
    'NumberOfDeviceRegistered': 5,
    'SatisfactionScore': 1,
    'NumberOfAddress': 6,
    'Complain': 1,
    'DaySinceLastOrder': 20,
    'CashbackAmount': 90,
    'PreferedOrderCat_Grocery': False,
    'PreferedOrderCat_Laptop & Accessory': False,
    'PreferedOrderCat_Mobile': False,
    'PreferedOrderCat_Mobile Phone': True,
    'PreferedOrderCat_Others': False,
    'MaritalStatus_Married': False,
    'MaritalStatus_Single': True
}

print(f"Low-risk customer churn probability: {predict_churn(low_risk_customer)}%")
print(f"High-risk customer churn probability: {predict_churn(high_risk_customer)}%")