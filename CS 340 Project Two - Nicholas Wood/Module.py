from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        #Initializing the MonogoClient. This helps to
        #access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:50438' % (username, password))
        self.database = self.client['AAC']

       
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, becasue data parameter is empty")
            return False
    
    def readAll(self, data):
        #checking to see if the data is empty of not
        if data is not None:
             return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to find, becasuse data parameter is empty")
            return False
        
    def update(self, data, change):
        #checking to see if data exist and then updating the database
        if data is not None:
            return self.database.animals.update(data,{"$set": change})
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return False
        
    def delete(self, data):
        #checking to see if data exist and then deleting it from the database 
        if data is not None:
            return self.database.animals.delete_one(data)
        else:
            raise Exception("Nothing to delete, becasuse data parameter is empty")
            return False