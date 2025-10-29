
import subprocess

class CommandService:

    def exec(self, command: str):
        subprocess.run(command, shell=True, text=True, capture_output=True, check=True)