import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the trained model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Set page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("❤️ Heart Disease Prediction System")
st.markdown("""
This application uses a machine learning model to predict the likelihood of heart disease
based on medical parameters. The model was trained on 303 patient records with 85% training accuracy.
""")

# Sidebar for information
with st.sidebar:
    st.header("📊 Model Information")
    st.info("""
    **Model Type:** Logistic Regression  
    **Training Accuracy:** 85.12%  
    **Testing Accuracy:** 81.97%  
    **Dataset:** 303 patients
    """)

# Create columns for input
col1, col2 = st.columns(2)

# Feature inputs
with col1:
    st.subheader("Patient Vitals")
    age = st.slider("Age", 29, 77, 50)
    sex = st.selectbox("Sex", ["Male (1)", "Female (0)"])
    sex_val = 1 if "Male" in sex else 0
    
    cp = st.slider("Chest Pain Type (0-3)", 0, 3, 1)
    trestbps = st.slider("Resting Blood Pressure (mmHg)", 90, 210, 130)
    chol = st.slider("Serum Cholesterol (mg/dl)", 120, 570, 240)

with col2:
    st.subheader("Additional Indicators")
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No (0)", "Yes (1)"])
    fbs_val = 1 if "Yes" in fbs else 0
    
    restecg = st.slider("Resting ECG (0-2)", 0, 2, 1)
    thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
    exang = st.selectbox("Exercise Induced Angina", ["No (0)", "Yes (1)"])
    exang_val = 1 if "Yes" in exang else 0

# Additional features
col3, col4 = st.columns(2)

with col3:
    oldpeak = st.slider("ST Depression (0-6.2)", 0.0, 6.2, 1.0)
    slope = st.slider("Slope of ST Segment (0-2)", 0, 2, 1)

with col4:
    ca = st.slider("Number of Major Vessels (0-4)", 0, 4, 0)
    thal = st.slider("Thal (0-3)", 0, 3, 2)

# Make prediction
if st.button("🔍 Predict", key="predict_btn", use_container_width=True):
    # Prepare input data
    input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs_val, restecg, 
                            thalach, exang_val, oldpeak, slope, ca, thal]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]
    
    # Display results
    st.divider()
    
    if prediction == 1:
        st.error(f"⚠️ **Prediction: Heart Disease Detected**", icon="❌")
        risk_level = "High Risk"
        color = "red"
    else:
        st.success(f"✅ **Prediction: No Heart Disease**", icon="✓")
        risk_level = "Low Risk"
        color = "green"
    
    # Show probability
    col_prob1, col_prob2 = st.columns(2)
    with col_prob1:
        st.metric("Probability of Disease", f"{prediction_proba[1]:.2%}")
    with col_prob2:
        st.metric("Probability of Healthy", f"{prediction_proba[0]:.2%}")
    
    # Display patient summary
    st.subheader("Patient Summary")
    summary_df = pd.DataFrame({
        'Parameter': ['Age', 'Sex', 'Chest Pain Type', 'Resting BP', 'Cholesterol',
                     'Fasting BS', 'Resting ECG', 'Max HR', 'Exercise Angina',
                     'ST Depression', 'ST Slope', 'Major Vessels', 'Thal'],
        'Value': [age, "Male" if sex_val==1 else "Female", cp, trestbps, chol,
                 "Yes" if fbs_val==1 else "No", restecg, thalach,
                 "Yes" if exang_val==1 else "No", f"{oldpeak:.1f}", slope, ca, thal]
    })
    st.dataframe(summary_df, use_container_width=True)

# Footer
st.divider()
st.caption("⚠️ **Disclaimer:** This tool is for educational purposes only and should not be used as a substitute for professional medical advice.")
