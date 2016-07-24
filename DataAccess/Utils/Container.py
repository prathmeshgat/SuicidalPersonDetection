__author__ = 'Prathmesh'

import DataAccess.Repos.DocumentRepo as Repo1
import DataAccess.Repos.CommentRepo as Repo2
class Container:

    def __init__(self):
        self.DocumentRepo = Repo1.DocumentRepo()
        self.CommentRepo = Repo2.CommentRepo()