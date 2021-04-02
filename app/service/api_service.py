
import requests
import os


APPID = os.environ["APPID"]

class OpenWeatherMap:
    def __init__(self) -> None:
        self.baseUrl = "https://api.openweathermap.org/data/2.5/"

    def getForecast(self, city):
        coord = self.getLocation(city)
        params = {
            "lat": coord["lat"],
            "lon": coord["lon"],
            "exclude": "current,minutely,hourly,alerts",
            "appid": APPID,
            "lang": "pt_br",
            "units": "metric",
        }
        url = self.baseUrl + "onecall"
        response = requests.get(url, params=params)
        return response.json()
    
    def getLocation(self, city):
        params = {
            "q": city,
            "appid": APPID,
            "lang": "pt_br",
        }
        
        url = self.baseUrl + "weather"
        response = requests.get(url, params=params)
        return response.json()["coord"]
