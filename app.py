import streamlit as st
import requests

# Streamlit app title
st.title("Wine Quality Prediction")

# Input fields for the features
fixed_acidity = st.number_input("Fixed Acidity", format="%.2f")
volatile_acidity = st.number_input("Volatile Acidity", format="%.2f")
citric_acid = st.number_input("Citric Acid", format="%.2f")
residual_sugar = st.number_input("Residual Sugar", format="%.2f")
chlorides = st.number_input("Chlorides", format="%.2f")
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", format="%.2f")
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", format="%.2f")
density = st.number_input("Density", format="%.2f")
pH = st.number_input("pH", format="%.2f")
sulphates = st.number_input("Sulphates", format="%.2f")
alcohol = st.number_input("Alcohol", format="%.2f")

# Button to submit the form
if st.button("Predict"):
    # API URL
    api_url = "http://localhost:5000/api/predict"  # Change to your API URL
    # Prepare data
    data = {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol,
    }

    # Make a POST request to the API
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f"Predicted Wine Quality: {prediction}")
    else:
        st.error("Error: " + response.json().get('error', 'Unknown error occurred.'))
