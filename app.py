import streamlit as st
import pandas as pd
import requests
import json

#streamlit run app.py
# Title of the app
st.title('Prediction of loan repayment')

# URL of the FastAPI API
api_url = 'http://127.0.0.1:8000/predict'

# Fonction to predict one loan demand
def predict_single(data):
    """
    Sends a POST request to the API to obtain the prediction for a single applicant.
    
    Args:
        data (dataframe): A dataframe containing the features of the applicant.
        
    Returns:
        str: The prediction returned by the API.
    """
    response = requests.post(api_url, json=json.loads(json.dumps(data)))
    if response.status_code == 200:
        return response.json()['prediction']
    else:
        st.error('Prediction error')
        return None


# User entries for applicant features
person_age = st.number_input('Age of the applicant ', min_value=20)
person_income = st.number_input('Annual income of the applicant (USD)', min_value=0.0)
person_emp_exp = st.number_input('Employment experience (years)', min_value=0.0)
loan_amnt = st.number_input('Amount of the loan (USD)', min_value=500)
loan_int_rate = st.number_input('Loan Interest rate', min_value=5)
loan_percent_income = st.number_input('Loan percent income',  min_value=0.0, max_value=1.0, step=0.01)
cb_person_cred_hist_length = st.number_input('Applicant credit history length', min_value=0)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, step=1)
previous_loan_defaults_on_file_Yes = st.radio('Default payment on previous loan Yes', [True, False])
person_home_ownership_MORTGAGE = st.radio('MORTGAGE as home ownership',  [True, False])
person_home_ownership_OWN = st.radio('OWNER as home ownership', [True, False])
person_home_ownership_RENT = st.radio('RENT as home ownership', [True, False])


# Button to do a single prediction
if st.button('Predict'):
    # API Data Processing
    data = {
        'person_age': person_age,
        'person_income': person_income,
        'person_emp_exp': person_emp_exp,
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_percent_income': loan_percent_income,
        'cb_person_cred_hist_length': cb_person_cred_hist_length,
        'credit_score': credit_score, 
        'previous_loan_defaults_on_file_Yes': previous_loan_defaults_on_file_Yes,
        'person_home_ownership_MORTGAGE': person_home_ownership_MORTGAGE,
        'person_home_ownership_OWN': person_home_ownership_OWN,
        'person_home_ownership_RENT': person_home_ownership_RENT
    }
    # Call the API to obtain the prediction
    prediction = predict_single(data)
    # Showing the prediction
    if prediction:
        st.success(f'The prediction is : {prediction}')

# Download CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Viewing CSV data
    st.write("CSV file Data:")
    st.write(df)
    
    # Checking that the CSV has the right columns
    expected_columns = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt',
       'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length',
       'credit_score', 'loan_status', 'previous_loan_defaults_on_file_Yes',
       'person_home_ownership_MORTGAGE', 'person_home_ownership_OWN',
       'person_home_ownership_RENT']
    if all(col in df.columns for col in expected_columns):
        # Prepare data for API
        data = df[expected_columns]
        
        # Make predictions for each CSV line
        predictions = [predict_single(d) for d in data]
        
        # Adding predictions to the DataFrame
        df['prediction'] = predictions
        
        # Show DataFrame with predictions
        st.write("Prediction results:")
        st.write(df)
    else:
        # Error message if columns are incorrect
        st.error(f"The CSV file must contain the following columns: {expected_columns}")
