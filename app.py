from fastapi import FastAPI, Request
from flask import Flask, request, Response, jsonify
import pickle
import uvicorn
import json
from fastapi.responses import JSONResponse
## loading the model
model_pickle = open("./artifacts/classifier.pkl", 'rb')
clf = pickle.load(model_pickle)


app = FastAPI()


@app.post("/predict")
async def home(request: Request):
    return "Hello World"


@app.post('/predict1',)
async def prediction(requestVal:str):
    # Pre-processing user input
    print("-----",requestVal)
    requestVal = json.loads(requestVal)
    print(type(requestVal))
    loan_req = requestVal #.get_json()
    print(loan_req) 

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000
 
    # Making predictions 
    prediction = clf.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    result = {
        'loan_approval_status': pred
    }

    return JSONResponse(content=result)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
