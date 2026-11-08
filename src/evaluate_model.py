import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from data_loader import load_data


# Load data

x_train, x_test, y_train, y_test = load_data()


# Load models

models = {

    "Logistic Regression":
        "models/logistic_regression_model.pkl",

    "Random Forest":
        "models/random_forest_model.pkl",

    "SVM":
        "models/svm_model.pkl"
}


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
        fmt="d"
    )

    plt.title(
        f"{model_name} Confusion Matrix"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig(
        f"outputs/{model_name.replace(' ','_')}_confusion_matrix.png"
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
    "outputs/model_comparison.csv",
    index=False
)