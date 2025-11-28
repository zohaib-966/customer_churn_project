import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("🔮 Customer Churn Prediction System")

# Load trained model
saved = joblib.load("model/churn_model.pkl")
model = saved["model"]
features = saved["features"]

st.subheader("Enter Customer Details")

# USER INPUTS
tenure = st.number_input("Tenure (months)", 0)
usage = st.number_input("Per Month Usage Minutes", 0)
complaints = st.number_input("Number of Complaints", 0)
charges = st.number_input("Monthly Charges", 0)

# Prepare user input in correct format
user_input = {
    "tenure": tenure,
    "usage": usage,
    "complaints": complaints,
    "charges": charges
}

# Predict Button
if st.button("Predict Churn"):
    user_df = pd.DataFrame([user_input])[features]

    prediction = model.predict(user_df)[0]

    if prediction == 1:
        st.error("🔴 Customer will LEAVE the service (Churn).")
    else:
        st.success("🟢 Customer will STAY with the service.")