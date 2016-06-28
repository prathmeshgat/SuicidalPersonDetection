__author__ = 'Prathmesh'
import os
from os import path
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment


def fromTextFile(TEXT_FILE):
    fp = open(TEXT_FILE, "r")
    t_file = fp.read()
    fp.close()
    return t_file

def getPersonalNarrationDocSet():
    #prepare document Set
    doc_set = list()
    for fileCount in range(1, 17):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
            doc = fromTextFile(TEXT_FILE)
            doc_set.append(doc)
    return doc_set;

def getSuicidalDocSet():
    #prepare document Set
    doc_set = list()
    for fileCount in range(1, 27):
            TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
            doc = fromTextFile(TEXT_FILE)
            doc_set.append(doc)
    return doc_set;

def calculateSentiment(docSet):
    docSentiment = list()
    for doc in docSet:
        # print(sentence)
        docSentiment.append(vaderSentiment(doc))
        # print("\n\t" + str(vs))
    return docSentiment

def displaySentiment(sentiments):
    for item in sentiments:
        print("\n\t" + str(item))
    return

#get suicidal docs
suicidalDocs = getSuicidalDocSet()

#calculate sentiment per doc
docSentiment = calculateSentiment(suicidalDocs)

#display sentiment per doc
print("Suicidal docs::")
displaySentiment(docSentiment)

#get personal-narration docs
psersonalNarrationDocs = getPersonalNarrationDocSet()

#calculate sentiment per doc
docSentiment = calculateSentiment(psersonalNarrationDocs)

#display sentiment per doc
print("Personal Narration docs::")
displaySentiment(docSentiment)
