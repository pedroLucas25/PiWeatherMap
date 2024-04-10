def return_data(city):

    from app.LocationRequest.LocationRequest import LocationRequest
    from app.WeatherRequest.WeatherRequest import WeatherRequest

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

    