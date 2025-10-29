
from builders.AbstractDbManager import AbstractDbManager
from builders.DbManager import DbManager
from services.CommandService import CommandService
from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 

class ExportEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        fileName = self.application.inputCurrentFile.text()
        title = self.application.comboBoxListDb.currentText()

        if fileName == '' or title == '':
            self.application.textBrowser.setText("Brak wybranej nazwy pliku lub bazy")
            return
        
        configDbService = DbManager()
        dbManager = configDbService.getManagerByTitle(title)

        if isinstance(dbManager, AbstractDbManager) == False:
            self.application.textBrowser.setText("Brak db managera")

        try:
            commandservice = CommandService()
            commandservice.exec(dbManager.getExportCommand(fileName))
            self.application.textBrowser.setText('Export z bazy do pliku wykonany!')

        except Exception as e:
            self.application.textBrowser.setText(repr(e))

        self.application.pushButton.click()