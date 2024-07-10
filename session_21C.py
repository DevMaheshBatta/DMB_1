from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDBHelper:

    def __init__(self, collection="users"):
        uri = "mongodb+srv://DevMahesh:devmahesh09@cluster0.iaylwlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Only if you face SSL error
       

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Only if you face SSL error, add -> tlsCAFile=ca
       

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        # Get reference to the database
        self.db = client['GWPDS']
        self.collection = self.db[collection]

    def insert(self, document):
        result= self.collection.insert_one(document)
        print("Document inserted in Collection:", self.collection.name)
        print("result is:",result)
        return result
    def fetch(self, query=""):
        documents = self.collection.find(query)
        return list(documents)
    

    def delete(self,query=""):
        result=self.collection.find(query)
        print("result is:",result)

    def update(self,document,query):
        document_to_update={'$set':document}
        result=self.collection.update_one(query,document_to_update)
        print("result is;",result)