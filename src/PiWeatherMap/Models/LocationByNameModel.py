# class LocalNameCode:

#     def __init__(self, language, localName):
#         self.language = language
#         self.localName = localName



class LocationByName:
    
    def __init__(self, name, localName, lat, lon, country, state):
        self.name = name
        self.localNameCode = localName
        self.lat = lat
        self.lon = lon
        self. country = country
        self.state = state