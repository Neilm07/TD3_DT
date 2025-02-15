#client.py comparaison avec les résultats sur l'url des autres (métamodèles) et implémenter l'algo de POS (proof of stake)
import requests
import numpy as np
from collections import Counter
import pos.py
from pos.py import *

# List of API URLs for group members
api_urls = ["https://5fc9-89-30-29-68.ngrok-free.app/predict", "https://50da-89-30-29-68.ngrok-free.app/predict", "https://b05d-89-30-29-68.ngrok-free.app/predict"]
model_weights = {"model1": 0.8, "model2": 0.9, "model3": 0.7}

def adjust_weights(model_name, isCorrect):
    # Increase weight if accurate, decrease otherwise
    model_weights[model_name] = max(0, min(1, model_weights[model_name] +  (isCorrect ? 0.1 : -0.1)))

def get_predictions(features):
    predictions = []
    for url in api_urls:
        response = requests.get(url, params=features)
        if response.status_code == 200:
            predictions.append(response.json()['prediction'])
    # Perform majority voting (choose the most common class)
    if predictions:
        majority_vote = Counter(predictions).most_common(1)[0][0]
        for i in range(3):
            model_name = "model" + str(i)
            if predictions[i]!=majority_vote:
                slash_balance(model_name,10)
                adjust_weights(model_name,False)
            else:
                reward_balance(model_name,10)
                adjust_weights(model_name,True)             
        return majority_vote
    else:
        raise ValueError("No predictions were collected from the APIs.")

# Feature inputs
features = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}

# Get the consensus prediction
consensus_prediction = get_predictions(features)
print("Consensus Prediction:", consensus_prediction)
