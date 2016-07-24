__author__ = 'Prathmesh'

import DataAccess.Repos.SuicidalDocumentRepo as Repo1
import DataAccess.Repos.SuicidalCommentRepo as Repo2
class Container:

    def __init__(self):
        self.SuicidalDocumentRepo = Repo1.SuicidalDocumentRepo()
        self.SuicidalCommentRepo = Repo2.SuicidalCommentRepo()