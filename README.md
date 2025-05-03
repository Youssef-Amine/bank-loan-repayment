# bank-loan-repayment
This project aims to predict bank loan repayment with classification alagorithms. 
 algoriths are used for modeling and a data visualization application with Sreamlit set to provide interactive insights.
## Objectives

- Analyze and preprocess records of loan applicants, with various attributes related to personal demographics, financial status, and loan details.
- Build Logistic regression Random Forest and XGBoost models
- Evaluate models with Confusion matrix, Precision, Recall, F1-score and PR-AUC to choose the best model
- Visualization application with Streamlit

---

## Project structure
```bash
bank-loan-repayment/
|
├── README. md # Project description
├── requirements.txt # Packages required
|
├── downloaddata.txt # Data link 
|
├── LoanRepaymentClassification. ipynb # Working notebook
|
├── loanRF_model. rar # Saved model
|
├── app. py # Interactive app (Streamlit)
├── main. py #Server configuration 
```

## Technologies used

- Python (pandas, numpy, matplotlib, seaborn)
- Sklearn (Logistic regression, Random Forest, metrics)
- FastAPI
- Scikit-learn
- Streamlit
---

## Results
The Random Forest model probably overfits. The score is perfect on training data but its performance decreases on the test data, which means it doesn't generalize perfectly.

The XGBoost model learns well without overfiting. There is less discrepancy between the train and the test, showing a better ability to generalize. In practice, this is the model to use here, as it is more robust.

Here we will choose Random Forest only the visualization purpose. In the Random Forest models there are more important features and it will need these features for data entries. In our Random Forest model, we can see around 12 important features, we will perform another Random Forest model with only these features for our application.


## References
- Kaggle dataset: https://www.kaggle.com/datasets/udaymalviya/bank-loan-data


> Portfolio project developed in 2025 by Youssef SAWADOGO. If you have any questions, please contact me via wyoussef.sawadogo@gmail.com.


