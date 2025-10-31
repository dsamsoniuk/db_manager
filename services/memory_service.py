
from PyQt6 import QtCore

class MemoryService:

    def __init__(self):
        self.memory = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
    
    def get(self, name: str, default: any):
        """ Get data from memory """
        
        return self.memory.value(name, default)
    
    def set(self, name: str, value: any):
        """ Set data to memory """

        self.memory.setValue(name, value)