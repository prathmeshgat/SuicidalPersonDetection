__author__ = 'Prathmesh'
import os
import speech_recognition as sr
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from os import path

def Tokenize(TextData):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = list()

    # create English stop words list
    en_stop = get_stop_words('en')

    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()

    # clean and tokenize document string
    raw = TextData.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    tokens = stemmed_tokens

    TOKENIZEDTEXT_FILE = path.join(os.pardir, "Resources/TokenizedTextFiles/Personal-Narration/Unbroken - Motivational Video.txt")
    fp = open(TOKENIZEDTEXT_FILE, "w")
    print(TOKENIZEDTEXT_FILE)
    # pickle.dump(tokens, fp)
    fp.write(str(tokens))
    fp.close()

def CovertAudioToText():
    TextData=""
    # obtain path to "english.wav" in the same folder as this script
    AUDIO_FILE = path.join(os.pardir, "Resources/Personal-Narration/Unbroken - Motivational Video.wav")

    # use the audio file as the audio Source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file

    # recognize speech using IBM Speech to Text
    IBM_USERNAME = "3b3b1302-75af-429c-99e3-fb6ae5d18b40" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "tx4ZdTbfswCo" # IBM Speech to Text passwords are mixed-case alphanumeric strings

    try:
        TextData = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        print(TextData)
        TEXT_FILE = path.join(os.pardir, "Resources/TextFiles/Personal-Narration/Unbroken - Motivational Video.txt")
        fp = open(TEXT_FILE, "w")
        print(TEXT_FILE)
        # pickle.dump(tokens, fp)
        fp.write(TextData)
        fp.close()
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))

    return TextData;

TextData = CovertAudioToText()

# TOKENIZEDTEXT_FILE = path.join(os.pardir, "TextFiles/☯Reading My Suicide Letter☯.txt")
# fp =open(TOKENIZEDTEXT_FILE,'r')
# TextData = fp.read()

#Tokenize(TextData)







