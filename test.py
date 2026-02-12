import joblib
from sklearn.datasets import load_iris

# Load model
model = joblib.load("model.pkl")

# Load sample data
iris = load_iris()
sample = iris.data[0].reshape(1, -1)

prediction = model.predict(sample)

print("Test Prediction:", prediction)
