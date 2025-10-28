from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager

class MySqlDbManager(AbstractDbManager):
    
    name: str = 'mysql'

    def getExportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        """
        Export to file 
        """
        return f"mysqldump -u {dto.user} --password={dto.db_password} --port={dto.port} --no-tablespaces --host={dto.host} {dto.db_name} > {fileName}"
    
    def getImportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        """
        Import from file to DB
        """
        return f"mysql -u {dto.user} --password={dto.db_password} --port={dto.port} --host={dto.host} {dto.db_name} < {fileName}"
