

from events.AbstractEvent import AbstractEvent
from views.main import Ui_MainWindow 

class ClickFileNameEvent(AbstractEvent):

    def __init__(self, application: Ui_MainWindow):
        self.application = application

    def run(self, item, column):
        filePath = self.application.inputDirPath.text() + item.text(column)
        self.application.inputCurrentFile.setText(filePath)