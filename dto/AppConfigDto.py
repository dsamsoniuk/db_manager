
from dto.ConfigDbDto import ConfigDbDto

class AppConfigDto:

    def __init__(self, current_db_manager: ConfigDbDto|None = None, default_path: str = ''):
        self.current_db_manager = current_db_manager 
        self.default_path = default_path


    