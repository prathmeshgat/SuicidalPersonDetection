__author__ = 'Prathmesh'
import os
import json
from os import path
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

class PNSentimentAnalyzer:
    docCount =0
    docSentiment = dict()
    docSet =list()

    def __init__(self, docCount):
        self.docCount = docCount

        self.prepareDocSet()

        self.calculateSentiment()

        self.displaySentiment()

    def __del__(self):
        print("destroyed")

    def readFromTextFile(self,TEXT_FILE):
        fp = open(TEXT_FILE, "r")
        t_file = fp.read()
        fp.close()
        return t_file

    def prepareDocSet(self):
        #prepare document Set
        for fileCount in range(1, self.docCount):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
            doc = self.readFromTextFile(TEXT_FILE)
            self.docSet.append(doc)

    def calculateSentiment(self):
        #calculate
        fileName =1
        for doc in self.docSet:
            # print(sentence)
            self.docSentiment[str(fileName)] = vaderSentiment(doc)
            fileName = fileName + 1
            # print("\n\t" + str(vs))

    def displaySentiment(self):
        print("\n\nResults for PN::\n")
        for item in self.docSentiment.keys():
            print("DocNumber "+item+"\n\t" + str(self.docSentiment[item]))

    def saveSentiment(self):
        return

class SuicideSentimentAnalyzer:
    docCount =0
    docSentiment = dict()
    docSet =list()

    def __init__(self, docCount):
        self.docCount = docCount

        self.prepareDocSet()

        self.calculateSentiment()

        self.displaySentiment()

    def __del__(self):
        print("destroyed")

    def readFromTextFile(self,TEXT_FILE):
        fp = open(TEXT_FILE, "r")
        t_file = fp.read()
        fp.close()
        return t_file

    def prepareDocSet(self):
        #prepare document Set
        for fileCount in range(1, self.docCount):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
            doc = self.readFromTextFile(TEXT_FILE)
            self.docSet.append(doc)

    def calculateSentiment(self):
        #calculate
        fileName =1
        for doc in self.docSet:
            # print(sentence)
            self.docSentiment[str(fileName)] = vaderSentiment(doc)
            fileName = fileName + 1
            # print("\n\t" + str(vs))

    def displaySentiment(self):
        print("\n\nResults for Suicidal::\n")
        for item in self.docSentiment.keys():
            print("DocNumber "+item+"\n\t" + str(self.docSentiment[item]))

    def saveSentiment(self):
        return

class CommentsPNSentimentAnalyzer:
    docCount =0
    docSentiment = dict()
    docSet =list()

    def __init__(self, docCount):
        self.docCount = docCount

        self.prepareDocSet()

        self.calculateSentiment()

        self.displaySentiment()

    def __del__(self):
        print("destroyed")

    def readFromTextFile(self,TEXT_FILE):
        fp = open(TEXT_FILE, "r")
        t_file = fp.read()
        fp.close()
        return t_file

    def prepareDocSet(self):
        #prepare document Set
        for fileCount in range(1, self.docCount):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
            doc = self.readFromTextFile(TEXT_FILE)
            self.docSet.append(doc)

    def calculateSentiment(self):
        #calculate
        fileName =1
        for doc in self.docSet:
            # print(sentence)
            self.docSentiment[str(fileName)] = vaderSentiment(doc)
            fileName = fileName + 1
            # print("\n\t" + str(vs))

    def displaySentiment(self):
        print("\n\nResults for PN::\n")
        for item in self.docSentiment.keys():
            print("DocNumber "+item+"\n\t" + str(self.docSentiment[item]))

    def saveSentiment(self):
        return

class CommentsSuicidalSentimentAnalyzer:
    docCount =0
    commentJson = dict()
    mcommentJson = dict()

    def __init__(self, docCount):
        self.docCount = docCount

        self.prepareDocSet()

        self.calculateSentiment()

        self.displaySentiment()

    def __del__(self):
        print("destroyed")

    def readFromTextFile(self,TEXT_FILE):
        fp = open(TEXT_FILE, "r")
        t_file = fp.read()
        self.commentJson = json.loads(t_file)
        fp.close()
        return t_file

    def analyzesentiment(self):
        #prepare document Set
        for fileCount in range(1, self.docCount):
            TEXT_FILE = path.join(os.pardir, "Resources/CommentsFiles/Suicidal/"+str(fileCount)+".txt")
            self.readFromTextFile(TEXT_FILE)
            self.calculateSentiment()
            self.saveSentiment(fileCount)

    def calculateSentiment(self):
        #calculate
        compound=0
        positive=0
        negative=0

        self.mcommentJson = {
                                "channelId":self.commentJson.channelId,
                                "videoId": self.commentJson.videoId,
                                "comments": list(),
                                "commentsCount":len(self.commentJson.comments),
                                "avrageCompoundSentiment":0.0,
                                "avragePositiveSentiment":0.0,
                                "avrageNegativeSentiment":0.0
                            }

        for item in self.commentJson["comments"]:
            # print(sentence)
            commentList = list()

            for item2 in item:
                tempJson = dict()
                tempsent = vaderSentiment(item2)
                tempJson={
                    "comment":item2,
                    "compound":tempsent["compound"],
                    "neg":tempsent["neg"],
                    "pos":tempsent["pos"],
                    "neu":tempsent["neu"]
                }

                commentList.append(tempJson)

            self.mcommentJson["comments"].append(commentList)
            # print("\n\t" + str(vs))

    def displaySentiment(self):
        print("\n\nResults for PN::\n")
        for item in self.docSentiment.keys():
            print("DocNumber "+item+"\n\t" + str(self.docSentiment[item]))

    def saveSentiment(self,fileCount):
        TEXT_FILE = path.join(os.path.dirname('C:/git/SuicidalPersonDetection/'), "Resources/CommentsFiles/Suicidal/"+str(fileCount)+".txt")
        fp = open(TEXT_FILE, "w")
        fp.write(json.dumps(self.mcommentJson))
        fp.close()
        return


#always documnet count is plus 1
suicudeSentimentList = SuicideSentimentAnalyzer(18)

#always documnet count is plus 1
personalNarrationSentimentList = PNSentimentAnalyzer(18)
