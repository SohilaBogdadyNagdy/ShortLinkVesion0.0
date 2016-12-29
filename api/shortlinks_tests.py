import unittest
from app import app


class ShortLinkTestCase (unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        #app.config['TESTING'] = True
        self.app = app.test_client()
       # with flaskr.app.app_context():
        #    flaskr.init_db()
    def test_empty_doc(self):
        rv =self.app.get('/shortlinks',follow_redirects=True)
        #print (rv.data)
    def JSONReq (self):
         authorizedUser = {"user": "admin", "password": "admin"}
         headers = {'Content-Type': 'application/json'}
         return headers
    def test_JSONRequestGet(self):
        """send json request get method"""
        resp= self.app.get ('/shortlinks',headers=self.JSONReq() )
        print (resp.data)



if (__name__=='__main__'):
    unittest.main ()
    
