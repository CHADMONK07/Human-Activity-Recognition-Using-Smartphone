import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from data_loader import load_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(BASE_DIR, "models")

OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUTS_DIR, exist_ok=True)



# Load data

x_train, x_test, y_train, y_test = load_data()


# Load models

models = {

    "Logistic Regression":
        os.path.join(MODELS_DIR, "logistic_regression_model.pkl"),

    "Random Forest":
        os.path.join(MODELS_DIR, "random_forest_model.pkl"),

    "SVM":
        os.path.join(MODELS_DIR, "svm_model.pkl")
}

for model_name, path in models.items():
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"{model_name} not found. Run train_model.py first."
        )
results = []


for model_name, path in models.items():

    with open(path, "rb") as file:
        model = pickle.load(file)


    predictions = model.predict(x_test)


    accuracy = accuracy_score(
        y_test,
        predictions
    )


    results.append(
        {
            "Model": model_name,
            "Accuracy": accuracy
        }
    )


    print("\n", model_name)

    print(
        classification_report(
            y_test,
            predictions
        )
    )


    cm = confusion_matrix(
        y_test,
        predictions
    )


    plt.figure(figsize=(8,6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title(
        f"{model_name} Confusion Matrix"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig(
    os.path.join(
        OUTPUTS_DIR,
        f"{model_name.replace(' ','_')}_confusion_matrix.png"
    )
)

    plt.close()



# Save comparison

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="Accuracy",
    ascending=False
)


print(results_df)


results_df.to_csv(
    os.path.join(
        OUTPUTS_DIR,
        "model_comparison.csv"
    ),
    index=False
)