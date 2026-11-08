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


## Dataset

Dataset:
UCI Human Activity Recognition Using Smartphones Dataset

Classes:

- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

---

## Machine Learning Models

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