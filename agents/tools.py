import joblib
import pandas as pd

model = joblib.load("models/fraud_model.pkl")

FEATURES = [
    "TransactionAmount",
    "time_diff",
    "device_usage_count",
    "ip_usage_count",
    "amount_balance_ratio",
    "login_risk"
]

def fraud_prediction_tool(transaction_dict):
    df_input = pd.DataFrame([transaction_dict])
    df_input = df_input[FEATURES]

    probs = model.predict_proba(df_input)
    prob = probs[0][1] if probs.shape[1] > 1 else 0.0

    reasoning = []

    # PATTERN 1: Account Takeover
    if transaction_dict["LoginAttempts"] > 2:
        reasoning.append("Multiple login attempts detected → possible account takeover")

    # PATTERN 2: Shared IP
    if transaction_dict["ip_usage_count"] > 10:
        reasoning.append("High IP reuse across accounts → potential coordinated activity")

    # PATTERN 3: Device Sharing
    if transaction_dict["device_usage_count"] > 10:
        reasoning.append("Device used across multiple accounts → suspicious behavior")

    # PATTERN 4: High Amount
    if transaction_dict["TransactionAmount"] > 2000:
        reasoning.append("High transaction amount detected")

    # COMBINED PATTERN (INI YANG POWERFUL)
    if (
        transaction_dict["LoginAttempts"] > 2 and
        transaction_dict["ip_usage_count"] > 10
    ):
        reasoning.append("Pattern match: Login abuse + shared IP → high fraud likelihood")

    if not reasoning:
        reasoning.append("Transaction behavior appears normal")

    return {
        "fraud_probability": float(prob),
        "reasoning": reasoning
    }


def risk_decision_tool(data):
    prob = data["fraud_probability"]

    if prob > 0.6:
        decision = "🚨 HIGH RISK"
    else:
        decision = "✅ LOW RISK"

    return {
        "decision": decision,
        "reasoning": data["reasoning"]
    }