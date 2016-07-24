__author__ = 'Prathmesh'

import json
import DataAccess.Models.Comment as Model
from pymongo import MongoClient

class CommentRepo:
    def __init__(self):

        self.client = MongoClient('localhost', 27017)

        self.db = self.client.coreData

        self.collection = self.db.CommentsSet

    def insert(self,comment):
        result = self.collection.insert(comment.__dict__)
        return result

    def object_decoder(self,obj):
        return Model.Comment(obj['_id'],obj['documentId'],obj['text'],obj['category'],obj['channelId'],obj['videoId'],obj['nnFraction'],obj['vbFration'],
                            obj['advFraction'],obj['prp1Fraction'],obj['prp2Fraction'],
                            obj['cleanedToken'],obj['posSentiment'],obj['negSentiment'],obj['neuSentiment'],
                            obj['compoundSentiment'],obj['custom1'],obj['custom2'],
                            obj['custom3'],obj['custom4'],obj['custom5'])

    def get(self,Id):
        comment = self.collection.find_one({"_id": Id})

        return self.object_decoder(comment)

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

    def getSuicidalCommentSet(self):
        commentSet = self.collection.find({"category": "S"})
        commentList = list()
        for comment in commentSet:
            commentList.append(self.object_decoder(comment))
        return commentList

    def getPersonalNarrationCommentSet(self):
        commentSet = self.collection.find({"category": "PN"})
        commentList = list()
        for comment in commentSet:
            commentList.append(self.object_decoder(comment))
        return commentList

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
        temp =comment.__dict__
        _dict = {key: value for key, value in temp.items() if value is not "_id"}
        result = self.collection.replace_one(
            {"_id": id},
            _dict
        )
        return result.matched_count