# 🧠 AXON  
## Next-Gen Agentic AI Audit System  

**艾克森 (Ài Kè Sēn)**  
**智链 (Zhì Liàn): Intelligent Risk Chain**  

> *The Neural Core of Compliance*

---

## 🌍 Business Problem

Traditional audit systems are **reactive and lagging**.

Fraud patterns such as:

- Brush-pumping (fake orders)  
- Shared device fraud rings  
- Coordinated IP-based attacks  
- Cross-border transaction anomalies  

are often detected **after financial damage occurs**.

In a rapidly evolving digital economy, organizations require an intelligent surveillance system capable of:

- Continuous monitoring.
- Autonomous risk detection.
- Network-level anomaly discovery.
- AI-assisted decision support.

---

## 🚀 Solution Overview

AXON introduces an **Agentic AI-powered audit architecture** that transforms traditional compliance frameworks into a proactive risk intelligence system.

Inspired by the biological *axon*, the signal-transmitting component of neurons—AXON functions as the neural intelligence layer of enterprise compliance.

Unlike static rule-based systems, AXON:

- Computes fraud probability in real time.
- Detects hidden Account–Device-IP relationships.
- Identifies coordinated fraud chains (智链 analysis).
- Provides AI-driven audit recommendations.

---

## 🧠 Why Agentic AI?

AXON is not a simple chatbot.

It is designed with an **agentic architecture**, meaning the system:

1. Understands audit intent  
2. Selects appropriate analytical tools  
3. Executes fraud detection logic  
4. Interprets results  
5. Provides structured audit insights  

This enables:

**Reactive Audit → Proactive Intelligence**

---

## 📊 Dataset

This project uses a simulated financial transaction dataset:

`bank_transactions_data.csv`

### Dataset Features

- TransactionID  
- AccountID  
- TransactionAmount  
- TransactionDate  
- TransactionType  
- Location  
- DeviceID  
- IP Address  
- Channel  
- CustomerAge  
- LoginAttempts  
- AccountBalance  

### 🎯 Simulation Objective

The dataset is designed to simulate:

- Fraud transactions  
- Fake order (brush-pumping) activity  
- Device/IP anomaly patterns  
- Cross-border monitoring scenarios  

---

## 🏗️ System Architecture

AXON consists of four core intelligence layers:

### 1️⃣ Data Processing Layer
- Feature engineering  
- Time difference calculation  
- Device/IP frequency analysis  
- Risk signal extraction  

### 2️⃣ Fraud Intelligence Layer
- Machine learning fraud probability model  
- Composite risk scoring  
- High-risk classification  

### 3️⃣ Network Intelligence Layer (智链)
- Account-Device-IP graph modeling  
- Fraud ring detection  
- Shared infrastructure anomaly analysis  

### 4️⃣ Agentic Decision Layer
- AI reasoning engine  
- Tool invocation  
- Risk summarization  
- Audit command execution  

---

## 📊 Key Features

- 📈 Fraud probability scoring (0–100%)  
- 🔗 Network relationship visualization  
- 🌍 Cross-border monitoring simulation  
- 🤖 AI Agent Command Center  
- 📉 Risk distribution dashboard  
- 🧠 Explainable risk signals  

---

## 🖥️ How to Use

### 1️⃣ Home
Overview of AXON architecture and system status.

### 2️⃣ Dashboard
- Total transaction count  
- High-risk detection count  
- Fraud probability distribution  
- Transaction amount vs risk analysis  

### 3️⃣ Network Analysis (智链)
- Visual Account ↔ Device ↔ IP relationships  
- Detect fraud clusters  
- Identify coordinated anomalies  

### 4️⃣ Agent Command Center

AXON's autonomous reasoning layer.

#### Example Commands:
- Calculate fraud loss.
- Find suspicious ip.
- Detect fake orders
- How high risk transactions.
- Summarize fraud pattern.

The agent:
- Interprets request  
- Executes fraud analysis  
- Returns structured insights  

---

## 📉 Example Fraud Pattern

> High login attempts + Shared IP + Low-value repeated transactions  

May indicate:

- Fake order groups  
- Bot-driven transactions  
- Coordinated fraud rings  

---

## 🛠️ Tech Stack

- **Streamlit** → Frontend interface  
- **Scikit-learn** → Fraud detection model  
- **Pandas** → Data processing  
- **NetworkX** → Graph relationship modeling  
- **Matplotlib** → Visualization  
- **Python** → System architecture  

---

## ⚙️ How to Run Locally

```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
