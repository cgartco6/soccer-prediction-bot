import requests
from config import settings

class TelegramNotifier:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"
        
    def send_predictions(self, predictions):
        message = self.format_message(predictions)
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }
        response = requests.post(url, json=payload)
        return response.status_code == 200
    
    def format_message(self, predictions):
        # Format prediction data for Telegram
        message = "⚽️ *AI Soccer Predictions* ⚽️\n\n"
        for pred in predictions:
            message += f"**{pred['home']} vs {pred['away']}**\n"
            message += f"Prediction: {pred['result']} | Score: {pred['score']}\n"
            message += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        return message
