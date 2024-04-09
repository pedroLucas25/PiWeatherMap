import sys

def create_app():

    from app.LocationRequest.LocationRequest import LocationRequest

    try:
        
        if len(sys.argv) < 4:
           print('Usage: python main.py country state city')
        
        country = sys.argv[1]
        state = sys.argv[2]
        city = sys.argv[3]
        
        app = LocationRequest.GetLocationByStateNCountryNCity(
            country = country,
            state = state,
            city = city
        )
        
        return app
        
    except Exception as e:
        return e

    