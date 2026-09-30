import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# 1. PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "01_data" / "02_processed"/"cleaned_data.csv"
MODEL_DIR = BASE_DIR / "04_models"

MODEL_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET")
print("=" * 60)

print("Dataset shape:", df.shape)
print()


# ============================================================
# 3. SEPARATE FEATURES AND TARGET
# ============================================================

# ID is only an identifier, so remove it.

X = df.drop(
    ["ID", "default.payment.next.month"],
    axis=1
)

y = df["default.payment.next.month"]


print("Features shape:", X.shape)
print("Target shape:", y.shape)

print()
print("Class distribution:")
print(y.value_counts())

print()


# ============================================================
# 4. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


print("=" * 60)
print("TRAIN / TEST SPLIT")
print("=" * 60)

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

print()


# ============================================================
# 5. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


print("=" * 60)
print("FEATURE SCALING")
print("=" * 60)

print("Scaling completed.")

print()


# ============================================================
# 6. CROSS VALIDATION
# ============================================================

print("=" * 60)
print("5-FOLD STRATIFIED CROSS-VALIDATION")
print("=" * 60)


skf = StratifiedKFold(

    n_splits=5,

    shuffle=True,

    random_state=42
)


# ------------------------------------------------------------
# Normal Logistic Regression
# ------------------------------------------------------------

normal_model = LogisticRegression(

    max_iter=1000,

    random_state=42
)


scoring = {

    "accuracy": "accuracy",

    "precision": "precision",

    "recall": "recall",

    "f1": "f1"
}


normal_cv_results = cross_validate(

    normal_model,

    X_train_scaled,

    y_train,

    cv=skf,

    scoring=scoring
)


print()
print("NORMAL LOGISTIC REGRESSION")

print(
    "CV Accuracy :",
    normal_cv_results["test_accuracy"].mean()
)

print(
    "CV Precision:",
    normal_cv_results["test_precision"].mean()
)

print(
    "CV Recall   :",
    normal_cv_results["test_recall"].mean()
)

print(
    "CV F1       :",
    normal_cv_results["test_f1"].mean()
)


# ============================================================
# 7. BALANCED LOGISTIC REGRESSION
# ============================================================

balanced_model = LogisticRegression(

    class_weight="balanced",

    max_iter=1000,

    random_state=42
)


balanced_cv_results = cross_validate(

    balanced_model,

    X_train_scaled,

    y_train,

    cv=skf,

    scoring=scoring
)


print()
print("BALANCED LOGISTIC REGRESSION")

print(
    "CV Accuracy :",
    balanced_cv_results["test_accuracy"].mean()
)

print(
    "CV Precision:",
    balanced_cv_results["test_precision"].mean()
)

print(
    "CV Recall   :",
    balanced_cv_results["test_recall"].mean()
)

print(
    "CV F1       :",
    balanced_cv_results["test_f1"].mean()
)


# ============================================================
# 8. TRAIN FINAL BALANCED MODEL
# ============================================================

print()
print("=" * 60)
print("FINAL MODEL TRAINING")
print("=" * 60)


balanced_model.fit(

    X_train_scaled,

    y_train
)


print("Final balanced Logistic Regression trained.")


# ============================================================
# 9. TEST SET PREDICTION
# ============================================================

y_pred = balanced_model.predict(

    X_test_scaled
)


# ============================================================
# 10. TEST METRICS
# ============================================================

accuracy = accuracy_score(

    y_test,

    y_pred
)


precision = precision_score(

    y_test,

    y_pred
)


recall = recall_score(

    y_test,

    y_pred
)


f1 = f1_score(

    y_test,

    y_pred
)


conf_matrix = confusion_matrix(

    y_test,

    y_pred
)


print()
print("=" * 60)
print("FINAL TEST RESULTS")
print("=" * 60)


print(
    "Accuracy :",
    accuracy
)

print(
    "Precision:",
    precision
)

print(
    "Recall   :",
    recall
)

print(
    "F1 Score :",
    f1
)


print()
print("Confusion Matrix:")

print(conf_matrix)


print()
print("Classification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ============================================================
# 11. SAVE MODEL
# ============================================================

MODEL_PATH = MODEL_DIR / "logistic_regression.pkl"

SCALER_PATH = MODEL_DIR / "scaler.pkl"


joblib.dump(

    balanced_model,

    MODEL_PATH
)


joblib.dump(

    scaler,

    SCALER_PATH
)


# ============================================================
# 12. FINAL MESSAGE
# ============================================================

print()
print("=" * 60)
print("FILES SAVED")
print("=" * 60)

print("Model:")
print(MODEL_PATH)

print()

print("Scaler:")
print(SCALER_PATH)

print()

print("Training completed successfully!")
