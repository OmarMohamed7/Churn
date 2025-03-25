import streamlit as st
import pandas as pd
import joblib  
from ui import get_user_input
from dashboard_streamlight import show_dashboard 
import os


encoder_path = os.path.join(os.path.dirname(__file__), "encoder.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
prediction_model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")


# Load models
encoder_model = joblib.load(encoder_path)  
scaler_model = joblib.load(scaler_path)  
prediction_model = joblib.load(prediction_model_path)  

def make_prediction(input_data):
    """
    Predicts customer churn based on input customer data.
    """
    input_df = pd.DataFrame([input_data])
    
    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[numerical_cols] = scaler_model.transform(input_df[numerical_cols])

    cat_columns = input_df.select_dtypes(include=['object']).columns
    encoded_features = encoder_model.transform(input_df[cat_columns])

    encoded_df = pd.DataFrame(
        encoded_features, 
        columns=encoder_model.get_feature_names_out(cat_columns), 
        index=input_df.index
    )

    df_encoded = input_df.drop(columns=cat_columns).join(encoded_df)



    prediction = prediction_model.predict(df_encoded)[0]
    probability = prediction_model.predict_proba(df_encoded)[0,1]

    return f"Churn with probability {probability:.2f}" if prediction == 1 else f"No Churn with probability {probability:.2f}"

# Streamlit App

# Streamlit Layout
st.set_page_config(layout="wide")

# ---- FIRST ROW: DASHBOARD ----
st.title("Customer Churn Analysis & Prediction")

show_dashboard()

input_data = get_user_input()  # Get input from Preiction UI

if st.button("🔍 Predict Churn"):
    result = make_prediction(input_data)
    st.success(result)
