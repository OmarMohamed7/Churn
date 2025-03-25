import streamlit as st
import pandas as pd
import joblib  
from ui import get_user_input  # Import UI function

# Load models
encoder_model = joblib.load("encoder.pkl")  
scaler_model = joblib.load("scaler.pkl")  
prediction_model = joblib.load("best_model.pkl")  

def make_prediction(input_data):
    """
    Predicts customer churn based on input customer data.
    """
    input_df = pd.DataFrame([input_data])

    cat_columns = input_df.select_dtypes(include=['object']).columns
    encoded_features = encoder_model.transform(input_df[cat_columns])

    encoded_df = pd.DataFrame(
        encoded_features, 
        columns=encoder_model.get_feature_names_out(cat_columns), 
        index=input_df.index
    )

    df_encoded = input_df.drop(columns=cat_columns).join(encoded_df)

    numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df_encoded[numerical_cols] = scaler_model.transform(df_encoded[numerical_cols])

    prediction = prediction_model.predict(df_encoded)[0]
    probability = prediction_model.predict_proba(df_encoded)[0,1]

    return f"Churn with probability {probability:.2f}" if prediction == 1 else f"No Churn with probability {probability:.2f}"

# Streamlit App
input_data = get_user_input()  # Get input from UI

if st.button("🔍 Predict Churn"):
    result = make_prediction(input_data)
    st.success(result)
