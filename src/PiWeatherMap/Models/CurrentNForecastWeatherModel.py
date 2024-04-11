class CurrentNForecastWeatherModel:
    
    def __init__(self, lat, lon, timezone, timezone_offset, current, minutely, hourly, daily, alerts):
        self.lat = lat
        self.lon = lon
        self.timezone = timezone
        self.timezone_offset = timezone_offset
        self.current = current
        self.minutely = minutely
        self.hourly = hourly
        self.daily = daily
        self.alerts = alerts