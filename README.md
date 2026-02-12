# ML CI/CD Pipeline with Jenkins (Iris Classification)

This project demonstrates an end-to-end Machine Learning workflow integrated with Jenkins CI/CD pipeline.

It includes:

- Model Training
- Model Testing
- Flask Deployment
- Automated CI Pipeline using Jenkins

---

## Project Overview

We use the **Iris dataset** to:

1. Train a Machine Learning model
2. Save the trained model (`model.pkl`)
3. Test model functionality
4. Deploy it using a Flask API
5. Automate the process using Jenkins

---

## Project Structure
jenkins_ml/
│
├── train.py # Trains model and saves model.pkl
├── test.py # Loads and tests the saved model
├── app.py # Flask API to serve predictions
├── requirements.txt # Python dependencies
├── Jenkinsfile # CI Pipeline definition
└── README.md


---

## ⚙️ Technologies Used

- Python 3.11
- Scikit-learn
- Flask
- Joblib
- Jenkins
- Git & GitHub

---

## Machine Learning Workflow

### 1) Training
- Loads Iris dataset
- Splits into train/test
- Trains RandomForestClassifier
- Saves model as `model.pkl`

### 2) Testing
- Loads `model.pkl`
- Performs sample prediction
- Ensures model works correctly

### 3️) Deployment
- Flask API exposes:
  - `GET /` → Health check
  - `POST /predict` → Model prediction

---

##  API Usage

### Health Check
http://127.0.0.1:5000/
Response: ML Model is Running!

---

### Prediction Endpoint

POST request: http://127.0.0.1:5000/predict
JSON Body:
json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Response:
{
  "prediction": 0
}

## Jenkins CI Pipeline Stages

Checkout Source Code
Create Virtual Environment
Install Dependencies
Train Model
Test Model
Build Success Confirmation
Pipeline is defined inside:
Jenkinsfile

## How to Run Locally
1️) Clone Repository
git clone https://github.com/mandalsantanu16092002/dvc-lab.git
cd dvc-lab

2️) Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️) Install Dependencies
pip install -r requirements.txt

4️) Train Model
python train.py

5️) Run Flask App
python app.py


Open: http://127.0.0.1:5000

## CI/CD Integration

This project demonstrates:

✔ Automated ML training
✔ Automated testing
✔ Continuous Integration using Jenkins
✔ Source control with GitHub

## Future Improvements

Dockerize application
Deploy to cloud (AWS / Azure)
Add GitHub Webhook for auto build
Add model versioning
Add logging & monitoring

👨‍💻 Author
Santanu Mandal
DevOps & MLOps Enthusiast

