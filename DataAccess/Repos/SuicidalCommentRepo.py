__author__ = 'Prathmesh'

import json
import DataAccess.Models.SuicidalComment as Model
from pymongo import MongoClient

class SuicidalCommentRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.SuicidalCommentsSet

    def insert(self,comment):
        _dict = comment.__dict__
        del _dict["_id"]
        result = self.collection.insert(_dict)
        return result

    def object_decoder(self,obj):
        return Model.SuicidalComment(
                            obj['documentId'],obj['text'],obj['category'],obj['channelId'],obj['videoId'],obj['ownerUserName'],obj['_id'],
                            obj['pastTenseFraction'],obj['presentTenseFraction'],
                            obj['futureTenseFraction'],obj['advFraction'],
                            obj['adjFraction'],obj['pronounFraction'],
                            obj['nounFraction'],obj['vbFration'],
                            obj['cleanedToken'],obj['posSentiment'],
                            obj['negSentiment'],obj['neuSentiment'],
                            obj['compoundSentiment'])

    def get(self,Id):
        comment = self.collection.find_one({"_id": Id})
        if(comment is not None):
            return self.object_decoder(comment)
        return None;

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


    def delete(self,Id):
       result = self.collection.delete_many({"_id": Id})
       return result.deleted_count

    def cleanCollection(self):
       self.collection.drop()

    def getAll(self):
        commentSet = self.collection.find()
        commentList = list()
        for comment in commentSet:
            commentList.append(self.object_decoder(comment))
        return commentList

    def update(self,comment):
        id =comment._id
        _dict = comment.__dict__
        del _dict["_id"]
        result = self.collection.replace_one(
            {"_id": id},
            _dict
        )
        return result.matched_count