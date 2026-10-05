from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI()


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# LOAD MODEL AND SCALER
# ==========================================

model = joblib.load("04_models/logistic_regression.pkl")
scaler = joblib.load("04_models/scaler.pkl")


# ==========================================
# INPUT DATA MODEL
# 23 FEATURES
# ==========================================

class CustomerData(BaseModel):

    LIMIT_BAL: float
    CHILDREN: float
    EDUCATION: float
    MARRIAGE: float
    AGE: float

    PAY_0: float
    PAY_2: float
    PAY_3: float
    PAY_4: float
    PAY_5: float
    PAY_6: float

    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float

    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float


# ==========================================
# HOME ROUTE
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Credit Card Default Prediction API is running"
    }


# ==========================================
# PREDICTION ROUTE
# ==========================================

@app.post("/predict")
def predict(data: CustomerData):

    # Create input array
    input_data = np.array([[
        data.LIMIT_BAL,
        data.CHILDREN,
        data.EDUCATION,
        data.MARRIAGE,
        data.AGE,

        data.PAY_0,
        data.PAY_2,
        data.PAY_3,
        data.PAY_4,
        data.PAY_5,
        data.PAY_6,

        data.BILL_AMT1,
        data.BILL_AMT2,
        data.BILL_AMT3,
        data.BILL_AMT4,
        data.BILL_AMT5,
        data.BILL_AMT6,

        data.PAY_AMT1,
        data.PAY_AMT2,
        data.PAY_AMT3,
        data.PAY_AMT4,
        data.PAY_AMT5,
        data.PAY_AMT6
    ]])


    # Scale the input
    input_scaled = scaler.transform(input_data)


    # Make prediction
    prediction = model.predict(input_scaled)[0]


    # Get default probability
    probability = model.predict_proba(input_scaled)[0][1]


    # Convert prediction to label
    if prediction == 1:
        result = "Default"
    else:
        result = "No Default"


    # Return result to frontend
    return {
        "prediction": int(prediction),
        "prediction_label": result,
        "default_probability": float(probability)
    }

