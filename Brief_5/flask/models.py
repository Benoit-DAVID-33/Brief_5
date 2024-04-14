import joblib

def load_model():
    """Charger le modèle pré-entraîné."""
    # model = joblib.load('C:/Users/benoi/Desktop/CODE/code bureau/Simplon_exercice//Brief_5/random_forest_model.pkl')
    model = joblib.load('random_forest_model.pkl')
    return model

def predict_imdb_score(model, data):
    """Faire une prédiction de note IMDb."""
    prediction = model.predict(data)
    return prediction
