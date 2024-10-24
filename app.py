import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Wine Quality Prediction", layout="centered")

# Add a header
st.title("🍷 Wine Quality Prediction")

# Add a brief description
st.write("""
This app predicts the quality of wine based on several features. 
Please enter the values below and click on the "Predict" button.
""")

# Create input fields for the features
st.header("Input Features")

# Use columns to create a multi-column layout
col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input("Fixed Acidity (g/dm³)", format="%.2f")
    volatile_acidity = st.number_input("Volatile Acidity (g/dm³)", format="%.2f")
    citric_acid = st.number_input("Citric Acid (g/dm³)", format="%.2f")
    residual_sugar = st.number_input("Residual Sugar (g/dm³)", format="%.2f")
    chlorides = st.number_input("Chlorides (g/dm³)", format="%.2f")

with col2:
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide (mg/dm³)", format="%.2f")
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide (mg/dm³)", format="%.2f")
    density = st.number_input("Density (g/cm³)", format="%.2f")
    pH = st.number_input("pH Level", format="%.2f")
    sulphates = st.number_input("Sulphates (g/dm³)", format="%.2f")
    alcohol = st.number_input("Alcohol (% by volume)", format="%.2f")

# Add a button with custom styling
if st.button("Predict", key="predict_button"):
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
    with st.spinner("Making prediction..."):
        response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f"Predicted Wine Quality: **{prediction}**", icon="✅")
    else:
        st.error("Error: " + response.json().get('error', 'Unknown error occurred.'))

# Add a footer
st.markdown("---")
st.write("Made with ❤️ by Ambigapathi V")
