from pymongo import MongoClient
#   Database: ag-test-5163
#   User: kzynA
#   Password: kACkB64Me
#   MongoDB URI: mongodb://<dbuser>:<dbpassword>@ds019926.mlab.com:19926/ag-test-5163
#mongo ds019926.mlab.com:19926/ag-test-5163 -u kzynA -p kACkB64Me
#mongo mongodb://kzynA:kACkB64Me@ds019926.mlab.com:19926/ag-test-5163
#    # mongo --host=ds019926.mlab.com: --port=19926 --username kzynA --password kACkB64Me

uri = 'mongodb://127.0.0.1:27017/ag-test-5163'
client = MongoClient(uri)
db = client['ag-test-5163']
DEBUG = True

