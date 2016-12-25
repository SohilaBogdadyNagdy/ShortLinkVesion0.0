from flask_inputs.validators import JsonSchema
from flask_inputs import Inputs
from jsonschema import validate
import jsonschema
from errorhandler import *
import json
CreateLinkschema = {

  "$schema": "http://json-schema.org/draft-04/schema#",

  "properties": {
    "slug": {
      "type": "string",
      "description": "shortlink code"
    },
    "ios": {
      "type": "object",
      "properties": {
        "primary": {
          "type": "string"
        },
        "fallback": {
          "type": "string"
        }
      },
      "required": [
        "primary",
        "fallback"
      ],
      "description": "iPhone URLs"
    },
    "android": {
      "type": "object",
      "properties": {
        "primary": {
          "type": "string"
        },
        "fallback": {
          "type": "string"
        }
      },
      "required": [
        "primary",
        "fallback"
      ],
      "description": "Android URLs"
    },
    "web": {
      "type": "string",
      "description": "Other platforms"
    }
  },
  "required": [
    "ios",
    "android",
    "web"
  ]
}

def  PostValidation(myrequest):
    """
    validate post data  coming with  request
    """
    try:
        validate (myrequest,CreateLinkschema)
        response= jsonify({
            "status": "successful",
            "slug": myrequest['slug'],
           "message": "created successfully"

        })
        response.status_code=201
        return response
    except :
        print ("catch  validation eror")
        response= bad_request("failed in validation request data")
        return response

iosupdateSchema ={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "ios": {
      "type": "object",
      "properties": {
        "fallback": {
          "type": "string"
        }
      },
      "description": "iPhone URLs"
    }
  }
}
webupdateSchema =     {
  "$schema": "http://json-schema.org/draft-04/schema#",

  "properties": {
    "web": {
      "type": "string",
      "description": "Other platforms"
    }
  }
}

def updateReValidation (req):

    ob=list (req.json .items())
    updatedlink=""
    if (ob[0][0]=='ios'):
        #validate ios schema
        try :
            jsonschema.validate (req.json ,iosupdateSchema )
            print ("pass validate method")
            updatedlink="ios"
            return updatedlink
        except :
            return bad_request("invalid request ios")


    else :
        #validate web schema
        try :
            validate (req.json,webupdateSchema)
            updatedlink="web"
            return updatedlink
        except :
            return bad_request("invalid request web")




                         
