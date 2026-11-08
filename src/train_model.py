import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from data_loader import load_data


# Load dataset

x_train, x_test, y_train, y_test = load_data()


# -------------------------------
# Logistic Regression
# -------------------------------

logistic_model = LogisticRegression(
    max_iter=1000
)

logistic_model.fit(
    x_train,
    y_train
)


with open(
    "models/logistic_regression_model.pkl",
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

rf_model.fit(
    x_train,
    y_train
)


with open(
    "models/random_forest_model.pkl",
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

svm_model.fit(
    x_train,
    y_train
)


with open(
    "models/svm_model.pkl",
    "wb"
) as file:
    pickle.dump(svm_model, file)


print("SVM trained")


# Save best model

with open(
    "models/best_model.pkl",
    "wb"
) as file:
    pickle.dump(svm_model, file)


print("Best model saved")