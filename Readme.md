# Customer Churn Analysis Dashboard

## Link [Churn Web App](https://churnn.streamlit.app/)

## Overview

A Streamlit-based application designed to predict customer churn using machine learning. Users can input customer data (e.g., demographics, usage patterns, or transaction history), and the app leverages a trained predictive model to determine the likelihood of churn. The interface likely includes visualizations, such as feature importance plots or churn rate trends, to provide actionable insights for retaining customers. This tool is ideal for businesses looking to proactively identify at-risk customers and implement targeted retention strategies.

# Features

    1. Filters
    
    The dashboard includes multiple filters

        - Gender: filtering by male, female, or all.

        - Contract Type: (Month-to-Month, One Year, Two Year).

        - Payment Method: Filters customers based on their payment method.

        - Senior Citizen: senior and non-senior customers.

    2. Graphs & Insights

        1. Churn Distribution

            Graph Type: Pie Chart

            Description: 
                Poportion of customers who have churned vs. those who have stayed.

        2. Tenure vs Churn

            Graph Type: Histogram

            Description: displays how long customers have been with the company (tenure) and categorizes them by whether they have churned or remained.

            Insights: It helps identify patterns in customer retention over time.
            
            If churn is high for customers with shorter tenure, it may indicate dissatisfaction with the onboarding experience.

            If churn increases after a specific period (e.g., 12 or 24 months), it could be linked to contract expirations.

            Longer-tenured customers who churn may suggest evolving needs or pricing concerns.

        3. Churn Box plot

            Graph Type: Box plot Chart

            Description: Illustrates the churn distribution.

        4. Contract Type vs Churn

            Graph Type: Bar Chart

            Description: Illustrates the churn rate across different contract types.

        5. Monthly Charges vs Total Charges

            Graph Type: Scatter Plot

            Description: Plots monthly charges against total charges with churn status.

            Insights: Helps determine whether customers with higher monthly charges are more likely to churn.

        6. Service Usage by Churn Status

            Graph Type: Grouped Bar Chart

            Description: Compares the usage of various services (Online Security, Backup, Device Protection, etc.) between churned and retained customers.

        7. Feature Correlation Heatmap

            Graph Type: Heatmap

            Description: Displays correlations between numerical features in the dataset.

            Insights: Helps in understanding which factors strongly influence customer churn.
