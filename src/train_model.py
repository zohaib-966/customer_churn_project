import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv("data/customer_churn_dataset.csv")

# Rename your columns to standard names
df = df.rename(columns={
    "tenure_months": "tenure",
    "permonth_usage_minutes": "usage",
    "complaints_count": "complaints",
    "monthly_charges": "charges"
})

# Features & target
X = df.drop(["churn", "customer_id"], axis=1)
y = df["churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("Model Accuracy:", acc)

# Create model directory if not exists
os.makedirs("model", exist_ok=True)

# Save model + feature names
joblib.dump(
    {"model": model, "features": list(X.columns)},
    "model/churn_model.pkl"
)

print("Model saved successfully at: model/churn_model.pkl")