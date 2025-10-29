from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager

class MongoDbManager(AbstractDbManager):
    name: str = 'mongodb'
    
    def getExportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        # return f"mongodump -h{dto.host}"
        return f"mongodump --host {dto.host} --port {dto.port} --username {dto.user} --password {dto.db_password} --db {dto.db_name} --out {fileName}"
    
    def getImportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        return f"mongoimport --host {dto.host} --port {dto.port} --username {dto.user} --password {dto.db_password} --db {dto.db_name} --out {fileName}"