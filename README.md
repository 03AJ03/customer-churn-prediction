# Customer Churn Prediction using Machine Learning

## Project Overview

Customer churn prediction is an important problem for banks and financial institutions.
This project uses machine learning techniques to predict whether a customer is likely to leave the bank based on their profile and activity.

The goal is to help organizations identify customers who are at risk of leaving so they can take proactive retention actions.

---

## Dataset

The dataset used in this project is the **Bank Customer Churn Dataset**.

It includes information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Ownership
* Active Member Status
* Estimated Salary

Target Variable:

* **Exited** (1 = Customer left, 0 = Customer stayed)

---

## Project Structure

```
customer-churn-prediction
│
├── app
│   └── streamlit_app.py        # Streamlit web interface
│
├── data
│   └── Churn_Modelling.csv     # Dataset
│
├── models
│   └── churn_model.pkl         # Trained model
│
├── notebooks
│   └── EDA.ipynb               # Exploratory Data Analysis
│
├── src
│   ├── preprocess.py           # Data preprocessing
│   ├── train.py                # Model training script
│   └── predict.py              # Prediction utilities
│
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## Machine Learning Model

The model used in this project is:

**Random Forest Classifier**

Why Random Forest:

* Handles tabular data well
* Works with non-linear relationships
* Provides good accuracy for classification problems

---

## How to Run the Project

### 1 Install dependencies

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

### 2 Train the model

```
python src/train.py
```

This will train the machine learning model and save it in the **models** folder.

---

### 3 Run the web application

```
streamlit run app/streamlit_app.py
```

A browser window will open where you can input customer details and predict churn.

---

## Features

* Data preprocessing pipeline
* Exploratory Data Analysis
* Machine learning model training
* Model persistence using pickle
* Interactive Streamlit web application

---
