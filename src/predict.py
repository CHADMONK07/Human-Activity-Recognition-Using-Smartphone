import pickle
import numpy as np


# Load best model

with open(
    "models/best_model.pkl",
    "rb"
) as file:
    model = pickle.load(file)


# Activity labels

activity_labels = {
    1: "Walking",
    2: "Walking Upstairs",
    3: "Walking Downstairs",
    4: "Sitting",
    5: "Standing",
    6: "Laying"
}


def predict_activity(sensor_data):

    prediction = model.predict(
        np.array(sensor_data).reshape(1,-1)
    )

    activity = activity_labels[
        prediction[0]
    ]

    return activity



# Example prediction

if __name__ == "__main__":

    sample = np.zeros(561)

    result = predict_activity(sample)

    print(
        "Predicted Activity:",
        result
    )