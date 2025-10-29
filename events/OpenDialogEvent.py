

from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 
from controllers.DbConfigController import DbConfigController

class OpenDialogEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self):
        dialog = DbConfigController()
        if dialog.exec(): 
            value = dialog.getMessage()
            self.application.textBrowser.setText(value)
            self.application.loadListDb()