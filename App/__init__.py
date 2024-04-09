import sys

def return_data():

    from app.LocationRequest.LocationRequest import LocationRequest

    try:
        
        if len(sys.argv) < 1:
           print('Usage: python main.py city')
        
        # country = sys.argv[1]
        # state = sys.argv[2]
        city = sys.argv[1]
        
        data = LocationRequest.GetLocationByCity(
            city = city
        )
        
        return data
        
    except Exception as e:
        print(e)

    