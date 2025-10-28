from abc import abstractmethod
from dto.ConfigDbDto import ConfigDbDto

class AbstractDbManager:
    @abstractmethod
    def getExportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        pass

    @abstractmethod
    def getImportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        pass