__author__ = 'Prathmesh'

import gensim
import os
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag, word_tokenize
from gensim import corpora, models
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
    for fileCount in range(1, 18):
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

def preprocessDocSet(doc_set):
    tokenizer = RegexpTokenizer(r'\w+')

    # create English stop words list
    en_stop = get_stop_words('en')
    en_stop.append('like')
    en_stop.append('hesitation')
    en_stop.append('know')
    en_stop.append('just')
    en_stop.append('well')
    en_stop.append('go')
    en_stop.append('thing')
    en_stop.append('get')
    en_stop.append('said')
    en_stop.append('time')
    en_stop.append('dnmt')
    en_stop.append('will')
    en_stop.append('think')
    en_stop.append('will')
    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for i in doc_set:

        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        #tokens = word_tokenize(raw)
        # remove stop words from tokens
        stopped_tokens = [item for item in tokens if not item in en_stop]

        # stem tokens
        stemmed_tokens = [p_stemmer.stem(item) for item in stopped_tokens]

        # remove stop words from stemmed tokens
        stopped_tokens = [item for item in stemmed_tokens if not item in en_stop]

        #remove tokens containing ''' & '%'
        cleaned_tokens = [item for item in stopped_tokens if ((item.find('\'') == -1) and item.find('%') == -1) and len(item)>2]

        # add tokens to list
        texts.append(cleaned_tokens)

    return texts

def testPreProcessDocSet(doc_set):

    tokenizer = RegexpTokenizer(r'\w+')

    # create English stop words list
    en_stop = get_stop_words('en')
    en_stop.append('like')
    en_stop.append('hesitation')
    en_stop.append('know')
    en_stop.append('just')
    en_stop.append('well')
    en_stop.append('go')
    en_stop.append('thing')
    en_stop.append('get')
    en_stop.append('said')
    en_stop.append('time')
    en_stop.append('dnmt')
    en_stop.append('will')
    en_stop.append('think')
    en_stop.append('will')
    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for doc in doc_set:
        raw = doc.lower()
        text = word_tokenize(raw)
        tagList = nltk.pos_tag(text)
        tagged_tokens_dict = dict()

        #text tokens
        text =[]

        #posTokens take only noun,verb,PROpositin
        posTokens = list()
        for item in tagList:
            # if(item[1] in ["NN","VB","RB","PRP","PRP$"]):
            if(item[1] in ["NN","PRP"]):
                posTokens.append(item[0])

        # remove stop words from tokens
        stopped_tokens = [item for item in posTokens if not item in en_stop]

        # stem tokens
        stemmed_tokens = [p_stemmer.stem(item) for item in stopped_tokens]

        # remove stop words from stemmed tokens
        stopped_tokens = [item for item in stemmed_tokens if not item in en_stop]

        #remove tokens containing ''' & '%'
        cleaned_tokens = [item for item in stopped_tokens if ((item.find('\'') == -1) and item.find('%') == -1) and len(item)>2]
        #cleaned_tokens = [item for item in stopped_tokens if ((item.find('\'') == -1) and item.find('%') == -1)]

        # add tokens to list
        texts.append(cleaned_tokens)

    return texts

def lda_apply(texts,no_topics,no_words,no_passes):
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=no_topics, id2word = dictionary, passes=no_passes)

    print(ldamodel.print_topics(num_topics=no_topics, num_words=no_words))

def topicModellingSuicidal():
    #Get Suicidal Doc set
    suicidalDocSet = getSuicidalDocSet()

    #pre-process Suicidal Doc set
    suicidalTokens = testPreProcessDocSet(suicidalDocSet)

    #apply lda on suicidal doc set
    print("Topics in Suicidal Corpus::")
    lda_apply(suicidalTokens,7,5,10)

    return

def topicModellingPersonalNarration():
    #Get Personal NArration DocSet
    personalNarrationDocSet = getPersonalNarrationDocSet()

    #pre-process Personal narration Doc set
    personalNarrationTokens = testPreProcessDocSet(personalNarrationDocSet)

    #apply lda on Personal Narration doc set
    print("Topics in Personal Narration Corpus::")
    lda_apply(personalNarrationTokens,26,5,10)

    return

def frequentWordsSuicidalVideos():
    #Get Suicidal Doc set
    suicidalDocSet = getSuicidalDocSet()

    #pre-process Suicidal Doc set
    suicidalTokens = testPreProcessDocSet(suicidalDocSet)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(suicidalTokens)

    sorted_dict= sorted(dictionary.dfs.items(), key=lambda x:x[1],reverse=True)

    wordCount=0
    topTenWords = list()
    for item in sorted_dict:
        if(wordCount<=50):
             for item1 in dictionary.token2id.items():
                 if item[0] == item1[1]:
                     topTenWords.append([item1[0],item[1]])
        else:
            break
        wordCount = wordCount + 1

    print("Suicidal::\n"+str(topTenWords))
    return topTenWords

def frequentWordsPersonalNarrationVideos():
    #Get Suicidal Doc set
    personlaNarrationDocSet = getPersonalNarrationDocSet()

    #pre-process Suicidal Doc set
    personlaNarrationTokens = testPreProcessDocSet(personlaNarrationDocSet)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(personlaNarrationTokens)

    sorted_dict= sorted(dictionary.dfs.items(), key=lambda x:x[1],reverse=True)

    wordCount=0
    topTenWords = list()
    for item in sorted_dict:
        if(wordCount<=50):
             for item1 in dictionary.token2id.items():
                 if item[0] == item1[1]:
                     topTenWords.append([item1[0],item[1]])
        else:
            break
        wordCount = wordCount + 1

    print("PN::\n"+str(topTenWords))
    return topTenWords


#topicModellingSuicidal()

#topicModellingPersonalNarration()

frequentWordsSuicidalVideos()

frequentWordsPersonalNarrationVideos()

