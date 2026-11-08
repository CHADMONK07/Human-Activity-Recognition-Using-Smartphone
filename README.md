# Human Activity Recognition Using Smartphone Sensors

# Human Activity Recognition Using Smartphone Sensors

## Project Overview

This project uses machine learning algorithms to classify human activities using smartphone sensor data.

The goal is to recognize activities such as walking, sitting, standing, and laying using smartphone accelerometer and gyroscope measurements.

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