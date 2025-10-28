from builders.MySqlDbManager import MySqlDbManager
from builders.MongoDbManager import MongoDbManager
from builders.AbstractDbManager import AbstractDbManager

class DbBuild:

    def __init__(self):
        self.list = [
            MySqlDbManager(),
            MongoDbManager(),
        ]

    def getList(self) -> list :
        return self.list
    
    def findByName(self, name) -> AbstractDbManager | None :
        for build in self.list:
            if name == build.name:
                return build
        return None