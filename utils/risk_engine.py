def compute_risk_score(row):
    score = (
        row["fraud_probability"] * 0.6 +
        (row["device_usage_count"] > 20) * 0.15 +
        (row["ip_usage_count"] > 20) * 0.15 +
        row["login_risk"] * 0.1
    )
    return score