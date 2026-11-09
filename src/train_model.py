import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from data_loader import load_data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODELS_DIR, exist_ok=True)
# Load dataset

x_train, x_test, y_train, y_test = load_data()


# -------------------------------
# Logistic Regression
# -------------------------------

logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
# Train Logistic Regression model
logistic_model.fit(
    x_train,
    y_train
)


with open(
    os.path.join(MODELS_DIR, "logistic_regression_model.pkl"),
    "wb"
) as file:
    pickle.dump(logistic_model, file)


print("Logistic Regression trained")


# -------------------------------
# Random Forest
# -------------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
# Train Random Forest model
rf_model.fit(
    x_train,
    y_train
)


with open(
    os.path.join(MODELS_DIR, "random_forest_model.pkl"),
    "wb"
) as file:
    pickle.dump(rf_model, file)


print("Random Forest trained")


# -------------------------------
# SVM
# -------------------------------

svm_model = SVC(
    kernel="linear"
)
# Train SVM model
svm_model.fit(
    x_train,
    y_train
)


with open(
    os.path.join(MODELS_DIR, "svm_model.pkl"),
    "wb"
) as file:
    pickle.dump(svm_model, file)


print("SVM trained")


# Save best model

with open(
    os.path.join(MODELS_DIR, "best_model.pkl"),
    "wb"
) as file:
    pickle.dump(svm_model, file)

print("Best model saved")