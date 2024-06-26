
import requests
from json import loads, JSONDecodeError

from PiWeatherMap.config import Config
from PiWeatherMap.Models.LocationByNameModel import LocationByName

class LocationRequest:
        
    def GetLocationByStateNCountryNCity(country, state, city):

        try:
            if not country:
                raise Exception('Invalid Coutry!')
            
            if not state:
                raise Exception('Invalid State!')
            
            if not city:
                raise Exception('Invalid City!')
            
            url = Config.geolocation_url + 'q=' + city + ',' + state + ',' + country + '&appid=' + Config.appid

            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()
    
            locationByName = LocationByName(
                name = data['name'],
                localName = data['local_names'],
                lat = data['lat'],
                lon = data['lon'],
                country = data['country'],
                state = data['state']
            )
            
            return locationByName
        
        except requests.RequestException as e:
            raise Exception(f"Erro na requisição: {e}")
        except JSONDecodeError:
            raise Exception("Erro ao decodificar o JSON")
        except KeyError:
            raise Exception("Erro ao acessar uma chave no dicionário de dados")
        except Exception as e:
            raise Exception(e)

    def GetLocationByCity(city):
        
        try:
            
            if not city:
                raise Exception('Invalid City!')
            
            url = Config.geolocation_url + 'q=' + city + '&appid=' + Config.appid

            response = requests.get(url)
            response.raise_for_status()  
            data_tmp = loads(response.text)
            data = data_tmp[0]
    
            locationByName = LocationByName(
                name = data['name'],
                lat = data['lat'],
                lon = data['lon'],
                country = data['country'],
                state = data['state']
            )
            
            return locationByName
        
        except requests.RequestException as e:
            raise Exception(f"Erro na requisição: {e}")
        except JSONDecodeError:
            raise Exception("Erro ao decodificar o JSON")
        except KeyError:
            raise Exception("Erro ao acessar uma chave no dicionário de dados")
        except Exception as e:
            raise Exception(e)