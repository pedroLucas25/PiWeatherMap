
import requests
from json import JSONDecodeError

from config import Config
from app.Models.LocationByNameModel import LocationByName

class LocationRequest:
        
    def GetLocationByStateNCountry(self, state, country, city):

        try:
            if not country and (any(country == _country.alfa_2 for _country in Config.iso_3166)):
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
            
            print(f"Nome: {locationByName.name}, country: {locationByName.country}")
        except requests.RequestException as e:
            print(f"Erro na requisição: {e}")
        except JSONDecodeError:
            print("Erro ao decodificar o JSON")
        except KeyError:
            print("Erro ao acessar uma chave no dicionário de dados")
        except Exception as e:
            print(e)