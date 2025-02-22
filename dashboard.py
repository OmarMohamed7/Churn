import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv('churn.csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies']

# Convert categorical service columns to numeric (1 for Yes, 0 for No)
for service in services:
    df[service] = df[service].apply(lambda x: 1 if x == 'Yes' or x == 'DSL' or x == 'Fiber optic' else 0)



# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container([
    html.H1("Customer Churn Analysis Dashboard", className='text-center mb-4'),

   
     
    # Filters
    dbc.Row([
        dbc.Col([
            html.Label("Gender"),
            dcc.Dropdown(
                id='gender-select',
                options=[{'label': i, 'value': i} for i in ['All'] + list(df['gender'].unique())],
                value='All',
                clearable=False
            )
        ], width=3),

        dbc.Col([
            html.Label("Contract Type"),
            dcc.Checklist(
                id='contract-select',
                options=[{'label': i, 'value': i} for i in df['Contract'].unique()],
                value=df['Contract'].unique(),
                inline=True,
                style={'display': 'flex', 'gap': '8px'},
            )
        ], width=4),

        dbc.Col([
            html.Label("Payment Method"),
            dcc.Dropdown(
                id='payment-select',
                options=[{'label': i, 'value': i} for i in ['All'] + list(df['PaymentMethod'].unique())],
                value='All',
                clearable=False,
            )
        ], width=3),

        dbc.Col([
            html.Label("Senior Citizen"),
            dcc.RadioItems(
                id='senior-select',
                options=[{'label': 'All', 'value': 'All'}, {'label': 'Yes', 'value': 1}, {'label': 'No', 'value': 0}],
                value='All',
                inline=True,
                style={'display': 'flex', 'gap': '8px'},
            )
        ], width=2)
    ], className='mb-3'),

    # Graphs 
    dbc.Row([
        dbc.Col(dcc.Graph(id='churn-distribution'), width=4),
        dbc.Col(dcc.Graph(id='tenure-churn'), width=4),
        dbc.Col(dcc.Graph(id='contract-churn'), width=4)
    ]),
    
      dbc.Row([
        dbc.Col(dcc.Graph(id='tenure-boxplot'), width=6),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='charges-scatter'), width=6),
        dbc.Col(dcc.Graph(id='services-churn'), width=6)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id='correlation-heatmap'), width=6)
    ]),
    
], fluid=True)

# Callbacks
@app.callback(
    [Output('churn-distribution', 'figure'),
     Output('tenure-churn', 'figure'),
     Output('contract-churn', 'figure'),
     Output('charges-scatter', 'figure'),
     Output('services-churn', 'figure'),
     Output('correlation-heatmap', 'figure'),
    Output('tenure-boxplot', 'figure')],
    [Input('gender-select', 'value'),
     Input('contract-select', 'value'),
     Input('payment-select', 'value'),
     Input('senior-select', 'value')]
)
def update_graphs(gender, contracts, payment, senior):
    filtered_df = df[df['Contract'].isin(contracts)]
    if gender != 'All':
        filtered_df = filtered_df[filtered_df['gender'] == gender]
    if payment != 'All':
        filtered_df = filtered_df[filtered_df['PaymentMethod'] == payment]
    if senior != 'All':
        filtered_df = filtered_df[filtered_df['SeniorCitizen'] == senior]

    # Churn Distribution
    churn_fig = px.pie(filtered_df, names='Churn', title='Churn Distribution', hole=0.4)

    # Tenure vs Churn
    tenure_fig = px.histogram(filtered_df, x='tenure', color='Churn',
                              title='Tenure Distribution by Churn Status', barmode='group')
    
    # Contract Type vs Churn
    contract_fig = px.bar(filtered_df, x='Contract', color='Churn',
                          title='Churn by Contract Type')
    
    # Charges Scatter Plot
    charges_fig = px.scatter(filtered_df, x='MonthlyCharges', y='TotalCharges',
                             color='Churn', title='Monthly vs Total Charges')
    
    # Services Churn
    services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies']
    service_churn = filtered_df.groupby('Churn')[services].mean().reset_index()
    service_fig = px.bar(service_churn.melt(id_vars='Churn'), 
                         x='variable', y='value', color='Churn',
                         title='Service Usage by Churn Status', barmode='group')
    
    # Correlation Heatmap
    numeric_df = filtered_df.select_dtypes(include=['number'])
    corr_matrix = numeric_df[['tenure', 'MonthlyCharges', 'TotalCharges']].corr()
    heatmap_fig = px.imshow(corr_matrix, text_auto=True, aspect='auto',
                            title='Feature Correlation Heatmap', color_continuous_scale='Viridis')
    
    # Tenure Boxplot
    tenure_box_fig = px.box(filtered_df, y='tenure', color='Churn', 
                            title='Tenure Box Plot by Churn Status')
    
    return churn_fig, tenure_fig, contract_fig, charges_fig, service_fig, heatmap_fig,tenure_box_fig

if __name__ == '__main__':
    app.run_server(debug=True)