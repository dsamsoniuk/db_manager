
from PyQt6 import QtCore

class MemoryService:

    def __init__(self):
        self.memory = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
    
    def get(self, name: str, default: any):
        return self.memory.value(name, default)
    
    def set(self, name: str, value: any):
        self.memory.setValue(name, value)