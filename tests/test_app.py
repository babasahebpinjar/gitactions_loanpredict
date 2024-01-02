from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is in a file named main.py
import json

client = TestClient(app)

def test_hello_world():
    response = client.post("/predict")
    assert response.status_code == 200
    #print("<<<<<<<<<<<<<<<<<")
    assert response.json() == "Hello World"


def test_prediction():
    sample_input = {
        "Gender": "Male",
        "Married": "Unmarried",
        "Credit_History": "Unclear Debts",
        "ApplicantIncome": 5000,
        "LoanAmount": 150
    }

    # get response
    response = client.post("/predict1?requestVal=" + json.dumps(sample_input))
    result = response.json()
    assert 'loan_approval_status' in result
    assert result['loan_approval_status'] in ['Approved', 'Rejected']
    print(response.content)
    assert response.status_code == 2001
