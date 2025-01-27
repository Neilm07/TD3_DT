#app.py avec flask
from sklearn.datasets import load_iris
from flask import Flask, request, jsonify
import pickle
import numpy as np


iris=load_iris()

app = Flask(__name__)

# Load the pre-trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get features from query parameters
        sepal_length = float(request.args.get('sepal_length'))
        sepal_width = float(request.args.get('sepal_width'))
        petal_length = float(request.args.get('petal_length'))
        petal_width = float(request.args.get('petal_width'))
        
        # Prepare input for prediction
        input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_features)[0]
        confidence = max(model.predict_proba(input_features)[0])
	
        return jsonify({
            "model": "Logistic Regression",
            "prediction": int(prediction),
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"error": str(e)})
    
app.run(host="0.0.0.0")

#lien avec les arguments : http://localhost:5000/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2

#lien ngrok : https://50da-89-30-29-68.ngrok-free.app/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2