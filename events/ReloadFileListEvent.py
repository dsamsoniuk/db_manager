

from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 
from services.AppConfigService import AppConfigService
import os
from PyQt6.QtWidgets import QTreeWidgetItem

class ReloadFileListEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        appService = AppConfigService()
        dir = self.application.inputDirPath.text()

        try:
            self.application.treeFile.clear()
            for name in os.listdir(dir):
                if name.endswith(".sql"):
                    item = QTreeWidgetItem([name])
                    self.application.treeFile.addTopLevelItem(item)

            appService.set(default_path = self.application.inputDirPath.text())
        except:
            self.application.textBrowser.setText('Nie udalo sie pobrac plików')
