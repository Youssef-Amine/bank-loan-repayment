from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
#pip install fastapi uvicorn joblib sklearn pip install scikit-learn
#uvicorn main:app --reload
# Loading of the model
model = joblib.load('loanRF_model.pkl')

# Creation of the app
app = FastAPI()

# Feature to request for the prediction
class LoanData(BaseModel):
    person_age: float
    person_income: float
    person_emp_exp: int
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    credit_score: int
    previous_loan_defaults_on_file_Yes: bool
    person_home_ownership_MORTGAGE: bool
    person_home_ownership_OWN: bool
    person_home_ownership_RENT: bool

# Home Endpoint
@app.get("/")
def read_root():
    """
    Home Endpoint of the API.
    Returns a welcome message with an indication of how to use the API.
    """
    return {"message": "Welcome to the Loan Repayment prediction API. Use the /predict endpoint to make predictions."}

# Prediction Endpoint 
@app.post("/predict")
def predict(data: LoanData):
    """
    Endpoint for making predictions about loan repayment.
    Receives applicant characteristics as input and returns prediction.
    """
    # Extraction of query characteristics and conversion into a dataframe
    features = pd.DataFrame([data.model_dump()])
    # Use of the model for prediction
    prediction = model.predict(features)[0]
    message = "The applicant repays the loan" if prediction == 1 else "The applicant does not repay the loan"
    # Return a compatible JSON response
    return {"prediction": message}

# To start the server : uvicorn main:app --reload
