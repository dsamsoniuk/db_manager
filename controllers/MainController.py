from views.main import Ui_MainWindow 
from PyQt6.QtWidgets import  QMainWindow
from services.ConfigDbRepository import ConfigDbRepository
from services.AppConfigService import AppConfigService
from events.ExportEvent import ExportEvent
from events.ImportEvent import ImportEvent
from events.ClickFileNameEvent import ClickFileNameEvent
from events.OpenDialogEvent import OpenDialogEvent
from events.DeleteDbRecordEvent import DeleteDbRecordEvent
from events.ReloadFileListEvent import ReloadFileListEvent

class MainController(QMainWindow, Ui_MainWindow):

    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        self.treeFile.setHeaderLabel("Files")

        appService = AppConfigService()
        config = appService.get()

        self.inputDirPath.setText(config.default_path)

        self.reloadFileListEvent = ReloadFileListEvent(self)
        self.btnLoadFiles.clicked.connect(self.reloadFileListEvent.run)

        self.openDialogEvent = OpenDialogEvent(self)
        self.showFormAddDb.clicked.connect(self.openDialogEvent.run)

        self.deleteDbRecordEvent = DeleteDbRecordEvent(self)
        self.btnDeleteRecordDb.clicked.connect(self.deleteDbRecordEvent.run)

        self.eventExport = ExportEvent(self)
        self.btnExport.clicked.connect(self.eventExport.run)
        
        self.eventImport = ImportEvent(self)
        self.btnImport.clicked.connect(self.eventImport.run)

        self.eventClickFileName = ClickFileNameEvent(self)
        self.treeFile.itemClicked.connect(self.eventClickFileName.run)

        self.loadListDb()
        self.btnLoadFiles.click()

    def loadListDb(self):
        self.comboBoxListDb.clear()

        configDbRepository = ConfigDbRepository()
        list = configDbRepository.findAll()

        for dbConfig in list:
            labelName = dbConfig.name
            self.comboBoxListDb.addItem(labelName , dbConfig.type_db)
