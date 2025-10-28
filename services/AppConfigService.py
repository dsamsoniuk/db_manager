from services.MemoryService import MemoryService
from dto.AppConfigDto import AppConfigDto
from dto.ConfigDbDto import ConfigDbDto

class AppConfigService:

    memoryIndexName: str = 'app_config'

    def __init__(self):
        self.memoryService = MemoryService()

    def set(self, current_db_manager: ConfigDbDto = None, default_path: str = '') -> None :
        config = AppConfigDto(current_db_manager, default_path)
        self.memoryService.set(self.memoryIndexName, config)

    def get(self) -> AppConfigDto :
        return self.memoryService.get(self.memoryIndexName, AppConfigDto())
    