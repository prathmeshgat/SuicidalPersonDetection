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

class TopicModelling:

    def __init__(self,docSet,noTopics,noWords,noPasses):
        self.docSet = docSet
        self.noTopics = noTopics
        self.noWords = noWords
        self.noPasses = noPasses

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

    def lda_apply(self,texts,no_topics,no_words,no_passes):
        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(texts)

        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in texts]

        # generate LDA model
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=no_topics, id2word = dictionary, passes=no_passes)

        return ldamodel.print_topics(num_topics=no_topics, num_words=no_words)

    def getTopics(self):

        #pre-process Suicidal Doc set
        Tokens = self.preprocessDocSet()

        #apply lda on suicidal doc set
        # print("Topics in Suicidal Corpus::")
        res = self.lda_apply(Tokens,self.noTopics,self.noWords,self.noPasses)

        return res

