# Human Activity Recognition Using Smartphone Sensors
# Human Activity Recognition Using Smartphone Sensors

<p align="center">

A Machine Learning based system that recognizes human activities using smartphone sensor data.

</p>

---

## 🚀 Project Overview

Human Activity Recognition (HAR) is a machine learning problem where the objective is to identify human activities based on sensor data collected from smartphones.

In this project, we use accelerometer and gyroscope measurements from smartphones to classify six different human activities:

- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

Multiple machine learning algorithms are trained and evaluated to build an accurate activity recognition system.

---
## 📌 Problem Statement

With the rapid growth of wearable devices and smartphone-based applications, automatically understanding human activities has become an important task in healthcare, fitness monitoring, smart environments, and safety systems.

Smartphones contain built-in sensors such as accelerometers and gyroscopes that continuously capture human movement patterns. However, converting this raw sensor data into meaningful activity information requires efficient data processing and machine learning techniques.

The objective of this project is to develop a machine learning model capable of accurately recognizing human physical activities from smartphone sensor measurements.

---
## 🎯 Objectives

The main objectives of this project are:

- To analyze smartphone sensor data collected during different human activities.
- To preprocess and prepare sensor data for machine learning applications.
- To train multiple classification models and compare their performance.
- To evaluate models using accuracy, classification reports, and confusion matrices.
- To develop a prediction pipeline capable of identifying human activities from sensor inputs.
- To select the best-performing model for activity recognition.

---


## 📂 Dataset Description

This project uses the **UCI Human Activity Recognition Using Smartphones Dataset**.

The dataset was created from experiments carried out using smartphone sensors to record human movement patterns. Data was collected from participants performing different daily activities while carrying a smartphone equipped with an accelerometer and gyroscope.

### Dataset Information

| Attribute | Description |
|-----------|-------------|
| Dataset Name | Human Activity Recognition Using Smartphones Dataset |
| Source | UCI Machine Learning Repository |
| Data Type | Smartphone sensor measurements |
| Sensors Used | Accelerometer and Gyroscope |
| Number of Features | 561 |
| Number of Activities | 6 |
| Learning Task | Multi-class Classification |

---

## 🏃 Activity Classes

The model classifies the following six activities:

| Class | Activity |
|------|----------|
| 1 | Walking |
| 2 | Walking Upstairs |
| 3 | Walking Downstairs |
| 4 | Sitting |
| 5 | Standing |
| 6 | Laying |

---

## 📊 Dataset Features

The dataset contains **561 numerical features** extracted from smartphone sensor signals.

These features include:

- Time-domain measurements
- Frequency-domain measurements
- Accelerometer features
- Gyroscope features
- Body and gravity motion components

Examples of extracted features:

- Mean acceleration values
- Standard deviation of movement
- Signal magnitude information
- Frequency-based sensor characteristics

These engineered features help machine learning algorithms identify unique patterns associated with different human activities.

---
## 🔄 Project Workflow

The complete workflow of the Human Activity Recognition system is shown below:

---

## 🏗️ Machine Learning Pipeline

### 1. Data Loading
- Sensor data is loaded from the UCI HAR dataset.
- Training and testing datasets are separated.

### 2. Data Preprocessing
- Feature names are assigned.
- Data is prepared in a format suitable for machine learning algorithms.

### 3. Model Training
Three classification algorithms are trained:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

### 4. Model Evaluation
Models are evaluated using:

- Accuracy score
- Classification report
- Confusion matrix

### 5. Prediction
The best-performing model is used to predict human activities from new sensor input.

---
## 📁 Repository Structure

The project is organized as follows:


### Folder Description

| Folder/File | Purpose |
|------------|---------|
| `data/` | Contains dataset files |
| `models/` | Stores trained machine learning models |
| `notebooks/` | Contains exploratory data analysis notebooks |
| `outputs/` | Stores evaluation results and visualizations |
| `src/` | Contains project source code |
| `requirements.txt` | Lists required Python libraries |
| `README.md` | Project documentation |

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn

### Data Visualization

- Matplotlib
- Seaborn

### Development Tools

- Jupyter Notebook
- VS Code
- Git & GitHub

---
## ⚙️ Installation & Setup

Follow the steps below to run this project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/CHADMONK07/Human-Activity-Recognition-Using-Smartphone.git

pip install -r requirements.txt

## 🧹 Data Preprocessing

Before training the machine learning models, the raw dataset is prepared through a structured preprocessing pipeline.

### Preprocessing Steps

### 1. Data Loading

- The UCI Human Activity Recognition dataset is loaded.
- Training and testing datasets are separated.

### 2. Feature Extraction

- The dataset contains 561 engineered features extracted from smartphone sensor signals.
- These features represent movement patterns captured by accelerometers and gyroscopes.

### 3. Feature Organization

- Feature names are assigned to the dataset.
- Data is converted into a structured format suitable for machine learning algorithms.

### 4. Model Ready Dataset

- The processed data is used as input for classification models.
- Training data is used for learning patterns.
- Testing data is used for evaluating model performance.

---

#MACHINE LEARNING MODELS
The following models were trained:

1. Logistic Regression
2. Random Forest
3. Support Vector Machine (SVM)

---

## Results

| Model | Accuracy |
|------|----------|
| SVM | 96.40% |
| Logistic Regression | 96.06% |
| Random Forest | 92.57% |

Best Model:

Support Vector Machine

---

## Project Structure
data/
models/
notebooks/
outputs/
src/

---

## Installation

Install dependencies:
pip install -r requirements.txt


---

## Running the Project

Train models:
python src/train_model.py


Evaluate models:
python src/evaluate_model.py


Predict activity:
python src/predict.py


---

## Contributors

- AMAAN - Data preprocessing and EDA
- JAI - Model training
- ATULYA - Model evaluation
- THANISH - Prediction pipeline and documentation