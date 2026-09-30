import joblib
import pandas as pd
from pathlib import Path


# ============================================================
# 1. PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "04_models" / "logistic_regression.pkl"
SCALER_PATH = BASE_DIR / "04_models" / "scaler.pkl"


# ============================================================
# 2. LOAD MODEL AND SCALER
# ============================================================

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("Model loaded successfully")
print("Scaler loaded successfully")


# ============================================================
# 3. NEW CUSTOMER DATA
# ============================================================

new_customer = pd.DataFrame({
    "LIMIT_BAL": [50000],

    "CHILDREN": [2],

    "EDUCATION": [2],

    "MARRIAGE": [1],

    "AGE": [30],

    "PAY_0": [0],

    "PAY_2": [0],

    "PAY_3": [0],

    "PAY_4": [0],

    "PAY_5": [0],

    "PAY_6": [0],

    "BILL_AMT1": [50000],

    "BILL_AMT2": [48000],

    "BILL_AMT3": [45000],

    "BILL_AMT4": [40000],

    "BILL_AMT5": [38000],

    "BILL_AMT6": [35000],

    "PAY_AMT1": [2000],

    "PAY_AMT2": [2000],

    "PAY_AMT3": [2000],

    "PAY_AMT4": [2000],

    "PAY_AMT5": [2000],

    "PAY_AMT6": [2000]
})


# ============================================================
# 4. SCALE NEW CUSTOMER
# ============================================================

new_customer_scaled = scaler.transform(new_customer)


# ============================================================
# 5. PREDICTION
# ============================================================

prediction = model.predict(new_customer_scaled)

probability = model.predict_proba(new_customer_scaled)


# ============================================================
# 6. DISPLAY RESULT
# ============================================================

print()
print("Prediction:", prediction[0])

print(
    "Probability of default:",
    probability[0][1]
)


# ============================================================
# 7. HUMAN-READABLE RESULT
# ============================================================

print()

if prediction[0] == 1:
    print("Result: Customer is predicted to DEFAULT.")
else:
    print("Result: Customer is predicted NOT to DEFAULT.")