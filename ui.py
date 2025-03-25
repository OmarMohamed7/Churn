import streamlit as st

def get_user_input():
    """
    Creates the Streamlit UI layout and returns user inputs as a dictionary.
    """
    st.title("📊 Customer Churn Prediction")
    st.write("Fill in customer details to predict churn.")

    # Layout: First row
    col1, col2, col3, col4 = st.columns(4)
    gender = col1.radio("Gender", ["Male", "Female"])
    SeniorCitizen = col2.radio("Senior Citizen", [0, 1])
    Partner = col3.radio("Partner", ["Yes", "No"])
    Dependents = col4.radio("Dependents", ["Yes", "No"])

    # Layout: Second row
    col1, col2, col3, col4 = st.columns(4)
    tenure = col1.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
    PhoneService = col2.radio("Phone Service", ["Yes", "No"])
    MultipleLines = col3.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    InternetService = col4.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    # Layout: Third row
    col1, col2, col3, col4 = st.columns(4)
    OnlineSecurity = col1.radio("Online Security", ["Yes", "No"])
    OnlineBackup = col2.radio("Online Backup", ["Yes", "No"])
    DeviceProtection = col3.radio("Device Protection", ["Yes", "No"])
    TechSupport = col4.radio("Tech Support", ["Yes", "No"])

    # Layout: Fourth row
    col1, col2, col3, col4 = st.columns(4)
    StreamingTV = col1.radio("Streaming TV", ["Yes", "No"])
    StreamingMovies = col2.radio("Streaming Movies", ["Yes", "No"])
    Contract = col3.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = col4.radio("Paperless Billing", ["Yes", "No"])

    # Layout: Fifth row
    col1, col2, col3 = st.columns(3)
    PaymentMethod = col1.selectbox(
        "Payment Method", 
        ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
    )
    MonthlyCharges = col2.number_input("Monthly Charges", min_value=0.0, value=29.85)
    TotalCharges = col3.number_input("Total Charges", min_value=0.0, value=29.85)

    # Collect inputs in a dictionary
    input_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    return input_data
