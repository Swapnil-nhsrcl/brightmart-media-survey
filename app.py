import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('model.sav')

st.set_page_config(page_title="Advertising Sales Predictor", layout="centered")

st.title("📈 Advertising Sales Prediction App")
st.write("Enter the budget for each advertising channel to predict the expected Sales.")

# Inputs for TV, Radio, and Newspaper
TV = st.number_input("TV Budget ($)", min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
Radio = st.number_input("Radio Budget ($)", min_value=0.0, max_value=1000.0, value=20.0, step=1.0)
Newspaper = st.number_input("Newspaper Budget ($)", min_value=0.0, max_value=1000.0, value=10.0, step=1.0)

# When the user clicks the button, make the prediction
if st.button("Predict Sales"):
    features = np.array([[TV, Radio, Newspaper]])
    prediction = model.predict(features)[0]
    st.success(f"🎯 Predicted Sales: {prediction:.2f} units")
