from flask import Flask, url_for
from  flask import jsonify , make_response
from flask import request
from errorhandler import *
from validation import PostValidation,updateReValidation
from model import *
import json
app = Flask(__name__)
app.config.from_object('config')

@app.route('/shortlinks', methods=['get'])
def getShortlinks():
    if (request.headers.get('content-type') != 'application/json'):
        return Non_JSON()
    else:
        #get all
        storedLinks=LIST_ALL()
        if (len (storedLinks) == 0 ):
            return empty()
        JsonLinks=json.dumps (storedLinks)
        return (jsonify ({'shortlinks':JsonLinks}) )




@app.route('/shortlinks', methods=['POST'])
def CreateShortlink():
    if ( not request.json):
        return Non_JSON()
    else :
         output=PostValidation(request.json)
         if (output.status_code==201):
             #add new documents in db
             InsertionFlag=Insertion(request)
             if InsertionFlag==False :
                 output=not_found("failed in creation")

         return output

@app.route('/shortlinks/<string:slug>', methods=['PUT'])
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
                       updateWebLink(slug,request.json['web'])
                   else :
                       updateIosPrimaryLink(slug,request.json['ios']['fallback'])
                   return "define succcesful"

               else :
                   print ("invalid update request")
                   return output


         else:
             return bad_request("invalid slug ")



if __name__ == '__main__':
    app.run()
