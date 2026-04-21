import streamlit as st
from PIL import Image

# Import pages
from dashboard import main as dashboard_page
from network_analysis import main as network_page
from agent_console import main as agent_page

# Page Icon
st.set_page_config(
    page_title="AXON: Next-Gen Intelligent Audit System",
    page_icon="🧬",
    layout="wide"
)

# GLOBAL STYLE
st.markdown("""
<style>

/* Background utama */
.stApp {
    background: linear-gradient(135deg, #0f172a, #064e3b);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95);
}

/* KPI card */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 15px;
}

/* Chart putih */
.stPlotlyChart {
    background-color: white !important;
    border-radius: 10px;
    padding: 10px;
}

/* Button */
button[kind="primary"] {
    background-color: #00FF88 !important;
    color: black !important;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:

    # Logo
    try:
        logo = Image.open("assets/Axon_Logo.png")
        st.image(logo, width=100)
    except:
        st.write("🧠")

    st.title("AXON")

    # Navigation
    page = st.radio(
        "Navigation",
        ["Home", "Dashboard", "Network", "Agent"]
    )

    st.markdown("---")
    st.success("System Status: Operational 🟢")

    # CREDIT 
    st.markdown("---")
    st.markdown(
        """
        <div style='font-size:12px; color:#9CA3AF; line-height:1.6'>
        <b>AXON AI Audit</b><br>
        Created by Baptista Yohana Vallen<br>
        Deloitte Digital Camp 2026<br>
        Mentor: Leo Ma
        </div>
        """,
        unsafe_allow_html=True
    )

# HOME PAGE
def home():
    st.title("AXON")
    st.subheader("Next-Gen Agentic AI Audit System")

    st.markdown("""
    **艾克森 (Ài Kè Sēn)**  
    **智链 (Zhì Liàn): Intelligent Risk Chain**

    > *The Neural Core of Compliance.*
    """)

    st.markdown("---")

    # KPI
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Audit Mode", "Proactive")
    c2.metric("Role", "Agentic AI")
    c3.metric("Scope", "Global 🌍")
    c4.metric("Status", "Active 🟢")

    st.markdown("---")

    # ABOUT
    st.markdown("## 🤖 About AXON")
    st.markdown("""
    AXON is an intelligent audit system designed as the **neural intelligence layer of enterprise compliance**.

    Inspired by the biological **axon**, the signal-transmitting component of neurons
    AXON continuously monitors transactional activity, detects risk chains,  
    and autonomously escalates suspicious patterns.

    Traditional audit systems are reactive.  
    **AXON is proactive, adaptive, and AI-driven.**
    """)

    st.markdown("---")

    # FEATURES
    st.markdown("## 🚀 Core Capabilities")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - Fraud probability scoring  
        - Device & IP anomaly detection  
        - Transaction behavior analysis  
        """)

    with col2:
        st.markdown("""
        - Network risk chain detection (智链)  
        - AI-assisted audit decisions  
        - Real-time monitoring dashboard  
        """)

    st.markdown("---")

    st.info("Use the sidebar to explore Dashboard, Network Analysis, and Agent Center.")

# =========================
# ROUTER (SAFE)
# =========================
if page == "Home":
    home()

elif page == "Dashboard":
    try:
        dashboard_page()
    except Exception as e:
        st.error("Error loading Dashboard")
        st.exception(e)

elif page == "Network":
    try:
        network_page()
    except Exception as e:
        st.error("Error loading Network Analysis")
        st.exception(e)

elif page == "Agent":
    try:
        agent_page()
    except Exception as e:
        st.error("Error loading Agent")
        st.exception(e)