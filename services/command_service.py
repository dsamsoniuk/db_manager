
import subprocess

class CommandService:

    def exec(self, command: str):
        """ Execute command bash """
        
        subprocess.run(command, shell=True, text=True, capture_output=True, check=True)