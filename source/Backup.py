__author__ = 'Prathmesh'

import os
import speech_recognition as sr
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from os import path

# obtain path to "english.wav" in the same folder as this script

AUDIO_FILE = path.join(os.pardir, "Resources\\AmandaTodd.wav")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Wit.ai
# WIT_AI_KEY = "3OSIPPVZUPXYD2AV2P65UKDNHDNBHAZA" # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "599f8844e2464b7e81ba1d63147c5f63" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using api.ai
# API_AI_CLIENT_ACCESS_TOKEN = "5efa00b0867847efa69a6abdca3bc3b1 " # api.ai keys are 32-character lowercase hexadecimal strings
# try:
#     print("api.ai thinks you said " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN))
# except sr.UnknownValueError:
#     print("api.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from api.ai service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "8e6242fe-09d3-4b27-9c54-d75fdbbe5866" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "I5dtpHrttHst" # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    TextData = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))


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

print(tokens)

TEXT_FILE = path.join(os.pardir, "TextFiles\\AmandaTodd.txt")
fp = open(TEXT_FILE,"w")
#pickle.dump(tokens, fp)
fp.write(str(tokens))
fp.close()





