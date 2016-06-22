import os
import speech_recognition as sr
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from os import path

TOKENIZEDTEXT_FILE = path.join(os.pardir, "TokenizedTextFiles/Suicidal/Blake Coatney - last words before he committed suicide.txt.txt")
fp = open(TOKENIZEDTEXT_FILE, "r")
tokens = fp.read()

