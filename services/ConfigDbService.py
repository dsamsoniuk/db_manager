from services.MemoryService import MemoryService
from dto.ConfigDbDto import ConfigDbDto

class ConfigDbService:

    def __init__(self):
        self.memoryService = MemoryService()
        self.list = self.memoryService.get('list_config_db', [])

    def add(self, dto: ConfigDbDto) -> None :
        """
        Add dbconfig to memory
        """
        newList = self.list or []
        newList.append(dto)
        self.memoryService.set('list_config_db', newList)

    def delete(self, name: str) -> None:
        """
        Delete dbconfig from memory
        """
        newList = []

        for record in self.list:
            if record.name == name:
                continue
            else:
                newList.append(record)
        self.memoryService.set('list_config_db', newList)

    def findAll(self) -> list[ConfigDbDto]:
        """
        Get all dbconfig from memory
        """
        return self.list or []
    
    def findByName(self, name: str) -> ConfigDbDto|None :
        """
        Find ConfigDbDto by name
        """
        for record in self.list:
            if record.name == name:
                return record
        return None