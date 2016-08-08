__author__ = 'Prathmesh'

class SuicidalDocument:

    def __init__(self,documentId,transcript,category,_id=-1,pastTenseFraction=0,presentTenseFraction=0,
                 futureTenseFraction=0,advFraction=0,adjFraction=0,pronounFraction=0,nounFraction=0,
                 vbFration=0,cleanedToken=list(),posSentiment=0,negSentiment=0,
                 neuSentiment=0,compoundSentiment=0):

        self.documentId = documentId

        self.transcript = transcript

        self.category = category

        self._id = _id

        self.pastTenseFraction = pastTenseFraction

        self.presentTenseFraction = presentTenseFraction

        self.futureTenseFraction = futureTenseFraction

        self.advFraction = advFraction

        self.adjFraction = adjFraction

        self.pronounFraction = pronounFraction

        self.nounFraction = nounFraction

        self.vbFration = vbFration

        self.cleanedToken = cleanedToken

        self.posSentiment = posSentiment

        self.negSentiment = negSentiment

        self.neuSentiment = neuSentiment

        self.compoundSentiment = compoundSentiment
