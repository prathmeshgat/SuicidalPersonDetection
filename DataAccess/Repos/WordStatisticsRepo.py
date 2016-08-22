__author__ = 'Prathmesh'

import pymongo
import DataAccess.Models.WordStatistics as Model
from pymongo import MongoClient


class WordStatisticsRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.WordStatistics

    def insert(self,document):
        _dict = document.__dict__
        del _dict["_id"]
        result = self.collection.insert_one(_dict)
        return result

    def object_decoder(self,obj):
        return Model.WordStatistics(obj['word'],obj['happinessScore'],
                                    obj['suicidalCorpusCount'],obj['personalNarrationCorpusCount'],
                                    obj['difference'],obj['pctHappinessShiftPN'],obj['pctHappinessShiftSui'],obj['_id'])

    def get(self,word):
        document = self.collection.find_one({"word": word})

        return self.object_decoder(document)

    def delete(self,word):
       result = self.collection.delete_many({"word": word})
       return result.deleted_count

    def cleanCollection(self):
       self.collection.drop()

    def getAll(self):
        wordSet = self.collection.find().sort([("difference", -1)])
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