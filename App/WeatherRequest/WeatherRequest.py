import requests
from json import loads, JSONDecodeError

from config import Config
from app.Models.CurrentNForecastWeatherModel import CurrentNForecastWeatherModel

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
            
            url = ''
            url.join([
                Config.weather_url, 'lat=', lat,
                '&lon=', lon,
                '&exclude=', exclude,
                '&lang=', lang,
                '&units', units,
                '&appid=', Config.appid
            ])

            response = requests.get(url)
            response.raise_for_status()  
            data_tmp = loads(response.text)
            data = data_tmp[0]
    
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

            print(currentNForecastWeatherModel.daily['weather']['description'])
            
            return currentNForecastWeatherModel.daily
        
        except requests.RequestException as e:
            print(f"Erro na requisição: {e}")
        except JSONDecodeError:
            print("Erro ao decodificar o JSON")
        except KeyError:
            print("Erro ao acessar uma chave no dicionário de dados")
        except Exception as e:
            print(e)
