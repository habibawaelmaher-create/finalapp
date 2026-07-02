import joblib
import pandas as pd
import streamlit as st

model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('diabetes_scaler.pkl')

st.title("🩺 Diabetes Prediction")

glucose = st.number_input("Glucose", value=120.0)
bmi = st.number_input("BMI", value=32.0)
pregnancies = st.number_input("Pregnancies", value=2)
dpf = st.number_input("Diabetes Pedigree Function", value=0.47)
age = st.number_input("Age", value=33)

if st.button("Predict"):
    data = pd.DataFrame([[glucose, bmi, pregnancies, dpf, age]],
                        columns=['Glucose', 'BMI', 'Pregnancies', 'DiabetesPedigreeFunction', 'Age'])
    
    pred = model.predict(scaler.transform(data))[0]
 
    if pred == 1:
        st.error("⚠️ Diabetes predicted")
    else:
        st.success("✅ No Diabetes predicted")