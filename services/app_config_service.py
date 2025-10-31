from services import MemoryService
from dto.AppConfigDto import AppConfigDto
from dto.ConfigDbDto import ConfigDbDto

class AppConfigService:

    memoryIndexName: str = 'app_config'

    def __init__(self):
        self.memoryService = MemoryService()

    def set(self, current_db_manager: ConfigDbDto = None, default_path: str = '') -> None :
        """ Set data to application config """

        config = AppConfigDto(current_db_manager, default_path)
        self.memoryService.set(self.memoryIndexName, config)

    def get(self) -> AppConfigDto :
        """ Get data from application config """

        return self.memoryService.get(self.memoryIndexName, AppConfigDto())
    