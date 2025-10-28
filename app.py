import sys
from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv
from controllers.MainApp import MainApp
from services.MemoryService import MemoryService
load_dotenv()

def main():

    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    # dto = ConfigDto()
    # dto.current_db = "mysql testt"
    # # print(dto)
    # memory = MemoryService()
    # memory.set('wizardwebsshport', dto)
    # print(memory.get('list_config_db')[0].type_db)
    # print(memory.get('test'))

    # settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
    # print(settings.fileName())
    # settings.setValue('wizardwebsshport', [23,454])
    # keys = settings.value('wizardwebsshport')[0]
    # print(keys)


    sys.exit(app.exec())

if __name__ == "__main__":
    main()