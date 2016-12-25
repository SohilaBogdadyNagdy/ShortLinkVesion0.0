from flask import jsonify
from flask import Response

def not_found(mesg):
    response = jsonify ({'status':"failed", "message":mesg})
    response.status_code=404
    return response
def empty():
    response =jsonify ({})
    response.status_code=500
    return response
def Auth_failed():
    response = jsonify ({'status':'failed','message': "auth failed, failed to login user"})
    response.status_code=401
    return response

def  Non_JSON():
    return bad_request("failed : Non-JSON Content-Type")


def  bad_request(failuremsg):

    response = jsonify (    {
  "status": failuremsg,
  "message": "Bad Request"
}  )
    response.status_code=400
    return response 
