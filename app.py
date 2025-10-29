import sys
from PyQt6.QtWidgets import QApplication
# from dotenv import load_dotenv
from controllers.MainApp import MainApp
# from services.MemoryService import MemoryService
# load_dotenv()

def main():

    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()