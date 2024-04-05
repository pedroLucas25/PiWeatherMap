from functools import wraps
from flask import make_response, abort, jsonify, g, request
from app.Models.responseModel import Response

from app.Dal.Workspaces.InfoDal import InfoDal

def verify_access(function):
    @wraps(function)
    def wrapper(**view_args):

        headers = request.headers
    
        #auth = AuthBLL()
        is_auth = 1# auth.verify_access(headers)
        
        if is_auth == 1:
            return function(**view_args)
        else:
            return no_auth()
            
    return wrapper

def no_auth():
    response = Response(401,'Access Denied!', {})
    return make_response(response.to_dict(), 401)

def get_workspace_info(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        
        email = kwargs.get('email')
        token = kwargs.get('token')

        if not email:
            email = request.headers.get('email')

        if not token:
            token = request.headers.get('token')

        if email is not None and token is not None:
            
            infoDal = InfoDal()
            workspace = infoDal.info(token, email)

            if not workspace:
                response = Response(500,'Workspace not found!', {})
                return make_response(response.to_dict(), 500)
			
        else:
            response = Response(500, 'Incomplete header parameters [token, email]', {})
            return make_response(response.to_dict(), 500)

        g.workspace = workspace
        return function(*args, **kwargs)
    return decorator