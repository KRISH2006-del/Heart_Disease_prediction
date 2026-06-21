# ❤️ Heart Disease Prediction System

A Machine Learning-powered web application built using Streamlit that predicts the likelihood of heart disease based on patient health parameters. The system leverages a trained Logistic Regression model to provide instant risk assessment and probability scores, helping users understand potential cardiovascular risks through an intuitive interface.

---

## 📌 Project Overview

Heart disease remains one of the leading causes of mortality worldwide. Early identification of risk factors can significantly improve preventive care and treatment outcomes.

This application enables users to enter key medical attributes and receive a prediction indicating whether heart disease is likely to be present. The model has been trained on a real-world clinical dataset containing patient health records and cardiovascular indicators.

---

## 🎯 Key Features

### 🔍 Intelligent Risk Prediction

* Predicts the likelihood of heart disease in real-time.
* Provides probability-based risk assessment.
* Generates clear and easy-to-understand results.

### 📊 Interactive User Interface

* User-friendly Streamlit dashboard.
* Dynamic input forms for medical parameters.
* Instant prediction with a single click.

### 📋 Comprehensive Patient Summary

* Displays all entered health metrics in tabular format.
* Helps users review their inputs before diagnosis.

### ⚡ Fast & Lightweight

* Logistic Regression model ensures quick predictions.
* Minimal computational requirements.

---

## 📈 Model Performance

| Metric            | Score                 |
| ----------------- | --------------------- |
| Training Accuracy | 85.12%                |
| Testing Accuracy  | 81.97%                |
| Algorithm         | Logistic Regression   |
| Dataset Size      | 303 Patient Records   |
| Features Used     | 13 Medical Attributes |

The model was trained using Scikit-learn's Logistic Regression algorithm and evaluated on unseen test data to ensure reliable performance.

---

## 🩺 Input Parameters

The prediction is based on the following medical features:

| Feature                 | Description                              |
| ----------------------- | ---------------------------------------- |
| Age                     | Patient age (29–77 years)                |
| Sex                     | Male / Female                            |
| Chest Pain Type         | Type of chest pain experienced           |
| Resting Blood Pressure  | Blood pressure in mmHg                   |
| Serum Cholesterol       | Cholesterol level in mg/dl               |
| Fasting Blood Sugar     | Above 120 mg/dl (Yes/No)                 |
| Resting ECG             | Electrocardiographic results             |
| Maximum Heart Rate      | Highest heart rate achieved              |
| Exercise-Induced Angina | Presence of exercise-related chest pain  |
| ST Depression           | Depression induced by exercise           |
| ST Segment Slope        | Slope of peak exercise ST segment        |
| Major Vessels           | Number of vessels colored by fluoroscopy |
| Thalassemia (Thal)      | Blood disorder indicator                 |

---

## 🎯 Prediction Output

After entering the patient details, the application provides:

✅ Heart Disease Detected / No Heart Disease

✅ Probability Score (%)

✅ Risk Assessment Summary

✅ Complete Patient Data Overview

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Machine Learning

* Scikit-learn
* Logistic Regression

### Data Processing

* Pandas
* NumPy

### Development Environment

* Python 3.8+

---

## 📂 Project Structure

```text
Heart_Disease_prediction/
│
├── app.py                          # Streamlit web application
├── model.pkl                       # Trained Logistic Regression model
├── train_model.py                  # Model training script
├── Heart_Disease_prediction.ipynb  # Data analysis and experimentation
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Heart_Disease_prediction.git
cd Heart_Disease_prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## ☁️ Deployment on Streamlit Cloud

### Step 1: Push Project to GitHub

Ensure the repository contains:

* app.py
* model.pkl
* requirements.txt
* README.md

### Step 2: Deploy

1. Sign in to Streamlit Cloud.
2. Click **New App**.
3. Select your GitHub repository.
4. Choose the branch (`main`).
5. Set the entry point to `app.py`.
6. Click **Deploy**.

Your application will be deployed at:

```text
https://heartdiseaseprediction-addwgei27ju4z2wchp7epu.streamlit.app
```

---

## 🔬 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Model Serialization using Pickle
8. Streamlit Deployment

---

## ⚠️ Disclaimer

This application is intended solely for educational, research, and demonstration purposes.

The predictions generated by this model should not be considered a medical diagnosis, treatment recommendation, or substitute for professional healthcare advice.

Always consult a qualified healthcare professional for medical evaluation and decision-making.

---

## 👨‍💻 Author

**V. Krishna Koundinya**

B.Tech – Computer Science & Engineering (Data Science)
Anurag University, Hyderabad



---



