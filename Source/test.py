__author__ = 'Prathmesh'
from pymongo import MongoClient
import DataAccess.Models.SuicidalDocument as DA
import DataAccess.Models.SuicidalComment as DA1
import DataAccess.Models.PersonalNarrationDocument as DA2
import DataAccess.Models.PersonalNarrationComment as DA3
import DataAccess.Utils.Container as Utils
import os
from os import path
import Source.POSTagging as pos
import Source.SentimentAnalysis as SA
import json
from bson.objectid import ObjectId

import Source.TopicModelling as TM
# Doc = DA.Document(1,"titu","S")
#
# container = Utils.Container()
#
# print(container.DocumentRepo.insert(Doc))
#
# res = container.DocumentRepo.getAll()
# for item in res:
#     print(item.__dict__)
#
# Doc.transcript="updated"
# print(container.DocumentRepo.update(Doc))
#
#
# res = container.DocumentRepo.getAll()
# for document in res:
#     print(document.__dict__)
#
# res = container.DocumentRepo.delete(1)
#
# print(res)
# res = container.DocumentRepo.getAll()
# for item in res:
#     print(item.__dict__)

def CreateDB():
    container = Utils.Container()
    container.PersonalNarrationDocumentRepo.cleanCollection()

    for fileCount in range(1, 18):
        if fileCount!= 14:
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
            fp = open(TEXT_FILE, "r")
            data = fp.read()
            fp.close()

            tagger = pos.POSTagger(data)
            res = tagger.getFractions()

            sentiments = SA.SentimentAnalyzer.calculateSentiment(data)

            Doc = DA.SuicidalDocument(fileCount,
                              data,
                              "S",
                              -1,
                              res["nnFraction"],
                              res["vbFration"],
                              res["advFraction"],
                              res["prp1Fraction"],
                              res["prp2Fraction"],
                              res["cleanedToken"],
                              sentiments["pos"],
                              sentiments["neg"],
                              sentiments["neu"],
                              sentiments["compound"])

            print(container.SuicidalDocumentRepo.insert(Doc))

    for fileCount in range(1, 18):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
            fp = open(TEXT_FILE, "r")
            data = fp.read()
            fp.close()

            tagger = pos.POSTagger(data)
            res = tagger.getFractions()

            sentiments = SA.SentimentAnalyzer.calculateSentiment(data)

            Doc = DA2.PersonalNarrationDocument(fileCount,
                              data,
                              "PN",
                              -1,
                              res["nnFraction"],
                              res["vbFration"],
                              res["advFraction"],
                              res["prp1Fraction"],
                              res["prp2Fraction"],
                              res["cleanedToken"],
                              sentiments["pos"],
                              sentiments["neg"],
                              sentiments["neu"],
                              sentiments["compound"])

            print(container.PersonalNarrationDocumentRepo.insert(Doc))

# CreateDB()

# container = Utils.Container()
# res = container.DocumentRepo.getSuicidalDocSet()
# docSet = list()
# for item in res:
#     docSet.append(item.__dict__["transcript"])
#
# topicsModel = TM.TopicModelling(docSet,5,3,10)
# print(topicsModel.getTopics())


def CreateCommentsDB():
    container = Utils.Container()
    container.SuicidalCommentRepo.cleanCollection()

    for fileCount in range(1, 18):
        if fileCount!= 14:
            TEXT_FILE = path.join(os.pardir, "Resources/CommentsFiles/Suicidal/"+str(fileCount)+".txt")
            fp = open(TEXT_FILE, "r")
            data = fp.read()
            fp.close()
            comments = json.loads(data)


            for comment in comments["comments"].values():
                for item in comment:

                    tagger = pos.POSTagger(item)
                    res = tagger.getFractions()
                    sentiments = SA.SentimentAnalyzer.calculateSentiment(item)

                    tcomment = DA1.SuicidalComment(fileCount,
                                      item,
                                      "S",
                                      comments["channelId"],
                                      comments["videoId"],
                                      -1,
                                      res["nnFraction"],
                                      res["vbFration"],
                                      res["advFraction"],
                                      res["prp1Fraction"],
                                      res["prp2Fraction"],
                                      res["cleanedToken"],
                                      sentiments["pos"],
                                      sentiments["neg"],
                                      sentiments["neu"],
                                      sentiments["compound"])

                    print(container.SuicidalCommentRepo.insert(tcomment))
                    # print(count)

# CreateCommentsDB()

container = Utils.Container()
res = container.PersonalNarrationDocumentRepo.getAll()
# print(res)
for item in res:
    print(item.__dict__)

