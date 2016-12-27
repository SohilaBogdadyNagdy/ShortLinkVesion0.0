from flask import Flask, url_for
from  flask import jsonify , make_response
from flask import request
from errorhandler import *
from validation import PostValidation,updateReValidation
from model import *
from decorator import *
import json
app = Flask(__name__)
app.config.from_object('config')

@app.route('/shortlinks', methods=['get'])
@requires_auth
def getShortlinks():
    if (request.headers.get('content-type') != 'application/json'):
        return Non_JSON()
    else:
        #get all
        storedLinks=LIST_ALL()
        if (len (storedLinks) == 0 ):
            return not_found("not found shortlink")
        return (jsonify ({'shortlinks':storedLinks}) )

@app.route('/shortlinks', methods=['POST'])
@requires_auth
def CreateShortlink():
    if ( not request.json):
        return Non_JSON()
    else :
         output=PostValidation(request.json)
         if (output==True ):
             #add new documents in db
             output=Insertion(request)
             return output
         return output

@app.route('/shortlinks/<string:slug>', methods=['PUT'])
@requires_auth
def api_Updateshortlink(slug):
     if (request.headers.get('content-type') != 'application/json'):
        return Non_JSON()
     if (len(slug) == 0):
        not_found("slug is a required")
     else :
         if (str (slug).isalnum() ):
             #go to  apply validation on request body
               output=updateReValidation(request)
               if (type (output)== str ): #request valid and update opeation will called
                   print ("call update method")
                   if (output=="web"):
                       output= updateWebLink(slug,request.json['web'])
                       return output
                   else :
                       output=updateIosfallbackLink(slug,request.json['ios']['fallback'])
                       return output

               else :
                   print ("invalid update request")
                   return output


         else:
             return bad_request("invalid slug ")

@app.errorhandler(500)
def server_error(e):
    #for internal server error exception
    return jsonify({})
@app.errorhandler(404)
def page_notfound(e):
    """register page not found method at 404 error """
    res=jsonify ({"status":"failed",
                    "message":"not found"
                    })
    res.status_code=404
    return res

if __name__ == '__main__':
    app.run()
