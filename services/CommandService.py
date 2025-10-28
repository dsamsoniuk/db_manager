
import subprocess

class CommandService:
    stdout: str = ''
    def exec(self, command: str):
        print('exec:' + command)
        results = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        # print(results.stdout)
        self.stdout = results.stdout