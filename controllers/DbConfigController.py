
from views.showFormAddDb import Ui_Dialog 
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from builders.DbManager import DbManager
import globals
from events.AddNewDbConfigEvent import AddNewDbConfigEvent

class DbConfigController(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(globals.VIEWS_DIR + "/showFormAddDb.ui", self) 

        self.addNewConfigEvent = AddNewDbConfigEvent(self)
        self.buttonBox.accepted.connect(self.addNewConfigEvent.run)
        self.displayDbTypes()

    def getMessage(self):
        return "DB has been added succesfully!"
    
    def displayDbTypes(self):
        builder = DbManager()
        for db in builder.getList():
            self.comboBox.addItem(db.name)