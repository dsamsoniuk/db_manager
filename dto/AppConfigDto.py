
from dto.ConfigDbDto import ConfigDbDto

class AppConfigDto:
    current_db_manager: ConfigDbDto|None = None
    default_path: str = ''
    