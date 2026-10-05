# Machine Learning Prediction Web Application

A Machine Learning web application that allows users to enter data through a web interface and receive predictions from a trained Machine Learning model.

The project integrates a **Scikit-learn Machine Learning model with a FastAPI backend and a web frontend**.

## 🚀 Project Overview

This project demonstrates how a Machine Learning model can be converted into a usable application.

Instead of making predictions only inside a Jupyter Notebook, the trained model is connected to an API. Users can enter values through the web interface, and the application returns the model's prediction.

### Application Flow

```text
User
 ↓
Frontend
 ↓
JavaScript
 ↓
FastAPI API
 ↓
Machine Learning Model
 ↓
Prediction
 ↓
Frontend displays result
```

## 🛠️ Technologies Used

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-learn
* Joblib

### Backend / API

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* HTML
* CSS
* JavaScript

### Development

* Jupyter Notebook
* VS Code

## 📁 Project Structure

```text
project/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   └── app.py
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── model/
│   └── model.pkl
│
├── notebooks/
│   └── project.ipynb
│
├── requirements.txt
└── README.md
```

## 🧠 Machine Learning Workflow

The Machine Learning part of the project follows these steps:

1. Data collection
2. Data cleaning
3. Exploratory Data Analysis
4. Data preprocessing
5. Train-test split
6. Model training
7. Cross-validation
8. Model evaluation
9. Model saving
10. Prediction on new data

The trained model is saved using **Joblib** and later loaded by the FastAPI application.

## 🔌 API Integration

FastAPI is used to create an API endpoint for predictions.

The frontend sends the user's input to the API as JSON.

Example:

```json
{
    "feature1": 10,
    "feature2": 20,
    "feature3": 30
}
```

The FastAPI backend receives the input, validates it, and passes it to the trained Machine Learning model.

The

