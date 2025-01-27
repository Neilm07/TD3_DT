from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

# Charger le dataset Iris
data = load_iris()
X, y = data.data, data.target

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -------------------- LogisticRegression --------------------
# Créer et entraîner un modèle Logistic Regression
lr_model = LogisticRegression(max_iter=200, random_state=42)
lr_model.fit(X_train, y_train)

with open("iris_model.pkl","wb") as file:
    pickle.dump(lr_model,file)

    
"""
# Faire des prédictions
lr_y_pred = lr_model.predict(X_test)

# Afficher le rapport de classification
print("\n=== LogisticRegression ===")
print(classification_report(y_test, lr_y_pred))
"""
