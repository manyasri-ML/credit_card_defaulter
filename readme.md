# 💳 Credit Card Default Prediction

A Machine Learning project that predicts whether a customer is likely to **default on their credit card payment** based on their financial and demographic information.

The main focus of this project is the **Machine Learning model, data preprocessing, model training, evaluation, and backend API development using FastAPI**.

---

## 📌 Project Overview

Credit card default prediction is a binary classification problem.

The model predicts:

* `0` → Customer is unlikely to default
* `1` → Customer is likely to default

The project demonstrates the complete workflow from **data analysis → machine learning → model saving → API development → deployment**.

---

## 🎯 Project Objectives

* Analyze customer credit card data
* Perform Exploratory Data Analysis (EDA)
* Preprocess the dataset
* Train a Logistic Regression classification model
* Evaluate model performance
* Save the trained model
* Build a REST API using FastAPI
* Accept new customer information through an API
* Return a default prediction
* Deploy the application

---

## 🗂️ Project Structure

```text
credit_card_default/
│
├── 02_notebook/
│   └── 04_logistic_regression.ipynb
│
├── 04_models/
│   └── logistic_regression.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── app.py
├── requirements.txt
├── readme.md
└── .gitignore
```

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Save Model
   ↓
FastAPI Backend
   ↓
Prediction API
```

---

## 🤖 Machine Learning Model

The project uses **Logistic Regression** for binary classification.

### Why Logistic Regression?

Logistic Regression is suitable for this problem because the target variable has two possible outcomes:

```text
0 → No Default
1 → Default
```

The model learns the relationship between customer features and the probability of credit card default.

---

## 📊 Model Evaluation

The model was evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Cross-validation was also used to check the model's performance across different subsets of the training data.

---

## 🧠 Backend — FastAPI

The trained machine learning model is integrated into a **FastAPI backend**.

The backend is responsible for:

1. Receiving customer information
2. Validating the input
3. Preparing the input for the model
4. Loading the trained Logistic Regression model
5. Generating the prediction
6. Returning the prediction through an API response

### Example API Request

```json
{
  "LIMIT_BAL": 20000,
  "SEX": 2,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 24,
  "PAY_0": 2,
  "PAY_2": 2,
  "PAY_3": 0,
  "PAY_4": 0,
  "PAY_5": 0,
  "PAY_6": 0
}
```

### Example Response

```json
{
  "prediction": 0,
  "message": "Customer is unlikely to default"
}
```

---

## 🔌 API Endpoint

The backend provides an endpoint for making predictions.

```text
POST /predict
```

The API accepts customer details and returns the predicted credit card default status.

FastAPI also provides interactive API documentation through:

```text
/docs
```

---

## 🌐 Frontend

A basic frontend interface was used to demonstrate the connection between the user interface and the FastAPI backend.

**The frontend was not the main focus of this project.**

The primary work and learning focus was on:

* Machine Learning
* Data preprocessing
* Model training
* Model evaluation
* Model serialization
* FastAPI
* API integration
* Backend deployment

The frontend was used mainly as a demonstration interface for sending input data to the prediction API.

---

## 🚀 Deployment

The backend API was prepared for deployment so that the machine learning prediction service can be accessed remotely.

The application uses **Uvicorn** as the ASGI server for running FastAPI.

Example:

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8001
```

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib

### Data Visualization

* Matplotlib
* Seaborn

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Deployment & Version Control

* Git
* GitHub
* Netlify / deployment platform for demonstration

---

## 📚 What I Learned

Through this project, I worked with:

* Exploratory Data Analysis
* Data preprocessing
* Feature selection
* Train-test splitting
* Logistic Regression
* Cross-validation
* Classification metrics
* Confusion matrix
* Model serialization using Joblib
* Creating APIs with FastAPI
* Request validation using Pydantic
* Connecting a machine learning model with an API
* Git and GitHub
* Deploying a machine learning application

---

## 🔮 Future Improvements

Possible improvements include:

* Trying additional classification algorithms
* Hyperparameter tuning
* Handling class imbalance
* Improving feature engineering
* Comparing multiple models
* Improving API security
* Building a more advanced frontend
* Adding monitoring for deployed predictions

---

## 👩‍💻 Author

**Manyasri**

This project was developed as a practical Machine Learning project to understand the complete process of taking a trained ML model from experimentation to a deployable backend API.


