__author__ = 'Prathmesh'

import DataAccess.Repos.SuicidalDocumentRepo as Repo1
import DataAccess.Repos.SuicidalCommentRepo as Repo2
import DataAccess.Repos.PersonalNarrationDocumentRepo as Repo3
import DataAccess.Repos.PersonalNarrationCommentRepo as Repo4
import DataAccess.Repos.HappinessScoreRepo as Repo5
class Container:

    def __init__(self):
        self.SuicidalDocumentRepo = Repo1.SuicidalDocumentRepo()
        self.SuicidalCommentRepo = Repo2.SuicidalCommentRepo()
        self.PersonalNarrationDocumentRepo = Repo3.PersonalNarrationDocumentRepo()
        self.PersonalNarrationCommentRepo = Repo4.PersonalNarrationCommentRepo()
        self.HappinessScoreRepo = Repo5.HappinessScoreRepo()