import requests
from json import loads, JSONDecodeError

from PiWeatherMap.config import Config
from PiWeatherMap.Models.CurrentNForecastWeatherModel import CurrentNForecastWeatherModel

class WeatherRequest:

    def GetWeatherByLatNLon(lat, lon):
        try:
            
            if not lat:
                raise Exception('Invalid latitude!')
            if not lon:
                raise Exception('Invalid longitude!')
            
            exclude = 'minutely,hourly,alerts'
            lang = 'pt'
            units = 'metric'
            
            url = Config.weather_url +\
                  'lat=' + str(lat) +\
                  '&lon=' + str(lon) +\
                  '&exclude=' + exclude +\
                  '&lang=' + lang +\
                  '&units' + units +\
                  '&appid=' + Config.appid

            response = requests.get(url)
            response.raise_for_status()  
            data = loads(response.text)
    
            currentNForecastWeatherModel = CurrentNForecastWeatherModel(
                lat = data['lat'],
                lon = data['lon'],
                timezone = data['timezone'],
                timezone_offset = data['timezone_offset'],
                current = data['current'],
                minutely = None,
                hourly = None,
                daily = [day_data for day_data in data['daily'][:5]],
                alerts = None
            )

            # raise Exception(currentNForecastWeatherModel.daily[0]['weather'][0]['description'])
            
            return currentNForecastWeatherModel
        
        except requests.RequestException as e:
            raise Exception(f"Erro na requisição: {e}")
        except JSONDecodeError:
            raise Exception("Erro ao decodificar o JSON")
        except KeyError:
            raise Exception("Erro ao acessar uma chave no dicionário de dados")
        except Exception as e:
            raise Exception(e)
