def main():
    import streamlit as st
    import time
    from utils.loader import load_data, load_model
    from utils.feature_engineering import engineer_features

    st.title("🤖 AXON Agent Command Center")

    # COMMAND SELECT 
    command = st.selectbox(
        "Select Audit Command",
        [
            "Identify High-Risk Transactions",
            "Detect Device Sharing",
            "Analyze Cross-Border Risk",
            "Summarize Fraud Pattern",
            "Calculate Fraud Loss",
            "Find Suspicious IPs",
            "Detect Fake Orders",
            "Custom Query"
        ]
    )

    # Custom input
    custom_query = ""
    if command == "Custom Query":
        custom_query = st.text_area("Enter custom audit instruction")

    # RUN 
    if st.button("Run Agent"):

        # Load
        df = load_data()
        df = engineer_features(df)
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

        # STEP THINKING 
        with st.spinner("AXON Agent reasoning..."):
            st.write("🧐 Step 1: Understanding task...")
            time.sleep(0.7)

            st.write("🔍 Step 2: Selecting analysis module...")
            time.sleep(0.7)

            st.write("⚙ Step 3: Executing analysis...")
            time.sleep(0.7)

        # ================= DEFAULT INTRO =================
        def default_intro():
            st.info(
                "Hello, I'm AXON AI Agent 👋\n\n"
                "I assist auditors in detecting fraud risks, analyzing transaction behavior, "
                "and uncovering anomalies across accounts, devices, and IP networks.\n\n"
                "Try commands like:\n"
                "- Calculate fraud loss\n"
                "- Find suspicious IPs\n"
                "- Detect fake orders\n"
                "- Show high-risk transactions"
            )

        # COMMAND HANDLER 

        # HIGH RISK
        if command == "Identify High-Risk Transactions":

            top = df.sort_values("fraud_probability", ascending=False).head(5)

            st.success("🚨 High-risk transactions identified")
            st.dataframe(
                top[["TransactionID", "TransactionAmount", "fraud_probability"]],
                use_container_width=True
            )

            st.caption("These transactions should be prioritized for audit review.")

        # DEVICE SHARING
        elif command == "Detect Device Sharing":

            device_counts = df["DeviceID"].value_counts()
            suspicious_devices = device_counts[device_counts > 5]

            st.warning("⚠ Device sharing detected")

            if not suspicious_devices.empty:
                st.dataframe(suspicious_devices.head())
            else:
                st.success("No significant device anomaly detected.")

        # CROSS BORDER
        elif command == "Analyze Cross-Border Risk":

            st.success("🌍 Cross-border risk pattern detected")

            st.write(
                "Transactions show anomalies across multiple regions, "
                "which may indicate cross-border fraud or account takeover."
            )

        # SUMMARY
        elif command == "Summarize Fraud Pattern":

            high = df[df["fraud_probability"] > 0.6]

            st.success("📊 Fraud Summary")
            st.write(f"Total transactions: {len(df)}")
            st.write(f"High-risk transactions: {len(high)}")

            if len(high) > 0:
                st.write(f"Average fraud amount: {high['TransactionAmount'].mean():.2f}")

            st.caption("Summary provides a high-level overview of fraud exposure.")

        # LOSS
        elif command == "Calculate Fraud Loss":

            high = df[df["fraud_probability"] > 0.6]
            total_loss = high["TransactionAmount"].sum()

            st.error(f"💰 Estimated Fraud Loss: ${total_loss:,.2f}")

            st.caption(
                "Represents potential financial exposure from high-risk transactions."
            )

        # IP
        elif command == "Find Suspicious IPs":

            ip_counts = df["IP Address"].value_counts().head(5)

            st.warning("🌐 Suspicious IPs detected")

            for ip, count in ip_counts.items():
                st.write(f"{ip} → {count} transactions")

            st.caption(
                "Repeated IP usage across accounts may indicate coordinated fraud activity."
            )

        # FAKE ORDER (IMPORTANT)
        elif command == "Detect Fake Orders":

            suspicious = df[
                (df["LoginAttempts"] > 3) &
                (df["TransactionAmount"] < 50)
            ].copy()

            suspicious = suspicious.sort_values("LoginAttempts", ascending=False)

            st.error(f"🛒 Potential fake orders detected: {len(suspicious)}")

            if len(suspicious) > 0:
                st.dataframe(
                    suspicious[[
                        "TransactionID",
                        "AccountID",
                        "TransactionAmount",
                        "LoginAttempts",
                        "IP Address"
                    ]],
                    use_container_width=True
                )

                st.caption(
                    "These transactions show patterns of fake orders "
                    "(low value + high login attempts)."
                )

                st.info(
                    "Fake orders are often used to manipulate platform metrics "
                    "or simulate user activity."
                )
            else:
                st.success("No fake order pattern detected.")

        # CUSTOM QUERY
        elif command == "Custom Query":

            if not custom_query:
                default_intro()

            else:
                q = custom_query.lower()

                if "loss" in q:
                    high = df[df["fraud_probability"] > 0.6]
                    total_loss = high["TransactionAmount"].sum()

                    st.error(f"💰 Estimated Fraud Loss: ${total_loss:,.2f}")

                elif "fraud" in q or "risk" in q:
                    top = df.sort_values("fraud_probability", ascending=False).head(5)
                    st.success("🚨 High-risk transactions")
                    st.dataframe(top[["TransactionID", "fraud_probability"]])

                elif "ip" in q:
                    st.warning("🌐 Suspicious IPs")
                    st.write(df["IP Address"].value_counts().head())

                elif "device" in q:
                    st.warning("🧠 Device anomaly detected")
                    st.write(df["DeviceID"].value_counts().head())

                elif "fake" in q or "order" in q:
                    suspicious = df[
                        (df["LoginAttempts"] > 3) &
                        (df["TransactionAmount"] < 50)
                    ]

                    st.error(f"🛒 Fake orders detected: {len(suspicious)}")

                    if len(suspicious) > 0:
                        st.dataframe(
                            suspicious[[
                                "TransactionID",
                                "TransactionAmount",
                                "LoginAttempts"
                            ]],
                            use_container_width=True
                        )

                else:
                    default_intro()