from flask import Flask, url_for
from  flask import jsonify , make_response
from flask import request
from errorhandler import *
from validation import PostValidation
from model import Insertion ,LIST_ALL
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

@app.route('/shortlinks', methods=['PUT'])
def api_Updateshortlink():
    return 'update of shortlink '



if __name__ == '__main__':
    app.run()
