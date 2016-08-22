__author__ = 'Prathmesh'


class WordStatistics:

    def __init__(self,word,happinessScore,suicidalCorpusCount,personalNarrationCorpusCount,difference,
                 pctHappinessShiftPN,pctHappinessShiftSui,_id=-1):

        self._id = _id

        self.word = word

        self.happinessScore = happinessScore

        self.suicidalCorpusCount = suicidalCorpusCount

        self.personalNarrationCorpusCount = personalNarrationCorpusCount

        self.difference = difference

        self.pctHappinessShiftPN = pctHappinessShiftPN

        self.pctHappinessShiftSui = pctHappinessShiftSui