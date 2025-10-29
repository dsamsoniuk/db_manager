
from views.showFormAddDb import Ui_Dialog 
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from dto.ConfigDbDto import ConfigDbDto
from builders.DbBuild import DbBuild
from services.ConfigDbService import ConfigDbService
import os, sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(".")

VIEWS_DIR = os.path.join(BASE_DIR, "views")


class AddDbDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(VIEWS_DIR + "/showFormAddDb.ui", self) 

        self.buttonBox.accepted.connect(self.save)

        builder = DbBuild()
        for db in builder.getList():
            self.comboBox.addItem(db.name)

    def getMessage(self):
        return "Baza została pomyślnie dodana!" #self.lineEdit.text()
    
    def save(self) -> None:

        dto = ConfigDbDto()
        dto.type_db = self.comboBox.currentText()
        dto.host = self.host.text()
        dto.port = self.port.text()
        dto.user = self.db_user.text()
        dto.name = self.name.text()
        dto.db_name = self.db_name.text()
        dto.db_password = self.db_password.text()

        serviceConfigDb = ConfigDbService()
        serviceConfigDb.add(dto)