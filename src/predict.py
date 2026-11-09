import pickle
import numpy as np
import pandas as pd
import os
from data_loader import load_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_model.pkl"
)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Trained model not found. Run train_model.py first."
    )
# Load trained model

with open(
    MODEL_PATH,
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

    # Get training data structure

    x_train, x_test, y_train, y_test = load_data()


    # Use same column names as training

    input_data = pd.DataFrame(
        [sensor_data],
        columns=x_train.columns
    )


    prediction = model.predict(
        input_data
    )


    return activity_labels[prediction[0]]



if __name__ == "__main__":


    # Dummy 561 feature input
# Demo input: replace with real smartphone sensor features
    sample = np.zeros(561)


    result = predict_activity(sample)


    print(
        "Predicted Activity:",
        result
    )