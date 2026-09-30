from pathlib import Path
import joblib
from fastapi import FastAPI
import numpy as np

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "04_models" / "logistic_regression.pkl"
scaler_path = BASE_DIR / "04_models" / "scaler.pkl"

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
from pydantic import BaseModel


class CustomerData(BaseModel):
    LIMIT_BAL: float
    CHILDREN: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
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

@app.post("/predict")
def predict(data: CustomerData):

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

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        result = "Default"
    else:
        result = "No Default"

    return {
        "prediction": int(prediction),
        "prediction_label": result,
        "default_probability": float(probability)
    }