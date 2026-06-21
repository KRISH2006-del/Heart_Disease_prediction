# Heart Disease Prediction System

A Streamlit web application that predicts the likelihood of heart disease based on medical parameters using a trained Logistic Regression model.

## 📊 Model Performance
- **Training Accuracy:** 85.12%
- **Testing Accuracy:** 81.97%
- **Algorithm:** Logistic Regression
- **Dataset:** 303 patients with 13 medical features

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Heart_Disease_prediction.git
cd Heart_Disease_prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud

### Step 1: Prepare Your Repository
Ensure your GitHub repository contains:
- `app.py` (Streamlit app)
- `requirements.txt` (dependencies)
- `model.pkl` (trained model)
- `README.md` (this file)

### Step 2: Deploy on Streamlit Cloud
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **New app**
3. Select your GitHub repository
4. Select the branch: `main`
5. Select the path: `app.py`
6. Click **Deploy**

Your app will be live at: `https://your-app-name.streamlit.app`

## 📝 Features

### Input Parameters
- **Age:** Patient's age (29-77 years)
- **Sex:** Male or Female
- **Chest Pain Type:** 0-3 severity scale
- **Resting Blood Pressure:** mmHg
- **Serum Cholesterol:** mg/dl
- **Fasting Blood Sugar:** >120 mg/dl (Yes/No)
- **Resting ECG:** 0-2 scale
- **Max Heart Rate:** Achieved during exercise
- **Exercise Induced Angina:** Yes/No
- **ST Depression:** Induced by exercise
- **ST Segment Slope:** 0-2 scale
- **Major Vessels:** Number of major vessels colored by fluoroscopy
- **Thal:** Blood disorder indicator (0-3)

### Output
- **Prediction:** Heart Disease Detected or No Heart Disease
- **Risk Level:** Probability score
- **Patient Summary:** Tabular view of all input parameters

## 📂 File Structure
```
Heart_Disease_prediction/
├── app.py                          # Streamlit application
├── model.pkl                       # Trained model
├── train_model.py                  # Model training script
├── requirements.txt                # Python dependencies
├── Heart_Disease_prediction.ipynb  # Original notebook
└── README.md                       # This file
```

## ⚠️ Important Notes
- This tool is for **educational purposes only**
- Should **NOT** be used as a substitute for professional medical advice
- Always consult with a healthcare provider for actual diagnosis

## 🔧 Troubleshooting

### Model file not found
Ensure `model.pkl` is in the same directory as `app.py`

### Import errors
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

### App not loading
Clear Streamlit cache:
```bash
streamlit cache clear
streamlit run app.py
```

## 📊 Technologies Used
- **Streamlit:** Web framework
- **Scikit-learn:** Machine learning
- **Pandas:** Data manipulation
- **NumPy:** Numerical computing

## 👤 Author
Created with ❤️

## 📄 License
This project is open source and available under the MIT License.
