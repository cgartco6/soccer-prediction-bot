import os

class Config:
    # API Keys
    FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY", "f51d01426524472192e4192e1aa0c842")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "07522d8003069c55cbc36f67ad21abe5")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_telegram_bot_token")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "your_telegram_chat_id")
    
    # System Parameters
    MAX_MATCHES = 16
    CACHE_EXPIRY_HOURS = 6
    MAX_API_RETRIES = 3
