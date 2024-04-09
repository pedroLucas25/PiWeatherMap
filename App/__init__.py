import sys

def create_app():

    from app.LocationRequest.LocationRequest import LocationRequest

    try:
        
        if len(sys.argv) < 1:
           print('Usage: python main.py country state city')
        
        # country = sys.argv[1]
        # state = sys.argv[2]
        city = sys.argv[1]
        
        LocationRequest.GetLocationByCity(
            city = city
        )
        
        # return app
        
    except Exception as e:
        print(e)

    