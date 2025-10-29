# from dotenv import load_dotenv
import os
from views.main import Ui_MainWindow 
from PyQt6.QtWidgets import  QMainWindow, QTreeWidgetItem
from controllers.AddDbDialog import AddDbDialog
from services.MemoryService import MemoryService
from builders.DbBuild import DbBuild
# load_dotenv()
from builders.AbstractDbManager import AbstractDbManager
from dto.ConfigDbDto import ConfigDbDto
from services.ConfigDbService import ConfigDbService
from services.CommandService import CommandService
from services.AppConfigService import AppConfigService

class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        appService = AppConfigService()
        config = appService.get()

        self.inputDirPath.setText(config.default_path)
        self.pushButton.clicked.connect(self.reloadFilesList)

        self.treeFile.setHeaderLabel("SQL Files")
        self.showFormAddDb.clicked.connect(self.open_dialog)

        self.treeFile.itemClicked.connect(self.on_item_clicked)

        self.btnDeleteRecordDb.clicked.connect(self.deleteRecordDb)

        self.btnExport.clicked.connect(self.exportFromDb)
        self.btnImport.clicked.connect(self.importToDb)

        self.loadListDb()
        self.reloadFilesList()

    def exportFromDb(self):
        fileName = self.inputCurrentFile.text()
        recordDbname = self.comboBoxListDb.currentText()

        if fileName == '' or recordDbname == '':
            self.textBrowser.setText("Brak wybranej nazwy pliku lub bazy")
            return

        serviceConfigDb = ConfigDbService()
        configDb = serviceConfigDb.findByName(recordDbname)
        if isinstance(configDb, ConfigDbDto) == False:
            return
        
        dbBuildService = DbBuild()
        builder = dbBuildService.findByName(configDb.type_db)

        if isinstance(builder, AbstractDbManager):
            commandservice = CommandService()
            command = builder.getExportCommand(configDb, fileName)
            try:
                commandservice.exec(command)
                self.textBrowser.setText('Export z bazy do pliku wykonany!')
            except Exception as e:
                self.textBrowser.setText(repr(e))
        else:
            print('Blad, brak buildera: ' + configDb.type_db)

        self.reloadFilesList()

    def importToDb(self):
        fileName = self.inputCurrentFile.text()
        recordDbname = self.comboBoxListDb.currentText()

        if fileName == '' or recordDbname == '':
            self.textBrowser.setText("Brak wybranej nazwy pliku lub bazy")
            return

        serviceConfigDb = ConfigDbService()
        configDb = serviceConfigDb.findByName(recordDbname)
        if isinstance(configDb, ConfigDbDto) == False:
            return
        
        dbBuildService = DbBuild()
        builder = dbBuildService.findByName(configDb.type_db)

        if isinstance(builder, AbstractDbManager):
            commandservice = CommandService()
            command = builder.getImportCommand(configDb, fileName)
            try:
                commandservice.exec(command)
                self.textBrowser.setText('Import z pliku do bazy wykonany!')
            except Exception as e:
                self.textBrowser.setText(repr(e))
        else:
            print('Blad, brak buildera: ' + configDb.type_db)

    def deleteRecordDb(self):
        recordDbname = self.comboBoxListDb.currentText()
        serviceConfigDb = ConfigDbService()
        serviceConfigDb.delete(recordDbname)
        self.loadListDb()

    def loadListDb(self):
        self.comboBoxListDb.clear()

        serviceConfigDb = ConfigDbService()
        list = serviceConfigDb.findAll()

        for dbConfig in list:
            self.comboBoxListDb.addItem(dbConfig.name, dbConfig.type_db)

    def on_item_clicked(self, item, column):
        filePath = self.inputDirPath.text() + item.text(column)
        self.inputCurrentFile.setText(filePath)

    def load_sql_files(self, tree_widget, folder):
        tree_widget.clear()
        for name in os.listdir(folder):
            if name.endswith(".sql"):
                item = QTreeWidgetItem([name])
                tree_widget.addTopLevelItem(item)

    def reloadFilesList(self):
        appService = AppConfigService()
        dir = self.inputDirPath.text()

        try:
            self.load_sql_files(self.treeFile, dir)
            appService.set(default_path = self.inputDirPath.text())
        except:
            self.textBrowser.setText('Nie udalo sie pobrac plików')

    def open_dialog(self):
            dialog = AddDbDialog()
            if dialog.exec(): 
                value = dialog.getMessage()
                self.textBrowser.setText(value)
                self.loadListDb()