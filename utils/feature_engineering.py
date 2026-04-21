import pandas as pd

def engineer_features(df):
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    df["PreviousTransactionDate"] = pd.to_datetime(df["PreviousTransactionDate"])

    df["time_diff"] = (
        df["TransactionDate"] - df["PreviousTransactionDate"]
    ).dt.total_seconds().fillna(0)

    df["device_usage_count"] = df.groupby("DeviceID")["TransactionID"].transform("count")
    df["ip_usage_count"] = df.groupby("IP Address")["TransactionID"].transform("count")

    df["login_risk"] = (df["LoginAttempts"] > 3).astype(int)

    df["amount_balance_ratio"] = (
        df["TransactionAmount"] / df["AccountBalance"].replace(0, 1)
    )

    return df