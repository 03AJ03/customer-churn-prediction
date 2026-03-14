import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("models/churn_model.pkl","rb"))

st.title("Customer Churn Prediction")

st.write("Enter customer details")

credit_score = st.slider("Credit Score", 300, 900)
age = st.slider("Age", 18, 100)
tenure = st.slider("Tenure", 0, 10)
balance = st.number_input("Balance")

num_products = st.slider("Number of Products",1,4)
has_card = st.selectbox("Has Credit Card", ["Yes","No"])
active_member = st.selectbox("Is Active Member", ["Yes","No"])
has_card = 1 if has_card == "Yes" else 0
active_member = 1 if active_member == "Yes" else 0
salary = st.number_input("Estimated Salary")

Country = st.selectbox("Country",["France","Germany","Spain"])
gender = st.selectbox("Gender",["Female","Male"])

geo_germany = 1 if Country == "Germany" else 0
geo_spain = 1 if Country == "Spain" else 0
gender_male = 1 if gender == "Male" else 0

if st.button("Predict"):

    features = np.array([[

        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        active_member,
        salary,
        geo_germany,
        geo_spain,
        gender_male

    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")