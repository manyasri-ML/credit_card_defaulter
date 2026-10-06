# Credit Card Default Prediction

A Machine Learning application that predicts whether a credit card customer is likely to default based on customer and credit-related information.

The project covers the complete workflow from **data analysis and model building to API development and deployment**.

## Project Overview

Credit card default prediction is a classification problem where the goal is to predict whether a customer will default on their credit card payment.

The trained Machine Learning model is integrated with a **FastAPI backend**, allowing users to send customer information through an API and receive a prediction.

## Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
FastAPI Backend
   ↓
API Prediction
   ↓
Deployed Application
```

## Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib

### Backend & API

* FastAPI
* Uvicorn
* Pydantic

### Development & Deployment

* Git
* GitHub
* Netlify / Deployment Platform

## Machine Learning

This project uses a supervised Machine Learning classification approach.

The dataset was analyzed and prepared before training the model. The workflow includes:

* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature selection
* Data preprocessing
* Model training
* Model evaluation
* Cross-validation
* Saving the trained model

The final trained model is saved using `joblib` and loaded by the FastAPI application for making predictions on new customer data.

## Backend API

The Machine Learning model is connected to a **FastAPI backend**.

The API:

1. Receives customer information.
2. Validates the input using Pydantic.
3. Loads the trained Machine Learning model.
4. Processes the input.
5. Generates a prediction.
6. Returns the prediction as a JSON response.

Example response:

```json
{
    "prediction": 1
}
```

Where the prediction represents the model's classification of the customer's default risk.

## Application Interface

A basic web interface is used to provide inputs and display the prediction from the API.

The primary focus of this project is the **Machine Learning model, Python backend, API integration, and deployment** rather than frontend development.

## Project Structure

```text
credit-card-default-prediction/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── credit_card_default.ipynb
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── model/
│   └── model.pkl
│
├── frontend/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder and file names may vary depending on the final project structure.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd credit-card-default-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI server

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8001
```

The API will be available locally.

You can also access the FastAPI documentation at:

```text
http://127.0.0.1:8001/docs
```

## API Usage

The API accepts customer information through a POST request.

Example:

```json
{
    "limit_bal": 20000,
    "sex": 2,
    "education": 2,
    "marriage": 1,
    "age": 24
}
```

The API processes the input using the trained model and returns the predicted result.

## Deployment

The FastAPI backend is deployed so that the Machine Learning model can be accessed through an API.

The application can therefore be used as a real-world ML application instead of only running the model inside a Jupyter Notebook.

## Key Learning Outcomes

Through this project, I worked with:

* Exploratory Data Analysis
* Data preprocessing
* Supervised Machine Learning
* Classification
* Model evaluation
* Cross-validation
* Saving and loading ML models
* Building REST APIs using FastAPI
* Input validation using Pydantic
* Connecting a Machine Learning model to an API
* Testing APIs
* Git and GitHub
* Deploying an ML application

## Future Improvements

* Improve model performance through feature engineering and hyperparameter tuning.
* Add additional model comparison.
* Improve API validation and error handling.
* Develop a more advanced user interface.
* Monitor model performance after deployment.

## Author

**Manyasri**

Machine Learning / Python Project


