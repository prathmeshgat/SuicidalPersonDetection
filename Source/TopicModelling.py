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

def fromTextFile(TEXT_FILE):
    fp = open(TEXT_FILE, "r")
    t_file = fp.read()
    fp.close()
    return(t_file)

def getpersonalNarrationDocSet():
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

    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for i in doc_set:

        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        en_stop.append('like')
        en_stop.append('hesitation')
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]

        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

        # add tokens to list
        texts.append(stopped_tokens)
        return texts;

def lda_apply(texts):
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=20)

    print(ldamodel.print_topics(num_topics=50, num_words=10))

#Get Suicidal Doc set
#suicidalDocSet = getSuicidalDocSet()
#pre-process Suicidal Doc set
#suicidalTokens = preprocessDocSet(suicidalDocSet)
#apply lda on suicidal doc set
#print("Topics in Suicidal Corpus::")
#lda_apply(suicidalTokens)

#Get Personal NArration DocSet
#personalNarrationDocSet = getpersonalNarrationDocSet()
#pre-process Personal narration Doc set
#personalNarrationTokens = preprocessDocSet(personalNarrationDocSet)
#apply lda on Personal Narration doc set
#print("Topics in Personal Narration Corpus::")
#lda_apply(personalNarrationTokens)

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# create sample documents
doc_set = list()
for fileCount in range(1, 27):
    TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Suicidal/"+str(fileCount)+".txt")
    doc = fromTextFile(TEXT_FILE)
    doc_set.append(doc)

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:

    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    en_stop.append('like')
    en_stop.append('hesitation')
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel1 = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=50)
print(ldamodel1.print_topics(num_topics=50, num_words=10))


# create sample documents
doc_set = list()
for fileCount in range(1, 18):
    TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/"+str(fileCount)+".txt")
    doc = fromTextFile(TEXT_FILE)
    doc_set.append(doc)

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:

    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    en_stop.append('like')
    en_stop.append('hesitation')
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel2 = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=50)
print(ldamodel2.print_topics(num_topics=50, num_words=10))