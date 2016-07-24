__author__ = 'Prathmesh'

class PersonalNarrationDocument:

    def __init__(self,documentId,transcript,category,_id=-1,nnFraction=0,vbFration=0,advFraction=0,prp1Fraction=0,prp2Fraction=0,
                 cleanedToken=list(),posSentiment=0,negSentiment=0,neuSentiment=0,compoundSentiment=0,
                 custom1=None,custom2 =None,custom3 = None,custom4 =None,custom5 = None):

        self.documentId = documentId

        self.transcript = transcript

        self.category = category

        self._id = _id

        self.nnFraction = nnFraction

        self.vbFration = vbFration

        self.advFraction = advFraction

        self.prp1Fraction = prp1Fraction

        self.prp2Fraction = prp2Fraction

        self.cleanedToken = cleanedToken

        self.posSentiment = posSentiment

        self.negSentiment = negSentiment

        self.neuSentiment = neuSentiment

        self.compoundSentiment = compoundSentiment

        self.custom1 = custom1

        self.custom2 = custom2

        self.custom3 = custom3

        self.custom4 = custom4

        self.custom5 = custom5
