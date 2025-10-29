

from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 
from services.ConfigDbRepository import ConfigDbRepository

class DeleteDbRecordEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        recordDbname = self.application.comboBoxListDb.currentText()
        configDbRepository = ConfigDbRepository()
        configDbRepository.delete(recordDbname)
        self.application.loadListDb()