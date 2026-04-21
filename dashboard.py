def main():
    import streamlit as st
    import matplotlib.pyplot as plt
    from utils.loader import load_data, load_model
    from agents.tools import fraud_prediction_tool, risk_decision_tool

    st.title("📊 AXON Risk Dashboard")

    # Load Data
    df = load_data()
    model = load_model()

    FEATURES = [
        "TransactionAmount",
        "time_diff",
        "device_usage_count",
        "ip_usage_count",
        "amount_balance_ratio",
        "login_risk"
    ]

    probs = model.predict_proba(df[FEATURES])
    df["fraud_probability"] = probs[:, 1] if probs.shape[1] > 1 else 0.0

    # RISK LABEL
    df["risk_level"] = df["fraud_probability"].apply(
        lambda x: "HIGH" if x > 0.6 else "LOW"
    )

    # KPI
    high = df[df["fraud_probability"] > 0.6]

    col1, col2 = st.columns(2)
    col1.metric("Total Transactions", len(df))
    col2.metric("🚨 High Risk Transactions", len(high))

    # AUTO SUMMARY
    st.success(
        f"AXON detected {len(high)} high-risk transactions out of {len(df)} total transactions."
    )

    st.markdown("---")

    # DISTRIBUTION 
    st.subheader("📊 Fraud Risk Distribution")

    fig, ax = plt.subplots()
    ax.hist(df["fraud_probability"], bins=20)

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    ax.set_xlabel("Fraud Probability")
    ax.set_ylabel("Number of Transactions")

    st.pyplot(fig)

    st.info(
        "Most transactions are low-risk, while a small portion shows elevated risk. "
        "This reflects real-world fraud patterns where anomalies are rare but critical."
    )

    st.markdown("---")

    # 📊 SCATTER 
    st.subheader("💰 Transaction Amount vs Risk")

    colors = ["red" if x > 0.6 else "green" for x in df["fraud_probability"]]

    fig2, ax2 = plt.subplots()
    ax2.scatter(df["TransactionAmount"], df["fraud_probability"], c=colors)

    ax2.set_facecolor("white")
    fig2.patch.set_facecolor("white")

    ax2.set_xlabel("Transaction Amount")
    ax2.set_ylabel("Fraud Probability")

    st.pyplot(fig2)

    st.info(
        "Red points indicate high-risk transactions. "
        "Higher amounts combined with abnormal behavior increase fraud likelihood."
    )

    st.markdown("---")

    # TOP HIGH
    st.markdown("## 🚨 Top High Risk Transactions")

    top_high = df.sort_values("fraud_probability", ascending=False).head(5)

    st.dataframe(
        top_high[[
            "TransactionID",
            "TransactionAmount",
            "fraud_probability",
            "risk_level"
        ]],
        use_container_width=True
    )

    st.caption("These transactions should be prioritized for audit investigation.")

    st.markdown("---")

    # LOW SAMPLE 
    st.markdown("## 🟢 Sample Low Risk Transactions")

    low_sample = df.sort_values("fraud_probability", ascending=True).head(5)

    st.dataframe(
        low_sample[[
            "TransactionID",
            "TransactionAmount",
            "fraud_probability",
            "risk_level"
        ]],
        use_container_width=True
    )

    st.caption("These represent normal transaction behavior.")

    st.markdown("---")

    # ANALYZE 
    st.markdown("## 🔎 Analyze Transaction")

    selected_id = st.selectbox(
        "Select Transaction",
        df.sort_values("fraud_probability", ascending=False)["TransactionID"]
    )

    if st.button("Analyze Transaction"):
        row = df[df["TransactionID"] == selected_id].iloc[0].to_dict()

        result = fraud_prediction_tool(row)
        decision = risk_decision_tool(result)

        st.metric("Fraud Probability", f"{result['fraud_probability']*100:.2f}%")

        # STATUS
        if result["fraud_probability"] > 0.6:
            st.error("🚨 HIGH RISK")
        else:
            st.success("✅ LOW RISK")

        # REASONING
        st.write("### 🧠 Detected Pattern")
        for r in decision["reasoning"]:
            st.write("-", r)

        # RECOMMENDATION
        st.write("### 📌 Recommended Action")

        if result["fraud_probability"] > 0.6:
            st.write("- Flag transaction for manual audit.")
            st.write("- Monitor related accounts and devices.")
            st.write("- Investigate IP and device linkage.")
        else:
            st.write("- No immediate action required.")
            st.write("- Continue monitoring behavior.")
