__author__ = 'Prathmesh'
from pymongo import MongoClient
import DataAccess.Models.Document as DA
import DataAccess.Utils.Container as Utils
import os
from os import path
import Source.POSTagging as pos
import Source.SentimentAnalysis as SA
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
    container.DocumentRepo.cleanCollection()

    for fileCount in range(1, 18):
        if fileCount!= 14:
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
            fp = open(TEXT_FILE, "r")
            data = fp.read()
            fp.close()

            tagger = pos.POSTagger(data)
            res = tagger.getFractions()

            sentiments = SA.SentimentAnalyzer.calculateSentiment(data)

            Doc = DA.Document(fileCount,
                              data,
                              "S",
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

            print(container.DocumentRepo.insert(Doc))

    id = 18
    for fileCount in range(1, 18):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
            fp = open(TEXT_FILE, "r")
            data = fp.read()
            fp.close()

            tagger = pos.POSTagger(data)
            res = tagger.getFractions()

            sentiments = SA.SentimentAnalyzer.calculateSentiment(data)

            Doc = DA.Document(id,
                              data,
                              "PN",
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

            print(container.DocumentRepo.insert(Doc))
            id = id +1



container = Utils.Container()
res = container.DocumentRepo.getSuicidalDocSet()
docSet = list()
for item in res:
    docSet.append(item.__dict__["transcript"])

topicsModel = TM.TopicModelling(docSet,5,3,10)
print(topicsModel.getTopics())