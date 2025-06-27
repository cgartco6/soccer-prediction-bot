import requests
import time
from datetime import datetime, timedelta
from config import settings

class SelfHealingSystem:
    def __init__(self):
        self.fallback_cache = {}
        self.error_count = 0
        
    def api_request(self, url, params=None, headers=None, cache_key=None):
        for attempt in range(settings.MAX_API_RETRIES):
            try:
                response = requests.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()
                
                if cache_key:
                    self.fallback_cache[cache_key] = (data, datetime.now())
                    
                return data
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {str(e)}")
                time.sleep(2 ** attempt)  # Exponential backoff
        
        # Fallback to cached data
        if cache_key and cache_key in self.fallback_cache:
            data, timestamp = self.fallback_cache[cache_key]
            if datetime.now() - timestamp < timedelta(hours=settings.CACHE_EXPIRY_HOURS):
                print(f"Using cached data for {cache_key}")
                return data
        
        raise ConnectionError(f"API unavailable after {settings.MAX_API_RETRIES} attempts")
    
    def monitor_health(self):
        if self.error_count > 5:
            self.recover_system()
    
    def recover_system(self):
        print("Performing system recovery...")
        self.error_count = 0
        # Add recovery logic here
