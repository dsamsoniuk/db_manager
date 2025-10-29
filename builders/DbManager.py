from builders.MySqlDbManager import MySqlDbManager
from builders.MongoDbManager import MongoDbManager
from builders.MariaDbManager import MariaDbManager
from builders.AbstractDbManager import AbstractDbManager
from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager
from services.ConfigDbRepository import ConfigDbRepository

class DbManager:

    def __init__(self):
        self.list = [
            MySqlDbManager(),
            # MongoDbManager(),
            MariaDbManager(),
        ]

    def getList(self) -> list :
        return self.list
    
    def findByName(self, name) -> AbstractDbManager | None :
        for build in self.list:
            if name == build.name:
                return build
        return None
    
    def getManagerByTitle(self, title: str) -> AbstractDbManager|None :

        configDbRepository = ConfigDbRepository()
        configDb = configDbRepository.findByName(title)

        if isinstance(configDb, ConfigDbDto) == False:
            return None
        
        builder = self.findByName(configDb.type_db)

        if isinstance(builder, AbstractDbManager):
            builder.setConfig(configDb)
            return builder
        
        return None