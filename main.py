from core.data_fetcher import DataFetcher
from core.predictor import SoccerPredictor
from services.telegram_service import TelegramNotifier
from config import settings
from datetime import datetime

def main():
    print(f"🚀 Starting prediction engine: {datetime.now()}")
    
    # Initialize components
    data_fetcher = DataFetcher()
    predictor = SoccerPredictor()
    notifier = TelegramNotifier()
    
    try:
        # Fetch data
        fixtures = data_fetcher.get_fixtures()['matches'][:settings.MAX_MATCHES]
        
        predictions = []
        for match in fixtures:
            # Get detailed data
            home_data = data_fetcher.get_team_data(match['homeTeam']['id'])
            away_data = data_fetcher.get_team_data(match['awayTeam']['id'])
            weather = data_fetcher.get_weather(match['area']['name'])
            
            # Make prediction
            probs = predictor.predict_match(home_data, away_data, weather)
            score = predictor.predict_score(probs[0], probs[2])
            
            predictions.append({
                'home': match['homeTeam']['name'],
                'away': match['awayTeam']['name'],
                'result': f"H: {probs[0]:.0%} D: {probs[1]:.0%} A: {probs[2]:.0%}",
                'score': score
            })
        
        # Send to Telegram
        if notifier.send_predictions(predictions):
            print("✅ Predictions sent successfully")
        else:
            print("❌ Failed to send predictions")
            
    except Exception as e:
        print(f"🔥 Critical error: {str(e)}")
        data_fetcher.healing.error_count += 1
        data_fetcher.healing.monitor_health()

if __name__ == "__main__":
    main()
