__author__ = 'Prathmesh'

import json
import DataAccess.Models.HappinessScore as Model
from pymongo import MongoClient

class HappinessScoreRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.HedonometerDataset

    def insert(self,document):
        _dict = document.__dict__
        del _dict["_id"]
        result = self.collection.insert_one(_dict)
        return result

    def object_decoder(self,obj):
        return Model.HappinessScore(obj['language'],obj['word'],obj['happinessScore'],obj['englishWord'],obj['_id'])

    def get(self,word):
        document = self.collection.find_one({"word": word})

        return self.object_decoder(document)



    def delete(self,word):
       result = self.collection.delete_many({"word": word})
       return result.deleted_count

    def cleanCollection(self):
       self.collection.drop()

    def getAll(self):
        wordSet = self.collection.find({"language": "english"})
        wordList = list()
        for doc in wordSet:
            wordList.append(self.object_decoder(doc))
        return wordList

    def update(self,word):
        id =word._id
        _dict = word.__dict__
        del _dict["_id"]
        result = self.collection.replace_one(
            {"_id": id},
            _dict
        )
        return result.matched_count