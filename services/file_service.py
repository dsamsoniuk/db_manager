
import os

class FileService:

    def get_file_list(self, dir_path: str, format: str = 'sql'):
        """ Get file list in dir """
        
        fileList = []
        if os.path.isdir(dir_path) == False:
            return fileList
        
        for name in os.listdir(dir_path):
            if name.endswith("." + format):
                fileList.append(name)
        return fileList
