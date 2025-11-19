from flask import jsonify
from .types.http_error_server import HttpErrorServer
from src.main.http_types.http_response.http_response import HttpResponse

def error_handler(error: Exception):

    if (isinstance(error, HttpErrorServer)):

        return HttpResponse(
            body={"error": {
                "title": error.name,
                "message": error.message
            }},
            status_code=error.status_code)
    
    else:

        return HttpResponse(body={
            "error":{
                "title":"Error Server",
                "message":str(error)
            }
        }, status_code=500)