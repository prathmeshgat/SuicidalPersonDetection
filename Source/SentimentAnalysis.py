__author__ = 'Prathmesh'
import os
import json
from os import path
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

class SentimentAnalyzer:
    @staticmethod
    def calculateSentiment(textdata):
        return vaderSentiment(textdata)



