from flask import jsonify
from flask import Response
#from app import app
def successful_opr(msg):
    response = jsonify ({"status": "successful",
  "message": msg })
    response.status_code=201
    return response
#@app.errorhandler(404)
#def not_found_page(e):
#    return jsonify({'error':e})
#@app.errorhandler (500)
#def  server_error(e):
#    return jsonify({'error':e})

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
