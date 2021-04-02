
import requests
import os
from datetime import datetime, time
import pytz

APPID = os.environ["APPID"]


class OpenWeatherMap:
    def __init__(self) -> None:
        self.baseUrl = "https://api.openweathermap.org/data/2.5/"

    def getForecast(self, city, sort=True):
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
        response = requests.get(url, params=params).json()
        
        if sort:
            timezone = pytz.timezone(response["timezone"])
            response["daily"].pop()
            for index,forecastDay in enumerate(response["daily"]):
                localTime = datetime.fromtimestamp(forecastDay["dt"],timezone)
                
                weekDay = localTime.strftime("%w")
                response["daily"][index]["weekday"] = int(weekDay)
            
            response["daily"].sort( key=lambda x: x["weekday"])
            
        return response
    
    def getLocation(self, city):
        params = {
            "q": city,
            "appid": APPID,
            "lang": "pt_br",
        }
        
        url = self.baseUrl + "weather"
        response = requests.get(url, params=params)
        return response.json()["coord"]
