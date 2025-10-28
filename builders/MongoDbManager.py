from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager

class MongoDbManager(AbstractDbManager):
    name: str = 'mongodb'
    
    def getExportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        return f"mongodump -h{dto.host}"
    
    def getImportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        return f"mongodump -h{dto.host}"