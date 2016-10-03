__author__ = 'Prathmesh'

import os
import nltk
import csv
from nltk import pos_tag, word_tokenize
from os import path

class POSTagger:
    def __init__(self,textData):
        self.textData = textData

    def getTaggedTokens(self):
        text = word_tokenize(self.textData)
        #print(text)
        #print("LENGTH of tagged::"+str(len(nltk.pos_tag(text)))+"\n"+"LENGTH of text file tokens::"+str(len(text)))
        #print(nltk.pos_tag(text))
        return(nltk.pos_tag(text))

    def getFractions(self):
        tagged_tokens = self.getTaggedTokens()
        tagged_tokens_dict = dict()

        for item in tagged_tokens:
            if(item[1] in tagged_tokens_dict.keys()):
                tagged_tokens_dict[item[1]] = tagged_tokens_dict[item[1]] + 1
            else:
                 tagged_tokens_dict[item[1]] = 1

        # print(tagged_tokens_dict)

        count =0
        nounCount =0
        verbCount=0
        adverbCount=0
        pronounCount = 0
        pastTense = 0
        presentTense = 0
        futureTense = 0
        adjectiveCount =0

        for item in tagged_tokens_dict.keys():
            count = count + tagged_tokens_dict[item]

            if(item == 'VBD'):
                pastTense = pastTense + tagged_tokens_dict[item]
            if(item == 'VBN'):
                pastTense = pastTense + tagged_tokens_dict[item]

            if(item == 'VBG'):
                presentTense = presentTense + tagged_tokens_dict[item]
            if(item == 'VBZ'):
                presentTense = presentTense + tagged_tokens_dict[item]
            if(item == 'VBP'):
                presentTense = presentTense + tagged_tokens_dict[item]

            if(item == 'MD'):
                futureTense = tagged_tokens_dict[item]

            if(item == 'RB'):
                adverbCount = adverbCount + tagged_tokens_dict[item]
            if(item == 'WRB'):
                adverbCount = adverbCount + tagged_tokens_dict[item]
            if(item == 'RBR'):
                adverbCount = adverbCount + tagged_tokens_dict[item]
            if(item == 'RBS'):
                adverbCount = adverbCount + tagged_tokens_dict[item]

            if(item == 'JJ'):
                adjectiveCount = adjectiveCount + tagged_tokens_dict[item]
            if(item == 'JJR'):
                adjectiveCount = adjectiveCount + tagged_tokens_dict[item]
            if(item == 'JJS'):
                adjectiveCount = adjectiveCount + tagged_tokens_dict[item]

            if(item == 'PRP'):
                pronounCount = pronounCount + tagged_tokens_dict[item]
            if(item == 'PRP$'):
                pronounCount = pronounCount + tagged_tokens_dict[item]
            if(item == 'WP$'):
                pronounCount = pronounCount + tagged_tokens_dict[item]

            if(item == 'NN'):
                nounCount = nounCount + tagged_tokens_dict[item]
            if(item == 'NNS'):
                nounCount = nounCount + tagged_tokens_dict[item]
            if(item == 'NNP'):
                nounCount = nounCount + tagged_tokens_dict[item]
            if(item == 'NNPS'):
                nounCount = nounCount + tagged_tokens_dict[item]

            if(item == 'VB'):
                verbCount = tagged_tokens_dict[item]

        res ={
            'cleanedToken':word_tokenize(self.textData),
            'pastTenseFraction':(0 if count ==0 else ((pastTense)/count)),
            'presentTenseFraction':(0 if count ==0 else ((presentTense)/count)),
            'futureTenseFraction':(0 if count ==0 else ((futureTense)/count)),
            'advFraction':(0 if count ==0 else adverbCount/count) ,
            'adjFraction':(0 if count ==0 else adjectiveCount/count) ,
            'pronounFraction':(0 if count ==0 else pronounCount/count) ,
            'nounFraction': (0 if count ==0 else nounCount/count),
            'vbFration': (0 if count ==0 else verbCount/count)
            }

        return res

# def suicudalRecords():
#     for fileCount in range(1, 27):
#         TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
#
#
#         writer.writerow({'FileNumber': fileCount, 'NOUN': (nounCount/count),'VERB': (verbCount/count),'ADV':(adverbCount/count) ,'P1':(personalPronounCount/count),'P2':(posessivePronounCount/count) ,'Class': 'S','ClassBool': 1})
#
# def personalNarrationRecords():
#     for fileCount in range(1, 18):
#         TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
#         tagged_tokens = fromTextFile(TEXT_FILE)
#         tagged_tokens_dict = dict()
#
#         for item in tagged_tokens:
#             if(item[1] in tagged_tokens_dict.keys()):
#                 tagged_tokens_dict[item[1]] = tagged_tokens_dict[item[1]] + 1
#             else:
#                  tagged_tokens_dict[item[1]] = 1
#
#         #print(tagged_tokens_dict)
#
#         count =0;
#         nounCount =0
#         verbCount=0
#         adverbCount=0
#         personalPronounCount = 0
#         posessivePronounCount = 0
#
#         for item in tagged_tokens_dict.keys():
#             count = count + tagged_tokens_dict[item]
#             if(item == 'NN'):
#                 nounCount = tagged_tokens_dict[item]
#             if(item == 'VB'):
#                 verbCount = tagged_tokens_dict[item]
#             if(item == 'RB'):
#                 adverbCount = tagged_tokens_dict[item]
#             if(item == 'PRP'):
#                 personalPronounCount = tagged_tokens_dict[item]
#             if(item == 'PRP$'):
#                 posessivePronounCount = tagged_tokens_dict[item]
#
#         writer.writerow({'FileNumber': fileCount, 'NOUN': (nounCount/count),'VERB': (verbCount/count),'ADV':(adverbCount/count) ,'P1':(personalPronounCount/count),'P2':(posessivePronounCount/count) ,'Class': 'P','ClassBool': 0})
#
#
#
#
# CSV_FILE = path.join(os.pardir, "Resources/Machine-Learning-Files/Features.csv")
# csvfile = open(CSV_FILE, 'w')
# fieldnames = ['FileNumber','NOUN', 'VERB','ADV','P1','P2','Class','ClassBool']
# writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=fieldnames)
# writer.writeheader()
#
# #personalNarrationRecords()
#
# suicudalRecords()




#print(count)
#print(nounCount)
#print(verbCount)
#print(adverbCount)
#print(personalPronounCount)
#print(posessivePronounCount)

#print("PERSONAL NARRATION FILE NO::")
#print("FRACTION OF NOUN::"+ str(nounCount/count))
#print("FRACTION OF VERB::"+ str(verbCount/count))
#print("FRACTION OF ADVERB::"+ str(adverbCount/count))
#print("FRACTION OF Personal Pronoun::"+ str(personalPronounCount/count))
#print("FRACTION OF PosessivePronoun::"+ str(posessivePronounCount/count))


