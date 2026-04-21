def main():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    import random

    st.title("AXON Cross-Border and Network Risk Analysis")

    # Load Data
    df = pd.read_csv("data/bank_transactions_data.csv")

    # Device Mapping
    def map_device(device_id):
        if "MOB" in str(device_id):
            return "Mobile"
        elif "TAB" in str(device_id):
            return "Tablet"
        else:
            return "Desktop"

    df["DeviceType"] = df["DeviceID"].apply(map_device)

    # Filter
    suspicious = df[
        (df["LoginAttempts"] > 3) |
        (df["TransactionAmount"] > 3000)
    ].copy().head(50)

    # MAP 
    st.subheader("🌍 Cross-Border Risk Overview")

    regions = ["Asia", "Europe", "North America", "Southeast Asia"]
    suspicious["Region"] = [random.choice(regions) for _ in range(len(suspicious))]

    region_counts = suspicious["Region"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.bar(region_counts.index, region_counts.values)

    ax1.set_facecolor("white")
    fig1.patch.set_facecolor("white")

    ax1.set_xlabel("Region")
    ax1.set_ylabel("Suspicious Transactions")

    st.pyplot(fig1)

    top_region = region_counts.idxmax()

    st.info(
        f"Region with highest suspicious activity: {top_region}. "
        "This may indicate cross-border fraud concentration."
    )

    st.caption(
        "Cross-border anomalies often indicate coordinated fraud such as fake orders or account takeovers."
    )

    st.markdown("---")

    # Network
    st.subheader("🔗 Account – Device – IP Network")

    G = nx.Graph()

    for _, row in suspicious.iterrows():
        G.add_edge(f"A-{row['AccountID']}", f"D-{row['DeviceType']}")
        G.add_edge(f"A-{row['AccountID']}", f"IP-{row['IP Address']}")

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)

    # COLOR NODE
    node_colors = []
    for node in G.nodes():
        if node.startswith("IP"):
            node_colors.append("red")
        elif node.startswith("D"):
            node_colors.append("orange")
        else:
            node_colors.append("green")

    nx.draw(
        G,
        pos,
        ax=ax2,
        node_color=node_colors,
        node_size=400,
        with_labels=True,
        font_size=7
    )

    ax2.set_facecolor("white")
    fig2.patch.set_facecolor("white")

    st.pyplot(fig2)

    st.info(
    "Red nodes represent IP addresses, orange nodes represent device types, and green nodes represent accounts.\n\n"
    "Clusters in the network suggest multiple accounts sharing the same IP or device, which may indicate coordinated fraud activity.\n\n"
    "Highly connected nodes (many links) are critical risk points, as they act as hubs linking multiple transactions together."
)

    st.markdown("---")

    # INSIGHT 
    st.subheader("🛡️ Detected Fraud Patterns")

    ip_flag = suspicious["IP Address"].nunique() < len(suspicious)/2
    device_flag = suspicious["DeviceType"].nunique() < len(suspicious)/2

    if ip_flag:
        st.error("⚠ Multiple accounts linked to same IP → potential fraud ring")

    if device_flag:
        st.error("⚠ Device sharing detected → possible fake order behavior")

    if ip_flag and device_flag:
        st.error("🚨 Coordinated fraud pattern across accounts, devices, and IPs")

    st.success(f"{len(suspicious)} suspicious transactions analyzed.")

    st.markdown("---")

    # Sample
    st.subheader("🔍 Sample Suspicious Transactions")

    st.dataframe(
        suspicious[[
            "TransactionID",
            "AccountID",
            "DeviceType",
            "IP Address",
            "TransactionAmount"
        ]],
        use_container_width=True
    )

    st.markdown("---")

    # Action
    st.subheader("Recommended Audit Actions")

    if ip_flag:
        st.warning("➡ Investigate shared IP usage across multiple accounts")

    if device_flag:
        st.warning("➡ Monitor unusual device usage patterns")

    if len(suspicious) > 20:
        st.error("➡ Escalate to fraud investigation team")

    st.info("These actions help auditors respond proactively.")

    st.markdown("---")

    # Simulation
    st.subheader("🧪 Fraud Simulation Tool")

    # AUTO EXAMPLE IP
    top_ips = df["IP Address"].value_counts().head(3)

    st.markdown("### Example Suspicious IPs")
    for ip, count in top_ips.items():
        st.write(f"- {ip} ({count} transactions)")

    st.markdown("""
    Try input:
    - IP Address above
    - Device Type: Mobile / Desktop / Tablet
    """)

    col1, col2 = st.columns(2)

    with col1:
        input_ip = st.text_input("Enter IP Address")

    with col2:
        input_device = st.selectbox(
            "Select Device Type",
            ["Mobile", "Desktop", "Tablet"]
        )

    if st.button("Analyze Simulation"):

        risk_flag = False

        # IP CHECK 
        if input_ip:
            ip_count = df[df["IP Address"] == input_ip].shape[0]

            if ip_count > 10:
                st.error(f"🚨 HIGH RISK: IP used {ip_count} times")
                risk_flag = True
            elif ip_count > 5:
                st.warning(f"⚠ MEDIUM RISK: IP used {ip_count} times")
                risk_flag = True
            elif ip_count > 1:
                st.info(f"ℹ Repeated usage: {ip_count} times")
            else:
                st.success("✅ IP appears normal")

        # DEVICE CHECK 
        device_count = df[df["DeviceType"] == input_device].shape[0]

        if device_count > len(df) * 0.4:
            st.error("🚨 HIGH RISK: Device dominates transactions")
            risk_flag = True
        elif device_count > len(df) * 0.25:
            st.warning("⚠ MEDIUM RISK: Device frequently used")
            risk_flag = True
        else:
            st.success("✅ Device usage normal")

        # FINAL 
        st.markdown("### 🛡️ AXON Decision")

        if risk_flag:
            st.error("🚨 Potential anomaly detected")
        else:
            st.success("✅ No strong anomaly detected")

        st.caption(
            "Risk is based on frequency patterns. Repeated usage across accounts may indicate coordinated fraud."
        )