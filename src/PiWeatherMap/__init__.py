def return_data(city):

    from PiWeatherMap.LocationRequest.LocationRequest import LocationRequest
    from PiWeatherMap.WeatherRequest.WeatherRequest import WeatherRequest

    try:
        
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

    