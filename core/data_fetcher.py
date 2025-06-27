from core.self_healing import SelfHealingSystem
from config import settings

class DataFetcher:
    def __init__(self):
        self.healing = SelfHealingSystem()
    
    def get_fixtures(self):
        url = "https://api.football-data.org/v4/matches"
        params = {'date': datetime.now().strftime('%Y-%m-%d')}
        headers = {'X-Auth-Token': settings.FOOTBALL_API_KEY}
        
        return self.healing.api_request(
            url,
            params=params,
            headers=headers,
            cache_key="fixtures"
        )
    
    def get_team_data(self, team_id):
        url = f"https://api.football-data.org/v4/teams/{team_id}"
        headers = {'X-Auth-Token': settings.FOOTBALL_API_KEY}
        
        return self.healing.api_request(
            url,
            headers=headers,
            cache_key=f"team_{team_id}"
        )
    
    def get_weather(self, location):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': location,
            'appid': settings.WEATHER_API_KEY,
            'units': 'metric'
        }
        
        return self.healing.api_request(
            url,
            params=params,
            cache_key=f"weather_{location}"
        )
