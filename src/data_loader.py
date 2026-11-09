import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "UCI HAR Dataset"
)
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        "Dataset not found.\n"
        "Please run:\n"
        "python src/download_data.py"
    )

def load_data():

    features = pd.read_csv(
        os.path.join(DATA_PATH, "features.txt"),
        sep=r"\s+",
        header=None
    )

    feature_names = features.iloc[:, 1].values

    feature_names = pd.Series(feature_names).apply(
        lambda x: x.replace("(", "_")
                  .replace(")", "_")
                  .replace("-", "_")
    )

    feature_names = (
        feature_names
        + "_"
        + feature_names.groupby(feature_names).cumcount().astype(str)
    )

    feature_names = feature_names.values


    x_train = pd.read_csv(
        os.path.join(DATA_PATH, "train", "X_train.txt"),
        sep=r"\s+",
        header=None,
        names=feature_names
    )


    x_test = pd.read_csv(
        os.path.join(DATA_PATH, "test", "X_test.txt"),
        sep=r"\s+",
        header=None,
        names=feature_names
    )


    y_train = pd.read_csv(
       os.path.join(DATA_PATH, "train", "y_train.txt"),
        sep=r"\s+",
        header=None,
        names=["activity"]
    )


    y_test = pd.read_csv(
       os.path.join(DATA_PATH, "test", "y_test.txt"),
        sep=r"\s+",
        header=None,
        names=["activity"]
    )


    y_train = y_train["activity"]
    y_test = y_test["activity"]


    return x_train, x_test, y_train, y_test