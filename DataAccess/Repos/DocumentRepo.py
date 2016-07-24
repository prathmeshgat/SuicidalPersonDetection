__author__ = 'Prathmesh'

import json
import DataAccess.Models.Document as Model
from pymongo import MongoClient

class DocumentRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.DocumentSet

    def insert(self,document):
        _dict = document.__dict__
        del _dict["_id"]
        result = self.collection.insert(_dict)
        return result

    def object_decoder(self,obj):
        return Model.Document(obj['documentId'],obj['transcript'],obj['category'],obj['_id'],obj['nnFraction'],obj['vbFration'],
                            obj['advFraction'],obj['prp1Fraction'],obj['prp2Fraction'],
                            obj['cleanedToken'],obj['posSentiment'],obj['negSentiment'],obj['neuSentiment'],
                            obj['compoundSentiment'],obj['custom1'],obj['custom2'],
                            obj['custom3'],obj['custom4'],obj['custom5'])

    def get(self,Id,category):
        document = self.collection.find_one({"documentId": Id,"category":category})

        return self.object_decoder(document)

    def getSuicidalDocSet(self):
        documentSet = self.collection.find({"category": "S"})
        docList = list()
        for doc in documentSet:
            docList.append(self.object_decoder(doc))
        return docList

    def getPersonalNarrationDocSet(self):
        documentSet = self.collection.find({"category": "PN"})
        docList = list()
        for doc in documentSet:
            docList.append(self.object_decoder(doc))
        return docList

    def getAvrageSentiment(self):
        cursor = self.collection.aggregate(
            [
                {
                    "$group":
                        {
                            "_id":"$category",
                            "compoundSentimentAvrage": {"$avg":"$compoundSentiment"},
                            "posSentimentAvrage": {"$avg":"$posSentiment"},
                            "negSentimentAvrage": {"$avg":"$negSentiment"},
                            "neupoundSentimentAvrage": {"$avg":"$neuSentiment"}
                        }
                }
            ]
        )

        sentimentList = list()

        for item in cursor:
            sentimentList.append(item)

        return sentimentList

    def delete(self,Id,category):
       result = self.collection.delete_many({"documentId": Id,"category":category})
       return result.deleted_count

    def cleanCollection(self):
       self.collection.drop()

    def getAll(self):
        documentSet = self.collection.find()
        docList = list()
        for doc in documentSet:
            docList.append(self.object_decoder(doc))
        return docList

    def update(self,document):
        id =document._id
        _dict = document.__dict__
        del _dict["_id"]
        result = self.collection.replace_one(
            {"_id": id},
            _dict
        )
        return result.matched_count