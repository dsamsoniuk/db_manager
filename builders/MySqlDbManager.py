from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager

class MySqlDbManager(AbstractDbManager):
    
    name: str = 'mysql'

    def setConfig(self, dto: ConfigDbDto) -> None:
        self.config = dto

    def getExportCommand(self, fileName: str) -> str:
        """
        Export to file 
        """
        return f"mysqldump -u {self.config.user} --password={self.config.db_password} --port={self.config.port} --no-tablespaces --host={self.config.host} {self.config.db_name} > {fileName}"
    
    def getImportCommand(self, fileName: str) -> str:
        """
        Import from file to DB
        """
        return f"mysql -u {self.config.user} --password={self.config.db_password} --port={self.config.port} --host={self.config.host} {self.config.db_name} < {fileName}"
