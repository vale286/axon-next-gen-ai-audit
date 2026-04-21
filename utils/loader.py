import streamlit as st
import pandas as pd
import joblib
from utils.feature_engineering import engineer_features

@st.cache_data
def load_data():
    df = pd.read_csv("data/bank_transactions_data.csv")
    df = engineer_features(df)
    return df

@st.cache_resource
def load_model():
    return joblib.load("models/fraud_model.pkl")