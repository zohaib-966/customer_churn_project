📌 Project Overview

The Customer Churn Prediction System is designed to help telecom companies identify customers who are likely to stop using their service.
Using machine learning, the model predicts whether a customer will leave (churn) or stay, based on their usage patterns and service experience.

This project includes:

A trained machine learning model (Random Forest)

A Streamlit dashboard for interactive prediction

A clean and user-friendly interface for uploading customer data

Real-time churn prediction without manual calculations

🎯 Project Purpose

The main goals of this project are:

To analyze customer behavior and identify churn risk

To help companies take early preventive actions

To provide an automated prediction dashboard

To practice Machine Learning concepts such as:

Data preprocessing

Feature engineering

Train–test split

Model evaluation

Model deployment with Streamlit

🧠 How the Model Works

The model is trained using a Random Forest Classifier on the following features:

tenure_months – How long the customer has been using the service

monthly_usage_minutes – Customer’s monthly usage

complaints_count – Number of complaints filed

monthly_charges – Monthly bill amount

contract_type – Type of contract (month-to-month, yearly, etc.)

✔️ Prediction Output

The model predicts:

🟢 Customer Will Stay

🔴 Customer Will Leave (Churn)

The prediction is displayed inside the dashboard immediately.

📦 Libraries Used
Python Libraries
Library	Purpose
pandas	Load & clean dataset
scikit-learn	Machine learning model training
joblib	Save & load trained ML model
matplotlib / seaborn	Visualizations & charts
streamlit	Build the interactive web dashboard
