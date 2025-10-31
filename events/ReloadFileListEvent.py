from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 
from services.AppConfigService import AppConfigService
from services import FileService
from PyQt6.QtWidgets import QTreeWidgetItem

class ReloadFileListEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        appConfigService = AppConfigService()
        fileService = FileService()

        self.application.treeFile.clear()

        dir = self.application.inputDirPath.text()

        for name in fileService.get_file_list(dir, 'sql'):
            item = QTreeWidgetItem([name])
            self.application.treeFile.addTopLevelItem(item)

        appConfigService.set(default_path = self.application.inputDirPath.text())
