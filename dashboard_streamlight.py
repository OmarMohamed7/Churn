import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    # Load Data
    df = pd.read_csv('churn.csv')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(subset=['TotalCharges'], inplace=True)

    return df

# Function to display the dashboard
def show_dashboard():
    st.subheader("Dashboard")

    # Load Data
    df = load_data()

    with st.sidebar:
        st.header("🔍 Filters")
        
        # Gender Filter
        gender_filter = st.multiselect("Select Gender", options=df['gender'].unique(), default=df['gender'].unique())

        # Contract Filter
        contract_filter = st.multiselect("Select Contract Type", options=df['Contract'].unique(), default=df['Contract'].unique())

        # Churn Filter
        churn_filter = st.radio("Churn", ["All", "Yes", "No"], index=0)

    # Apply Filters
    filtered_df = df[df['gender'].isin(gender_filter) & df['Contract'].isin(contract_filter)]
    
    if churn_filter != "All":
        filtered_df = filtered_df[filtered_df['Churn'] == churn_filter]

    col1, col2, col3 = st.columns(3)

    # Churn Distribution
    fig1 = px.pie(filtered_df, names='Churn', title='Churn Distribution', hole=0.4)
    col1.plotly_chart(fig1, use_container_width=True)

    # Tenure vs Churn
    fig2 = px.histogram(filtered_df, x='tenure', color='Churn', title='Tenure Distribution', barmode='group')
    col2.plotly_chart(fig2, use_container_width=True)

    # Contract Type vs Churn
    fig3 = px.bar(filtered_df, x='Contract', color='Churn', title='Churn by Contract Type')
    col3.plotly_chart(fig3, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)

        # Charges Scatter Plot
        fig4 = px.scatter(df, x='MonthlyCharges', y='TotalCharges', color='Churn', title='Monthly vs Total Charges')
        col1.plotly_chart(fig4, use_container_width=True)

        # Correlation Heatmap
        corr_matrix = filtered_df[['tenure', 'MonthlyCharges', 'TotalCharges']].corr()
        fig5 = px.imshow(corr_matrix, text_auto=True, aspect='auto', title='Feature Correlation Heatmap')
        col2.plotly_chart(fig5, use_container_width=True)
