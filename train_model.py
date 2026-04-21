import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils.feature_engineering import engineer_features

df = pd.read_csv("data/bank_transactions_data.csv")
df = engineer_features(df)

# FRAUD RULE 
df["is_fraud"] = (
    (df["TransactionAmount"] > 3000) |
    (df["LoginAttempts"] > 3) |
    (df["device_usage_count"] > 15) |
    (df["ip_usage_count"] > 15)
).astype(int)

print("Label Distribution:")
print(df["is_fraud"].value_counts())

FEATURES = [
    "TransactionAmount",
    "time_diff",
    "device_usage_count",
    "ip_usage_count",
    "amount_balance_ratio",
    "login_risk"
]

X = df[FEATURES]
y = df["is_fraud"]

# HANDLE IMBALANCE
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y)

joblib.dump(model, "models/fraud_model.pkl")

print("✅ Model trained successfully")