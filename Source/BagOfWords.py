__author__ = 'Prathmesh'

import gensim
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora

class BagOfWords:

    def __init__(self,docSet,numberOfWords):
        self.docSet = docSet
        self.numberOfWords = numberOfWords

    def preprocessDocSet(self):
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
        for i in self.docSet:

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

    def preprocessDocSetForWordCount(self):
        tokenizer = RegexpTokenizer(r'\w+')

        # create English stop words list
        en_stop = get_stop_words('en')
        # en_stop.append('like')
        en_stop.append('hesitation')
        # en_stop.append('know')
        # en_stop.append('just')
        # en_stop.append('well')
        # en_stop.append('go')
        # en_stop.append('thing')
        # en_stop.append('get')
        # en_stop.append('said')
        # en_stop.append('time')
        en_stop.append('dnmt')
        # en_stop.append('will')
        # en_stop.append('think')
        # en_stop.append('will')
        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()

        # list for tokenized documents in loop
        texts = []

        # loop through document list
        for i in self.docSet:

            # clean and tokenize document string
            raw = i.lower()
            tokens = tokenizer.tokenize(raw)
            #tokens = word_tokenize(raw)
            # remove stop words from tokens
            stopped_tokens = [item for item in tokens if not item in en_stop]

            # stem tokens
            # stemmed_tokens = [p_stemmer.stem(item) for item in stopped_tokens]

            # remove stop words from stemmed tokens
            # stopped_tokens = [item for item in stemmed_tokens if not item in en_stop]

            #remove tokens containing ''' & '%'
            cleaned_tokens = [item for item in stopped_tokens if ((item.find('\'') == -1) and item.find('%') == -1) and len(item)>2]

            # add tokens to list
            texts.append(cleaned_tokens)

        return texts

    def topFrequentWords(self):
        #Get Doc set
        DocSet = self.docSet

        #pre-process Suicidal Doc set
        tokens = self.preprocessDocSet()

        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(tokens)

        sorted_dict= sorted(dictionary.dfs.items(), key=lambda x:x[1],reverse=True)

        wordCount=0
        topTenWords = list()
        for item in sorted_dict:
            if(wordCount<=self.numberOfWords):
                 for item1 in dictionary.token2id.items():
                     if item[0] == item1[1]:
                         topTenWords.append([item1[0],item[1]])
            else:
                break
            wordCount = wordCount + 1

        # print("Suicidal::\n"+str(topTenWords))
        return topTenWords

    def wordFrequency(self):
        #Get Doc set
        DocSet = self.docSet

        #pre-process Suicidal Doc set
        tokens = self.preprocessDocSetForWordCount()

        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(tokens)

        sorted_dict= sorted(dictionary.dfs.items(), key=lambda x:x[1],reverse=True)


        wordFrequencyDict = dict()
        for item in sorted_dict:
            for item1 in dictionary.token2id.items():
                if item[0] == item1[1]:
                    wordFrequencyDict[item1[0]] = item[1]

        # print("Suicidal::\n"+str(topTenWords))
        return wordFrequencyDict

