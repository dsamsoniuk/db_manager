
from events.AbstractEvent import AbstractEvent
from dto.ConfigDbDto import ConfigDbDto
from services.ConfigDbRepository import ConfigDbRepository
from views.showFormAddDb import Ui_Dialog 

class AddNewDbConfigEvent(AbstractEvent):

    def __init__(self, application: Ui_Dialog):
        self.application = application

    def run(self):
        dto = ConfigDbDto()
        dto.type_db = self.application.comboBox.currentText()
        dto.host = self.application.host.text()
        dto.port = self.application.port.text()
        dto.user = self.application.db_user.text()
        dto.db_name = self.application.db_name.text()
        dto.db_password = self.application.db_password.text()
        dto.name = dto.type_db + ": " + self.application.name.text()

        configDbRepository = ConfigDbRepository()
        configDbRepository.add(dto)