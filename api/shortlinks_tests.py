import unittest
from app import app
import json


class ShortLinkTestCase (unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    def test_nonAuth(self):
        """ non authorized user request """
        rv =self.app.get('/shortlinks',headers={'Content-Type': 'application/json'})
        #print (rv.data)
    def test_nonJSON (self):
        re= self.app.get ('/shortlinks',headers={'Authorization':'Basic YWRtaW46YWRtaW4='})
        #print (re.data)
    def JSONReqAuth (self):
         """add  content type : application-json and  authorizaton :encode (user,pass)"""
         authorizedUser = {"user": "admin", "password": "admin"}
         headers = {'Content-Type': 'application/json', 'Authorization':'Basic YWRtaW46YWRtaW4='}
         return headers
    def test_JSONAuthRequestGet(self):
        """send json request get method"""
        resp= self.app.get ('/shortlinks',headers=self.JSONReqAuth() )
        #print (resp.data)
    def test_POST(self):
        response= self.app.post ('/shortlinks')
        #print (response.data)
    def test_AuthPost(self):

        myresp = self.app.post ('/shortlinks',headers={'Authorization':'Basic YWRtaW46YWRtaW4='})
        print (myresp.data)
    def test_AuthJsonPost(self):
        """trigger new post request create and add new shortlink document in collection """
        NewSH={
        "slug": "s5G1f3",
        "ios": {
        "primary": "IOSPRIMARY16",
        "fallback": "FALLBACKIOS16"
        },
        "android": {
        "primary": "ANDpRIMARY16",
        "fallback": "andFALLBACK16"
        },
        "web": "WEB16"
        }
        myheaders= { 'Content-Type':'application/json','Authorization':'Basic YWRtaW46YWRtaW4='}
        #myresp = self.app.post('/shortlinks',data=json.dumps (NewSH),headers=myheaders)
        #print (myresp.data)






if (__name__=='__main__'):
    unittest.main ()
    
