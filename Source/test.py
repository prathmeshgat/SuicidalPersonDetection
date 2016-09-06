__author__ = 'Prathmesh'
import pprint
import csv
import xlrd
import DataAccess.Models.SuicidalDocument as DA
import DataAccess.Models.SuicidalComment as DA1
import DataAccess.Models.PersonalNarrationDocument as DA2
import DataAccess.Models.PersonalNarrationComment as DA3
import DataAccess.Models.HappinessScore as DA4
import DataAccess.Models.WordStatistics as DA5
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

    topicsModel = TM.TopicModelling(commentSet,50,3,10,"SuicidalComments.html")
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

    topicsModel = TM.TopicModelling(commentSet,20,3,10,"PNComments.html")
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

    topicsModel = TM.TopicModelling(docSet,5,3,10,"PNDocs.html")
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
    count =0
    for item in wordList:
        print("\n")
        print(item)
        count = count +1
    print(count)

def topicModellingSuicidalDocs():
    container = Utils.Container()
    res = container.SuicidalDocumentRepo.getAll()

    docSet = list()
    for item in res:
        docSet.append(item.transcript)

    topicsModel = TM.TopicModelling(docSet,5,3,10,"SuicidalDocs.html")
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

            Doc = DA.SuicidalDocument(
                              fileCount,
                              data,
                              "S",
                              -1,
                              res['pastTenseFraction'],
                              res['presentTenseFraction'],
                              res['futureTenseFraction'],
                              res['advFraction'],
                              res['adjFraction'],
                              res['pronounFraction'],
                              res['nounFraction'],
                              res['vbFration'],
                              res['cleanedToken'],
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

            Doc = DA2.PersonalNarrationDocument(
                              fileCount,
                              data,
                              "PN",
                              -1,
                              res['pastTenseFraction'],
                              res['presentTenseFraction'],
                              res['futureTenseFraction'],
                              res['advFraction'],
                              res['adjFraction'],
                              res['pronounFraction'],
                              res['nounFraction'],
                              res['vbFration'],
                              res['cleanedToken'],
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


            for user in comments["comments"].keys():
                for item in comments["comments"][user]:

                    tagger = pos.POSTagger(item)
                    res = tagger.getFractions()
                    sentiments = SA.SentimentAnalyzer.calculateSentiment(item)

                    tcomment = DA1.SuicidalComment(
                                      fileCount,
                                      item,
                                      "S",
                                      comments["channelId"],
                                      comments["videoId"],
                                      user,
                                      -1,
                                      res['pastTenseFraction'],
                                      res['presentTenseFraction'],
                                      res['futureTenseFraction'],
                                      res['advFraction'],
                                      res['adjFraction'],
                                      res['pronounFraction'],
                                      res['nounFraction'],
                                      res['vbFration'],
                                      res['cleanedToken'],
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

def create_hedenometerDataset():

    container = Utils.Container()
    container.HappinessScoreRepo.cleanCollection()

    filePath = path.join(os.pardir, "Resources/1.xlsx")
    xl_workbook = xlrd.open_workbook(filePath)
    xl_sheet = xl_workbook.sheet_by_index(0)
    print ('Sheet name: %s' % xl_sheet.name)

    # Print all values, iterating through rows and columns
    num_cols = xl_sheet.ncols   # Number of columns
    item = DA4.HappinessScore(1,2,3,4,5)
    for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
        # print ('-'*40)
        print ('Row: %s' % row_idx)   # Print row number
        tempList = list()

        for col_idx in range(0, num_cols):  # Iterate through columns
            cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            tempList.append(cell_obj)
            # print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        if(tempList[0].value == "english"):
            item.language = tempList[0].value
            item.word = tempList[1].value.replace(" ", "")
            item.happinessScore = tempList[2].value
            item.englishWord = tempList[3].value.replace(" ", "")
            print(container.HappinessScoreRepo.insert(item))
            print("\n"+item.word)
        # print(tempList)

def createWordStatDB():
    container = Utils.Container()
    container.WordStatisticsRepo.cleanCollection()

    SwordDict = dict()
    PNwordDict = dict()

    wordStatObj = DA5.WordStatistics("a",10,12,12,0,0,0)

    SDocSetCursor = container.SuicidalDocumentRepo.getAll()
    SdocSet = list()

    for item in SDocSetCursor:
        SdocSet.append(item.transcript)

    model1 = BG.BagOfWords(SdocSet,-1)
    SwordDict = model1.wordFrequency()

    PNDocSetCursor = container.PersonalNarrationDocumentRepo.getAll()
    PNdocSet = list()

    for item in PNDocSetCursor:
        PNdocSet.append(item.transcript)

    model2 = BG.BagOfWords(PNdocSet,-1)
    PNwordDict = model2.wordFrequency()

    hedenometerCursor = container.HappinessScoreRepo.getAll()
    for item in hedenometerCursor:
        wordStatObj.word = item.word
        wordStatObj.happinessScore = item.happinessScore
        wordStatObj.personalNarrationCorpusCount = (PNwordDict[item.englishWord.lower()] if (item.englishWord.lower() in PNwordDict.keys()) else 0)
        wordStatObj.suicidalCorpusCount = (SwordDict[item.englishWord.lower()] if (item.englishWord.lower() in SwordDict.keys()) else 0)
        wordStatObj.difference = abs(wordStatObj.personalNarrationCorpusCount - wordStatObj.suicidalCorpusCount)
        print(container.WordStatisticsRepo.insert(wordStatObj))

def getAvrageHappinessScoreSuicidalDocs():
    container = Utils.Container()

    res = container.WordStatisticsRepo.getAll()
    happinessValue = 0
    count = 0
    for item in res:
        happinessValue = happinessValue + (item.happinessScore *item.suicidalCorpusCount)
        count = count +item.suicidalCorpusCount

    print("Count::"+str(happinessValue/count))
    return (happinessValue/count)

def getAvrageHappinessScorePNDocs():
    container = Utils.Container()

    res = container.WordStatisticsRepo.getAll()
    happinessValue = 0
    count = 0
    for item in res:
        happinessValue = happinessValue + (item.happinessScore * item.personalNarrationCorpusCount)
        count = count + item.personalNarrationCorpusCount

    print("Count::"+str(happinessValue/count))
    return (happinessValue/count)

def calculatePctHappinessShiftDocs():
    CN = getAvrageHappinessScorePNDocs()
    CS = getAvrageHappinessScoreSuicidalDocs()
    pp = pprint.PrettyPrinter(indent=4)
    container = Utils.Container()
    res = container.WordStatisticsRepo.getAll()
    count =0
    for item in res:
        print("\n")
        if(item.personalNarrationCorpusCount!=0):
            item.pctHappinessShiftPN = ((item.happinessScore-CN)/(CN))*100.0
        else:
            item.pctHappinessShiftPN =0.0

        if(item.suicidalCorpusCount!=0):
            item.pctHappinessShiftSui = ((item.happinessScore-CS)/(CS))*100.0
        else:
            item.pctHappinessShiftSui =0

        container.WordStatisticsRepo.update(item)

        if(item.difference!=0):
            pp.pprint(item.__dict__)
            count = count +1
            # if(count==50):
            #     break
    print("Count::"+str(count))

def createwordChartCSV():
    CSV_FILE = path.join(os.pardir, "Resources/chart.csv")
    csvfile = open(CSV_FILE, 'w')
    fieldnames = ['Word','Value']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=fieldnames)
    writer.writeheader()
    graphList = list()
    pp = pprint.PrettyPrinter(indent=4)
    container = Utils.Container()
    res = container.WordStatisticsRepo.getAll()
    count =0
    for item in res:
        print("\n")
        pp.pprint(item.__dict__)
        if(item.difference!=0):
            count = count +1

            if(item.suicidalCorpusCount>item.personalNarrationCorpusCount):
                side = "right"
                arrow = "up"
                value = abs(item.pctHappinessShiftSui)
            else:
                side= "left"
                arrow ="down"
                value = -(abs(item.pctHappinessShiftSui))
            if(item.pctHappinessShiftSui>0):
                color = "yellow"
            else:
                color= "blue"

            word = item.englishWord
            graphList.append(
                {'word':word,
                 'value':value,
                 'arrowDirection':arrow,
                 'color':color,
                 'side':side
                 })
            writer.writerow({'Word': word, 'Value': value})
            if(count==50):
                break
    print("Count::"+str(count))

    for item in graphList:
        print("\n")
        pp.pprint(item)


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

# create_hedenometerDataset()

# tagCloudSuicidalDocs()

# createWordStatDB()

# getAvrageHappinessScorePNDocs()

# getAvrageHappinessScoreSuicidalDocs()

# calculatePctHappinessShiftDocs()

# createwordChartCSV()

# pp = pprint.PrettyPrinter(indent=4)
# container = Utils.Container()
# res = container.HappinessScoreRepo.getAll()
# count =0
# for item in res:
#     # print("\n")
#     if(item.word == "without"):
#         count = count +1
#     pp.pprint(item.__dict__)
#     # count = count +1
# print("Count::"+str(count))




