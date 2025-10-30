
import os

class FileService:

    def getFileListInDir(self, path: str, format: str = 'sql'):
        """
        Get file list in dir
        """
        fileList = []
        if os.path.isdir(path) == False:
            return fileList
        
        for name in os.listdir(path):
            if name.endswith("." + format):
                fileList.append(name)
        return fileList
