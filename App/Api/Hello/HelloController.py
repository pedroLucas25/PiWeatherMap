from app import app
from flask import make_response, g

from app.Models.responseModel import Response

@app.route('/', methods=['GET'])
def hello_get():

    try:
    
        response = {
            'response' : 'Hello World'
        }

        response = Response(200, '', response)
        return make_response(response.to_dict(), 200)

    except Exception as e:
        print(str(e))
        response = Response(500, str(e), {})
        return make_response(response.to_dict(), 500)