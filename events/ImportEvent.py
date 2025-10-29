
from builders.AbstractDbManager import AbstractDbManager
from builders.DbManager import DbManager
from services.CommandService import CommandService
from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 

class ImportEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        fileName = self.application.inputCurrentFile.text()
        title = self.application.comboBoxListDb.currentText()

        if fileName == '' or title == '':
            self.application.textBrowser.setText("Please chooice filename and db")
            return
        
        configDbService = DbManager()
        dbManager = configDbService.getManagerByTitle(title)

        if isinstance(dbManager, AbstractDbManager) == False:
            self.application.textBrowser.setText("No manager")

        try:
            commandservice = CommandService()
            commandservice.exec(dbManager.getImportCommand(fileName))
            self.application.textBrowser.setText('Import from DB done!')

        except Exception as e:
            self.application.textBrowser.setText(repr(e))

        self.application.btnLoadFiles.click()