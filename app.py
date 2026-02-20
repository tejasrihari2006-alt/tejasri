import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open("tejaa.pkl","rb"))

st.title("🎓 Student GPA Prediction")

study = st.number_input("Study Hours")
sleep = st.number_input("Sleep Hours")
attendance = st.number_input("Attendance %")
social = st.number_input("Social Media Hours")

if st.button("Predict GPA"):
    data = np.array([[study, sleep, attendance, social]])
    prediction = model.predict(data)
    st.success(f"Predicted GPA: {prediction[0]:.2f}")