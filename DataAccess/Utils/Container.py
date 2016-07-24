__author__ = 'Prathmesh'

import DataAccess.Repos.DocumentRepo as Repos
class Container:

    def __init__(self):
        self.DocumentRepo = Repos.DocumentRepo()
