from dto.ConfigDbDto import ConfigDbDto
from builders.AbstractDbManager import AbstractDbManager

class MySqlDbManager(AbstractDbManager):
    
    name: str = 'mysql'

    # Export to file 
    def getExportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        return f"mysqldump -u {dto.user} --password={dto.db_password} --host={dto.host} {dto.db_name} > {fileName}"
    
    # Import from file to DB
    def getImportCommand(self, dto: ConfigDbDto, fileName: str) -> str:
        return f"mysql -u {dto.user} --password={dto.db_password} --host={dto.host} {dto.db_name} < {fileName}"
