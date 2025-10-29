
from views.showFormAddDb import Ui_Dialog 
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from dto.ConfigDbDto import ConfigDbDto
from builders.DbManager import DbManager
from services.ConfigDbRepository import ConfigDbRepository
import globals

class DbConfigController(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        
        uic.loadUi(globals.VIEWS_DIR + "/showFormAddDb.ui", self) 

        self.buttonBox.accepted.connect(self.save)

        builder = DbManager()
        for db in builder.getList():
            self.comboBox.addItem(db.name)

    def getMessage(self):
        return "Baza została pomyślnie dodana!"
    
    def save(self) -> None:

        dto = ConfigDbDto()
        dto.type_db = self.comboBox.currentText()
        dto.host = self.host.text()
        dto.port = self.port.text()
        dto.user = self.db_user.text()
        dto.name = self.name.text()
        dto.db_name = self.db_name.text()
        dto.db_password = self.db_password.text()

        configDbRepository = ConfigDbRepository()
        configDbRepository.add(dto)