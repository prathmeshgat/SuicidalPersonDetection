__author__ = 'Prathmesh'

import json
import DataAccess.Models.SuicidalDocument as Model
from pymongo import MongoClient

class SuicidalDocumentRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.SuicidalDocumentSet

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

    def get(self,Id):
        document = self.collection.find_one({"documentId": Id})

        return self.object_decoder(document)

    def getAvrageSentiment(self):
        cursor = self.collection.aggregate(
            [
                {
                    "$group":
                        {
                            "_id":None,
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

    def delete(self,Id):
       result = self.collection.delete_many({"documentId": Id})
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