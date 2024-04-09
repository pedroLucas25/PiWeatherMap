import sys

def return_data():

    from app.LocationRequest.LocationRequest import LocationRequest
    from app.WeatherRequest.WeatherRequest import WeatherRequest

    try:
        
        if len(sys.argv) < 1:
           print('Usage: python main.py city')
        
        # country = sys.argv[1]
        # state = sys.argv[2]
        city = sys.argv[1]
        
        data_tmp = LocationRequest.GetLocationByCity(
            city = city
        )

        data = WeatherRequest.GetWeatherByLatNLon(
            lat = data_tmp.lat,
            lon = data_tmp.lon
        )
        
        return data
        
    except Exception as e:
        print(e)

    