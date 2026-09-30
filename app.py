import streamlit as st
import requests


st.title("Credit Card Default Prediction")

st.write("Enter customer information to predict credit card default.")


LIMIT_BAL = st.number_input("Credit Limit", value=20000.0)

CHILDREN = st.number_input(
    "Children",
    min_value=0,
    value=0,
    step=1
)

EDUCATION = st.number_input(
    "Education",
    min_value=0,
    value=2,
    step=1
)

MARRIAGE = st.number_input(
    "Marriage",
    min_value=0,
    value=1,
    step=1
)

AGE = st.number_input(
    "Age",
    min_value=18,
    value=24,
    step=1
)

PAY_0 = st.number_input("PAY_0", value=2, step=1)
PAY_2 = st.number_input("PAY_2", value=2, step=1)
PAY_3 = st.number_input("PAY_3", value=-1, step=1)
PAY_4 = st.number_input("PAY_4", value=-1, step=1)
PAY_5 = st.number_input("PAY_5", value=-2, step=1)
PAY_6 = st.number_input("PAY_6", value=-2, step=1)

BILL_AMT1 = st.number_input("BILL_AMT1", value=3913.0)
BILL_AMT2 = st.number_input("BILL_AMT2", value=3102.0)
BILL_AMT3 = st.number_input("BILL_AMT3", value=689.0)
BILL_AMT4 = st.number_input("BILL_AMT4", value=0.0)
BILL_AMT5 = st.number_input("BILL_AMT5", value=0.0)
BILL_AMT6 = st.number_input("BILL_AMT6", value=0.0)

PAY_AMT1 = st.number_input("PAY_AMT1", value=0.0)
PAY_AMT2 = st.number_input("PAY_AMT2", value=689.0)
PAY_AMT3 = st.number_input("PAY_AMT3", value=0.0)
PAY_AMT4 = st.number_input("PAY_AMT4", value=0.0)
PAY_AMT5 = st.number_input("PAY_AMT5", value=0.0)
PAY_AMT6 = st.number_input("PAY_AMT6", value=0.0)


if st.button("Predict Default"):

    data = {
        "LIMIT_BAL": LIMIT_BAL,
        "CHILDREN": CHILDREN,
        "EDUCATION": EDUCATION,
        "MARRIAGE": MARRIAGE,
        "AGE": AGE,
        "PAY_0": PAY_0,
        "PAY_2": PAY_2,
        "PAY_3": PAY_3,
        "PAY_4": PAY_4,
        "PAY_5": PAY_5,
        "PAY_6": PAY_6,
        "BILL_AMT1": BILL_AMT1,
        "BILL_AMT2": BILL_AMT2,
        "BILL_AMT3": BILL_AMT3,
        "BILL_AMT4": BILL_AMT4,
        "BILL_AMT5": BILL_AMT5,
        "BILL_AMT6": BILL_AMT6,
        "PAY_AMT1": PAY_AMT1,
        "PAY_AMT2": PAY_AMT2,
        "PAY_AMT3": PAY_AMT3,
        "PAY_AMT4": PAY_AMT4,
        "PAY_AMT5": PAY_AMT5,
        "PAY_AMT6": PAY_AMT6
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:

        result = response.json()

        st.subheader("Prediction Result")

        st.write(
            "Prediction:",
            result["prediction_label"]
        )

        st.write(
            "Default Probability:",
            f"{result['default_probability']:.2%}"
        )

    else:

        st.error("Could not connect to the prediction API.")