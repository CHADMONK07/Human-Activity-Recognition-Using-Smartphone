import os
import zipfile
import urllib.request


# UCI HAR Dataset URL
DATASET_URL = (
    "https://archive.ics.uci.edu/static/public/240/"
    "human+activity+recognition+using+smartphones.zip"
)


# Project root directory
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# Dataset paths
RAW_DATA_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)

DOWNLOAD_ZIP = os.path.join(
    RAW_DATA_PATH,
    "dataset.zip"
)


# -------------------------------
# Download progress function
# -------------------------------

def show_progress(block_num, block_size, total_size):

    downloaded = block_num * block_size

    percentage = downloaded * 100 / total_size

    print(
        f"\rDownloading: {percentage:.2f}%",
        end=""
    )


# -------------------------------
# Download Dataset
# -------------------------------

def download_dataset():

    os.makedirs(
        RAW_DATA_PATH,
        exist_ok=True
    )

    dataset_folder = os.path.join(
        RAW_DATA_PATH,
        "UCI HAR Dataset"
    )

    if os.path.exists(dataset_folder):

        print("Dataset already exists.")

        return False


    print("Downloading UCI HAR Dataset...")


    try:

        urllib.request.urlretrieve(
            DATASET_URL,
            DOWNLOAD_ZIP,
            show_progress
        )


        print(
            "\nDownload completed."
        )

        return True


    except Exception as error:

        print(
            "Download failed:"
        )

        print(error)

        return False



# -------------------------------
# Extract Dataset
# -------------------------------

def extract_dataset():

    print(
        "Extracting dataset..."
    )


    try:

        # Extract outer zip

        with zipfile.ZipFile(
            DOWNLOAD_ZIP,
            "r"
        ) as zip_file:

            zip_file.extractall(
                RAW_DATA_PATH
            )


        print(
            "Outer zip extracted."
        )


        # Check inner zip

        inner_zip = os.path.join(
            RAW_DATA_PATH,
            "UCI HAR Dataset.zip"
        )


        if os.path.exists(inner_zip):

            print(
                "Inner zip found. Extracting..."
            )


            with zipfile.ZipFile(
                inner_zip,
                "r"
            ) as zip_file:

                zip_file.extractall(
                    RAW_DATA_PATH
                )


            print(
                "Inner zip extracted."
            )


        else:

            print(
                "No inner zip found."
            )


        # -------------------------------
        # Dataset verification
        # -------------------------------

        required_file = os.path.join(
            RAW_DATA_PATH,
            "UCI HAR Dataset",
            "features.txt"
        )


        if not os.path.exists(required_file):

            raise FileNotFoundError(
                "Dataset extraction incomplete. "
                "features.txt not found."
            )


        print(
            "Dataset verification successful."
        )


        print(
            "Extraction completed."
        )


        return True



    except Exception as error:

        print(
            "Extraction failed:"
        )

        print(error)

        return False



# -------------------------------
# Cleanup temporary files
# -------------------------------

def cleanup():

    files = [

        DOWNLOAD_ZIP,

        os.path.join(
            RAW_DATA_PATH,
            "UCI HAR Dataset.zip"
        )

    ]


    for file in files:

        if os.path.exists(file):

            os.remove(file)


    print(
        "Temporary files removed."
    )



# -------------------------------
# Main
# -------------------------------

def main():

    print(
        "Starting dataset setup...\n"
    )


    if download_dataset():

        if extract_dataset():

            cleanup()

            print(
                "\nDataset setup completed successfully."
            )
    else:

     print(
        "\nDataset setup skipped. Dataset already available."
    )


if __name__ == "__main__":

    main()