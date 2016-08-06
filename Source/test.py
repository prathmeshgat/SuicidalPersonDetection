__author__ = 'Prathmesh'
import pprint
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
import Source.TopicModelling as TM
import Source.BagOfWords as BG
import Source.TagCloud as TG
from bson.objectid import ObjectId



def topicModellingSuicidalComments():
    container = Utils.Container()
    res = container.SuicidalCommentRepo.getAll()

    commentSet = list()
    for item in res:
        commentSet.append(item.text)

    topicsModel = TM.TopicModelling(commentSet,50,3,10)
    print("No of comments::"+ str(len(commentSet)))
    topics =topicsModel.getTopics()
    for item in topics:
        print("\n")
        print(item)

def frequentWordsSuicidalComments():
    container = Utils.Container()
    res = container.SuicidalCommentRepo.getAll()

    commentSet = list()
    for item in res:
        commentSet.append(item.text)

    model = BG.BagOfWords(commentSet,100)
    print("No of comments::"+ str(len(commentSet)))
    wordList = model.topFrequentWords()
    for item in wordList:
        print("\n")
        print(item)

def topicModellingPNComments():
    container = Utils.Container()
    res = container.PersonalNarrationCommentRepo.getAll()

    commentSet = list()
    for item in res:
        commentSet.append(item.text)

    topicsModel = TM.TopicModelling(commentSet,20,3,10)
    print("No of comments::"+ str(len(commentSet)))
    topics =topicsModel.getTopics()
    for item in topics:
        print("\n")
        print(item)

def frequentWordsPNComments():
    container = Utils.Container()
    res = container.PersonalNarrationCommentRepo.getAll()

    commentSet = list()
    for item in res:
        commentSet.append(item.text)

    model = BG.BagOfWords(commentSet,100)
    print("No of comments::"+ str(len(commentSet)))
    wordList = model.topFrequentWords()
    for item in wordList:
        print("\n")
        print(item)

def topicModellingPNDocs():
    container = Utils.Container()
    res = container.PersonalNarrationDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    topicsModel = TM.TopicModelling(docSet,5,3,10)
    print("No of documents::"+ str(len(docSet)))
    topics =topicsModel.getTopics()
    for item in topics:
        print("\n")
        print(item)

def frequentWordsPNDocs():
    container = Utils.Container()
    res = container.PersonalNarrationDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    model = BG.BagOfWords(docSet,100)
    print("No of Docs::"+ str(len(docSet)))
    wordList = model.topFrequentWords()
    for item in wordList:
        print("\n")
        print(item)

def topicModellingSuicidalDocs():
    container = Utils.Container()
    res = container.SuicidalDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    topicsModel = TM.TopicModelling(docSet,5,3,10)
    print("No of documents::"+ str(len(docSet)))
    topics =topicsModel.getTopics()
    for item in topics:
        print("\n")
        print(item)

def frequentWordsSuicidalDocs():
    container = Utils.Container()
    res = container.SuicidalDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    model = BG.BagOfWords(docSet,100)
    print("No of Docs::"+ str(len(docSet)))
    wordList = model.topFrequentWords()
    for item in wordList:
        print("\n")
        print(item)

def tagCloudSuicidalDocs():
    container = Utils.Container()
    res = container.SuicidalDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    model = TG.TagCloud(docSet)
    model.tagCloud()

def CreateDB():
    container = Utils.Container()
    container.SuicidalDocumentRepo.cleanCollection()

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

    container.PersonalNarrationDocumentRepo.cleanCollection()
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


            for comment in comments["comments"].keys():
                for item in comments["comments"][comment]:

                    tagger = pos.POSTagger(item)
                    res = tagger.getFractions()
                    sentiments = SA.SentimentAnalyzer.calculateSentiment(item)

                    tcomment = DA1.SuicidalComment(fileCount,
                                      item,
                                      "S",
                                      comments["channelId"],
                                      comments["videoId"],
                                      comment,
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

def crudSuicidalDocs():

    container = Utils.Container()

    #create
    Doc = DA.SuicidalDocument(50,"titu","S")
    print(container.SuicidalDocumentRepo.insert(Doc))

    #retrive
    res = container.SuicidalDocumentRepo.get(50)
    print(res.__dict__)

    #update
    Doc.transcript="updated"
    print(container.SuicidalDocumentRepo.update(Doc))
    res = container.SuicidalDocumentRepo.get(50)
    print(res.__dict__)

    #delete
    res = container.SuicidalDocumentRepo.delete(50)
    print(res)

    container = Utils.Container()
    res = container.SuicidalDocumentRepo.getAll()
    for item in res:
        print(item.__dict__)

def crudSuicidalComments():

    container = Utils.Container()

    #create
    Doc = DA1.SuicidalComment(50,"titu","S","CH123","V123","U123")
    id = container.SuicidalCommentRepo.insert(Doc)
    print(id)

    # retrive
    res = container.SuicidalCommentRepo.get(ObjectId(id))
    print(res.__dict__)

    #update
    Doc.text="updated"
    Doc._id = ObjectId(id)
    print(container.SuicidalCommentRepo.update(Doc))
    res = container.SuicidalCommentRepo.get(ObjectId(id))
    print(res.__dict__)

    #delete
    res = container.SuicidalCommentRepo.delete(ObjectId(id))
    print(res)

    res = container.SuicidalCommentRepo.get(ObjectId(id))
    print(res)

def crudPNComments():

    container = Utils.Container()

    #create
    Doc = DA3.PersonalNarrationComment(50,"titu","S","CH123","V123","U123")
    id = container.PersonalNarrationCommentRepo.insert(Doc)
    print(id)

    # retrive
    res = container.PersonalNarrationCommentRepo.get(ObjectId(id))
    print(res.__dict__)

    #update
    Doc.text="updated"
    Doc._id = ObjectId(id)
    print(container.PersonalNarrationCommentRepo.update(Doc))
    res = container.PersonalNarrationCommentRepo.get(ObjectId(id))
    print(res.__dict__)

    #delete
    res = container.PersonalNarrationCommentRepo.delete(ObjectId(id))
    print(res)

    res = container.PersonalNarrationCommentRepo.get(ObjectId(id))
    print(res)

def crudPNDocs():

    container = Utils.Container()

    #create
    Doc = DA2.PersonalNarrationDocument(50,"titu","PN")
    print(container.PersonalNarrationDocumentRepo.insert(Doc))

    #retrive
    res = container.PersonalNarrationDocumentRepo.get(50)
    print(res.__dict__)

    #update
    Doc.transcript="updated"
    print(container.PersonalNarrationDocumentRepo.update(Doc))
    res = container.PersonalNarrationDocumentRepo.get(50)
    print(res.__dict__)

    #delete
    res = container.PersonalNarrationDocumentRepo.delete(50)
    print(res)

    container = Utils.Container()
    res = container.PersonalNarrationDocumentRepo.getAll()
    for item in res:
        print(item.__dict__)

def avgSentimentComments():
    container = Utils.Container()

    res = container.SuicidalDocumentRepo.getAvrageSentiment()
    print("\nAverage Sentiment Suicidal docs::\n")
    print(res)

    res = container.PersonalNarrationDocumentRepo.getAvrageSentiment()
    print("\nAverage Sentiment PN docs::\n")
    print(res)

    res = container.SuicidalCommentRepo.getAvrageSentiment()
    print("\nAverage Sentiment Suicidal Comments::")
    print(res)

    res = container.PersonalNarrationCommentRepo.getAvrageSentiment()
    print("\nAverage Sentiment PN Comment::")
    print(res)


# frequentWordsSuicidalDocs()

# topicModellingSuicidalDocs()

# frequentWordsSuicidalComments()

# topicModellingSuicidalComments()

# frequentWordsPNDocs()

# topicModellingPNDocs()

# frequentWordsPNComments()

# topicModellingPNComments()

# avgSentimentComments()

# crudSuicidalDocs()

# crudPNDocs()

# crudSuicidalComments()

# crudPNComments()

# CreateDB()

# CreateCommentsDB()

# tagCloudSuicidalDocs()

# pp = pprint.PrettyPrinter(indent=4)
# container = Utils.Container()
# # container.PersonalNarrationCommentRepo.cleanCollection()
# res = container.SuicidalDocumentRepo.getAll()
# count =0
# for item in res:
#     print("\n")
#     pp.pprint(item.__dict__)
#     count = count +1
# print("Count::"+str(count))


