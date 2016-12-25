from config import client
from flask import request
from mongoframes import *
from errorhandler import *
#   Database: ag-test-5163
#   User: kzynA
#   Password: kACkB64Me
#   MongoDB URI: mongodb://<dbuser>:<dbpassword>@ds019926.mlab.com:19926/ag-test-5163
#mongo ds019926.mlab.com:19926/ag-test-5163 -u kzynA -p kACkB64Me
#mongo mongodb://kzynA:kACkB64Me@ds019926.mlab.com:19926/ag-test-5163
#    # mongo --host=ds019926.mlab.com: --port=19926 --username kzynA --password kACkB64Me
Frame._client = client
db=client['ag-test-5163']
class ShortLink(Frame):

    _fields = {
        'slug',
        'ios',
        'android',
        'web'
        }

class Item(SubFrame):

    _fields = {
        'primary',
        'fallback'
        }

#buid insert , get and update  methods
def Insertion (request):
    MyNewShortLink = ShortLink (
        slug=request.json['slug'],
        ios = Item(
          primary=request.json ['ios']['primary'],
          fallback=request.json['ios']['fallback']
        ),
        android=Item (
            primary=request.json['android']['primary'],
            fallback=request.json['android']['fallback']
        ),
        web=request.json['web']

    )
    try :

        MyNewShortLink.insert ()
        return True

    except :
        print ("failed in insertion process")
        return False

def LIST_ALL():

    """list all document in my shortlink collection """
    doc= db.ShortLink.find()
    List_of_Document=[]
    for i in doc:
        del i['_id']
        #print (i)
        List_of_Document.append(i)
    return List_of_Document


def updateWebLink(slug,newlink):
    """method update just web link """
    print ("update web link")
    retrievedlink = ShortLink.one (Q.slug==slug)
    #check  if there islink retrieved from db
    if (not retrievedlink ):
        return not_found("not found link")
    retrievedlink.web = newlink
    retrievedlink.update ()
    return successful_opr("update successfuly")


def updateIosfallbackLink(slug,newlink):
    """for update fallback in iphone """
    lk = ShortLink.one (Q.slug==slug)
    if (not lk):
        return not_found("not found link")
    else:
        lk.ios['fallback']=newlink
        lk.update()
        return successful_opr("update ios successfully")








