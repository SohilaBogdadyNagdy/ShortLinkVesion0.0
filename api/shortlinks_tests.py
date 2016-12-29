import unittest
from app import app


class ShortLinkTestCase (unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    def test_nonAuth(self):
        """ non authorized user request """
        rv =self.app.get('/shortlinks',headers={'Content-Type': 'application/json'})
        print (rv.data)
    def test_nonJSON (self):
        re= self.app.get ('/shortlinks',headers={'Authorization':'Basic YWRtaW46YWRtaW4='})
        print (re.data)
    def JSONReqAuth (self):
         """add  content type : application-json and  authorizaton :encode (user,pass)"""
         authorizedUser = {"user": "admin", "password": "admin"}
         headers = {'Content-Type': 'application/json', 'Authorization':'Basic YWRtaW46YWRtaW4='}
         return headers
    def test_JSONAuthRequestGet(self):
        """send json request get method"""
        resp= self.app.get ('/shortlinks',headers=self.JSONReqAuth() )
        print (resp.data)




if (__name__=='__main__'):
    unittest.main ()
    
