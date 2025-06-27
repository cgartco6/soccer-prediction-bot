import joblib
import os

def load_model(model_path='models/soccer_model.pkl'):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        print("Model not found, using fallback")
        return None

def save_model(model, model_path='models/soccer_model.pkl'):
    joblib.dump(model, model_path)
