# 💳 Credit Card Default Prediction

## 📌 Project Overview

This project is a **Machine Learning web application** that predicts whether a credit card customer is likely to default on their payment.

The project covers the complete ML application workflow:

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preparation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
FastAPI Backend
   ↓
Frontend
   ↓
Prediction
```

The trained Machine Learning model is integrated with a **FastAPI backend** and a **web frontend**, allowing users to enter customer information and receive a prediction.

---

# 🎯 Project Objective

The objective of this project is to predict whether a customer will default on their credit card payment.

The target variable is binary:

```text
0 → No Default
1 → Default
```

The application also returns the probability of default.

Example:

```text
Prediction: Default
Default Probability: 72.45%
```

---

# 📊 Dataset

The dataset contains demographic information, credit information, payment history, bill amounts, and previous payment amounts.

### Customer Information

* `LIMIT_BAL` — Credit limit
* `EDUCATION` — Education level
* `MARRIAGE` — Marital status
* `AGE` — Customer age
* `CHILDREN` — Number of children

### Payment History

* `PAY_0`
* `PAY_2`
* `PAY_3`
* `PAY_4`
* `PAY_5`
* `PAY_6`

### Bill Amounts

* `BILL_AMT1`
* `BILL_AMT2`
* `BILL_AMT3`
* `BILL_AMT4`
* `BILL_AMT5`
* `BILL_AMT6`

### Previous Payments

* `PAY_AMT1`
* `PAY_AMT2`
* `PAY_AMT3`
* `PAY_AMT4`
* `PAY_AMT5`
* `PAY_AMT6`

---

# 🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the dataset before building the model.

The analysis included:

* Understanding the dataset structure
* Checking missing values
* Checking duplicate records
* Analyzing numerical features
* Analyzing categorical features
* Studying feature distributions
* Checking correlations
* Understanding the target variable
* Studying relationships between customer characteristics and default behavior

EDA helped determine how the data should be prepared before training the model.

---

# 🤖 Machine Learning Model

This project uses **Logistic Regression** for binary classification.

The model predicts:

```text
0 → No Default
1 → Default
```

Logistic Regression was selected because the problem is a binary classification problem and the model can provide prediction probabilities.

---

# ⚙️ Data Preprocessing

Before sending customer data to the model, the input features are scaled using the same scaler used during model training.

The prediction pipeline is:

```text
User Input
    ↓
Scaler
    ↓
Scaled Features
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Probability
```

The trained scaler is saved so that new data is transformed in the same way as the training data.

---

# 💾 Saved Machine Learning Files

The trained model files are stored inside:

```text
04_models/
```

They include:

```text
04_models/
├── logistic_regression.pkl
└── scaler.pkl
```

### `logistic_regression.pkl`

Contains the trained Logistic Regression model.

### `scaler.pkl`

Contains the scaler used for preprocessing.

Saving these files allows the trained model to be loaded later without retraining it every time the application starts.

---

# 📁 Project Structure

The complete project is organized as follows:

```text
credict_card_fault/
│
├── 01_data/
│   └|─ 01_raw
│    |     |___credit_card_default.csv
|    |___02_processed
|           |__cleaned_data.csv
├── 02_notebook/
│   └── Jupyter notebooks
│       ├── 01_credit_default_analysis.ipynb
│       ├── 02_data_cleaning.ipynb
│       ├── 03_eda.ipynb
│       └── 04_logistic_regression.pkl
│
├── 04_models/
│   ├── logistic_regression.pkl
│   └── scaler.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── src/
│   └── __init__.py
│   |___predict.py
|   |___train.py
├── app.py
├── requirement.txt
├── readme.md
└── venv/
```

### Folder Responsibilities

| Folder/File       | Purpose                                          |
| ----------------- | ------------------------------------------------ |
| `01_data/`        | Stores the dataset                               |
| `02_notebook/`    | EDA, preprocessing, training and experimentation |
| `04_models/`      | Stores trained ML model and scaler               |
| `frontend/`       | User interface                                   |
| `src/`            | Supporting project/source files                  |
| `app.py`          | FastAPI backend                                  |
| `requirement.txt` | Python dependencies                              |
| `readme.md`       | Project documentation                            |
| `venv/`           | Python virtual environment                       |

---

# 🎨 Frontend

The frontend is located inside:

```text
frontend/
```

It contains:

```text
frontend/
├── index.html
├── style.css
└── script.js
```

### `index.html`

Creates the structure of the web page and input form.

### `style.css`

Controls the appearance and layout of the application.

### `script.js`

Handles:

* Reading user input
* Converting values into numbers
* Creating the JSON request
* Sending the request to FastAPI
* Receiving the prediction
* Displaying the prediction result

The frontend was developed with **AI assistance**, particularly for creating and improving the HTML, CSS, and JavaScript interface. The frontend is integrated with the FastAPI backend and the trained ML model as part of this project.

---

# 🚀 Backend API

The backend is implemented using **FastAPI**.

The backend file is:

```text
app.py
```

The backend is responsible for:

1. Receiving customer data
2. Validating the input
3. Preparing the input
4. Scaling the features
5. Loading the trained ML model
6. Making the prediction
7. Calculating the default probability
8. Returning the result as JSON

---

# 🌐 API Endpoints

## Home Endpoint

```text
GET /
```

Used to check whether the API is running.

Example response:

```json
{
    "message": "Credit Card Default Prediction API is running"
}
```

---

## Prediction Endpoint

```text
POST /predict
```

This endpoint receives customer information and returns the prediction.

Example request:

```json
{
    "LIMIT_BAL": 50000,
    "CHILDREN": 0,
    "EDUCATION": 2,
    "MARRIAGE": 1,
    "AGE": 30,
    "PAY_0": 0,
    "PAY_2": 0,
    "PAY_3": 0,
    "PAY_4": 0,
    "PAY_5": 0,
    "PAY_6": 0,
    "BILL_AMT1": 5000,
    "BILL_AMT2": 4500,
    "BILL_AMT3": 4000,
    "BILL_AMT4": 3500,
    "BILL_AMT5": 3000,
    "BILL_AMT6": 2500,
    "PAY_AMT1": 1000,
    "PAY_AMT2": 1000,
    "PAY_AMT3": 1000,
    "PAY_AMT4": 1000,
    "PAY_AMT5": 1000,
    "PAY_AMT6": 1000
}
```

Example response:

```json
{
    "prediction": 0,
    "prediction_label": "No Default",
    "default_probability": 0.23
}
```

---

# 🔗 Frontend–Backend Connection

During local development, the frontend and backend run on different ports.

```text
Frontend
http://127.0.0.1:5500
        │
        │ HTTP Request
        ↓
Backend
http://127.0.0.1:8000
        │
        ↓
/predict
        │
        ↓
ML Model
```

The frontend sends the prediction request using JavaScript:

```javascript
fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
});
```

---

# 🔄 Complete Prediction Flow

The complete application works as follows:

```text
                    USER
                      │
                      ↓
                 FRONTEND
               HTML / CSS / JS
                      │
                      ↓
                  fetch()
                      │
                      ↓
                    JSON
                      │
                      ↓
              FASTAPI BACKEND
                      │
                      ↓
               Input Validation
                      │
                      ↓
                   Scaler
                      │
                      ↓
            Logistic Regression
                      │
                      ↓
                 Prediction
                      │
                      ↓
               Probability
                      │
                      ↓
                    JSON
                      │
                      ↓
                  FRONTEND
                      │
                      ↓
                Display Result
```

---

# 🔐 CORS

The frontend and backend run on different origins during local development.

Frontend:

```text
http://127.0.0.1:5500
```

Backend:

```text
http://127.0.0.1:8000
```

The backend therefore allows the frontend origin through CORS.

```python
allow_origins=[
    "http://127.0.0.1:5500"
]
```

The CORS origin is:

```text
protocol + host + port
```

Therefore:

```text
http://127.0.0.1:5500
```

is the origin.

The complete frontend page:

```text
http://127.0.0.1:5500/frontend/index.html
```

is **not** used as the CORS origin.

---

# 📦 Technologies Used

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Backend

* FastAPI
* Uvicorn
* Pydantic

## Frontend

* HTML
* CSS
* JavaScript
* Fetch API

## Development

* Jupyter Notebook
* VS Code
* Git/GitHub
* AI assistance for frontend development

---

# 🛠️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd credict_card_fault
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirement.txt
```

---

# ▶️ Run the Backend

Start the FastAPI server:

```bash
uvicorn app:app --reload --port 8000
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

The `/docs` page can be used to test the API directly.

---

# ▶️ Run the Frontend

Open the `frontend/index.html` file using a local development server such as VS Code Live Server.

For example:

```text
http://127.0.0.1:5500/frontend/index.html
```

The exact port may vary depending on the local development server.

---

# 🧪 Testing

The application can be tested in two ways.

### 1. Backend testing

Use FastAPI Swagger:

```text
http://127.0.0.1:8000/docs
```

Test:

```text
POST /predict
```

### 2. Frontend testing

Open the frontend application and enter customer information.

The frontend sends the information to the backend, and the prediction is displayed on the webpage.

---

# 🌍 Deployment

During development, the application uses localhost:

```text
Frontend:
http://127.0.0.1:5500

Backend:
http://127.0.0.1:8000
```

After deployment, these will be replaced with public URLs.

For example:

```text
Frontend:
https://your-frontend-domain.com

Backend:
https://your-api-domain.com
```

The frontend will then send requests to:

```text
https://your-api-domain.com/predict
```

The backend CORS configuration will also need to allow the deployed frontend domain.

---

# 🧠 What I Learned

Through this project, I learned how to build an ML application from model development to API integration.

### Machine Learning

* Data cleaning
* Exploratory Data Analysis
* Feature preparation
* Logistic Regression
* Model evaluation
* Model serialization
* Prediction probabilities

### ML Engineering

* Saving trained models
* Saving preprocessing objects
* Loading models into an application
* Building an inference pipeline

### Backend

* FastAPI
* REST API concepts
* API endpoints
* HTTP methods
* Pydantic validation
* JSON
* CORS
* Uvicorn

### Frontend

* HTML forms
* CSS styling
* JavaScript
* Fetch API
* Sending JSON to an API
* Receiving JSON responses
* Displaying ML predictions

### Deployment Concepts

* Localhost
* Ports
* Frontend/backend separation
* API URLs
* Production deployment architecture

---

# 🚀 Future Improvements

Possible future improvements include:

* Compare multiple ML algorithms
* Improve model performance
* Add stronger input validation
* Improve frontend design
* Add automated tests
* Add logging
* Add model monitoring
* Add authentication
* Deploy the application to the cloud
* Add CI/CD
* Use environment variables for API configuration

---

# 👩‍💻 Author

**Manyasri**

Credit Card Default Prediction — Machine Learning Application

---

## ⭐ Project Summary

This project demonstrates how a trained Machine Learning model can be transformed into a usable application.

The final architecture is:

```text
                  USER
                    │
                    ↓
                FRONTEND
                    │
                    ↓
              FASTAPI API
                    │
                    ↓
            PREPROCESSING
                    │
                    ↓
              ML MODEL
                    │
                    ↓
               PREDICTION
                    │
                    ↓
                FRONTEND
                    │
                    ↓
                  USER
```

The project combines **Machine Learning + Python + FastAPI + REST API + JSON + JavaScript + HTML + CSS** into one complete application.



