__author__ = 'Prathmesh'

import gensim
import pyLDAvis.gensim
import os
import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag, word_tokenize
from gensim import corpora, models
from os import path
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

class TopicModelling:

    def __init__(self,docSet,noTopics,noWords,noPasses,visualizationName):
        self.docSet = docSet
        self.noTopics = noTopics
        self.noWords = noWords
        self.noPasses = noPasses
        self.visualizationName = visualizationName

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

        # _data = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)

        # FILE = path.join(os.pardir, "Results/Visualizations/TopicModelling/"+self.visualizationName)

        # pyLDAvis.save_html(_data,FILE)

        return ldamodel.print_topics(num_topics=no_topics, num_words=no_words)

    def lda_apply_with_propensity(self):

         #pre-process Suicidal Doc set
        Tokens = self.preprocessDocSet()

        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(Tokens)

        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in Tokens]

        # num topics
        parameter_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


        # for num_topics_value in num_topics_list:
        for parameter_value in parameter_list:

            # split into 80% training and 20% test sets
            np.random.shuffle(corpus)
            p = int(len(corpus) * .8)
            cp_train = corpus[0:p]
            cp_test = corpus[p:]

            ldamodel = gensim.models.ldamodel.LdaModel(cp_train, num_topics=3, id2word = dictionary,
                                                       passes=25,update_every=0, alpha=None, eta=None,chunksize=3125,decay=0.5)

            # perplex = ldamodel.bound(cp_test)

            per_word_perplex = ldamodel.log_perplexity(cp_test, total_docs=None)

            count =0
            for document in cp_test:
                for word in document:
                    count = count +1

            perplex = np.exp2(-per_word_perplex / count)

            # perplex = np.exp2(-per_word_perplex / sum(cnt for document in cp_test for _, cnt in document))

            print("Topics:: "+str(parameter_value)+" Perplexity: "+ str(perplex)+" Per-word Perplexity: " +str(per_word_perplex))

    def getTopics(self):

        #pre-process Suicidal Doc set
        Tokens = self.preprocessDocSet()

        #apply lda on suicidal doc set
        # print("Topics in Suicidal Corpus::")
        res = self.lda_apply(Tokens,self.noTopics,self.noWords,self.noPasses)

        return res

