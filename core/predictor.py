import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from models.prediction_model import load_model
from utils.helpers import calculate_features

class SoccerPredictor:
    def __init__(self):
        self.model = load_model()
        
    def predict_match(self, home_data, away_data, weather):
        try:
            # Feature engineering
            features = calculate_features(home_data, away_data, weather)
            
            # Model prediction
            if self.model:
                return self.model.predict_proba([features])[0]
            else:
                # Fallback algorithm
                return self.fallback_prediction(home_data, away_data)
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            return [0.35, 0.35, 0.30]  # Default probabilities
    
    def predict_score(self, home_win_prob, away_win_prob):
        # Score prediction logic
        home_goals = max(0, min(3, round(1.5 + home_win_prob - away_win_prob)))
        away_goals = max(0, min(3, round(0.8 + away_win_prob - home_win_prob)))
        return f"{home_goals}-{away_goals}"
    
    def simulate_bookie(self, prediction, bookie_name):
        # Bookie algorithm simulation
        pass
