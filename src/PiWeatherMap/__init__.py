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

        response = {
            'name': data_tmp.name,
            'lat': data.lat,
            'lon': data.lon,
            'timezone_offset': data.timezone_offset,
            'daily': data.daily
        }
        
        return response
        
    except Exception as e:
        raise Exception(e)

    