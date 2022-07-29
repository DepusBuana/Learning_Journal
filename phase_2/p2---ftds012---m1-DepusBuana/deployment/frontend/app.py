import streamlit as st
import pandas as pd
import pickle
import requests
import json

st.title('Customer Churn Predictions')


with open ('preprop.pkl', 'rb') as f:
    preprocess = pickle.load(f)


MonthlyCharges = st.number_input('MonthlyCharges', min_value=0)
TotalCharges = st.number_input('TotalCharges', min_value=0)
Tenure = st.number_input('Tenure', min_value=1)
SeniorCitizen = st.radio('Senior citizen status (1 = Yes, 2 = No)', [1, 0])
Partner = st.radio('Partner status', ['No', 'Yes'])
Dependents = st.radio('Dependents status', ['No', 'Yes'])
InternetService = st.radio('InternetService (Yes = available)', ['No', 'DSL', 'Fiber optic'])
OnlineSecurity = st.radio('OnlineSecurity (Yes = available)', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.radio('OnlineBackup (Yes = available)', ['No', 'Yes', 'No internet service'])
DeviceProtection = st.radio('DeviceProtection (Yes = available)', ['No', 'Yes', 'No internet service'])
TechSupport = st.radio('TechSupport (Yes = available)', ['No', 'Yes', 'No internet service'])
StreamingTV = st.radio('StreamingTV (Yes = available)', ['No', 'Yes'])
StreamingMovies = st.radio('StreamingMovies (Yes = available)', ['No', 'Yes', 'No internet service'])
Contract = st.radio('Contract status', ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.radio('PaperlessBilling (Yes = available)', ['Yes', 'No'])
PaymentMethod = st.radio('PaymentMethod',['Electronic check','Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

data = [
        MonthlyCharges,
        TotalCharges,
        Partner,
        Dependents,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        Tenure,
        SeniorCitizen
    ]

col5, col6, col7 = st.columns([1.75, 1, 1])
with col6:
    predict = st.button("Predict")

columns = ['MonthlyCharges', 'TotalCharges', 'Partner', 'Dependents', 'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport','StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod','tenure', 'SeniorCitizen']

new_data = pd.DataFrame([data], columns = columns)
new_data_enc = preprocess.transform(new_data)
new_data_list = new_data_enc.tolist()

input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':new_data_list
})

if predict:
        URL = "http://tf-p2m1-gusti-ayu-be.herokuapp.com/v1/models/churn_rate:predict"
        r = requests.post(URL, data=input_data_json)
        result = r.json()
        if result['predictions'][0][0] > 0.5:
            result_style2 = '<h1 style="font-family:cursive; color:#f54242; text-align:center;"> Churn Customer </h1>'
            st.markdown(result_style2,unsafe_allow_html=True)
        else:
            result_style2 = '<h1 style="font-family:cursive; color:#1c9c29; text-align:center;"> Retained Customer </h1>'
            st.markdown(result_style2,unsafe_allow_html=True)
