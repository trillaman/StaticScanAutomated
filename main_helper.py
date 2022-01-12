import os
import re
import sys
from dotenv import load_dotenv

class MainHelper:
    # TODO DEFINE TYPE OF FILE TO SCAN eg. if zip then unzip first
    def get_file_by_extension(self, file):
        split_tup = os.path.splitext(file)
        file_extension = split_tup[1]

        return file_extension

    def get_filename(self, filepath):
        split_tup = filepath.split("/")
        for i in range(len(split_tup)):
            filename = split_tup[-1]
        filename = filename.split(".")
        return filename[0]

    def unzip_file(self, file):
        unzip_cmd = "unzip -d " + os.getcwd() + "/unzipped " + file
        try:
            os.system(unzip_cmd)
        except Exception:
            print("Couldn't unzip file" + file)
        finally:
            print("File " + file + " unzipped")

        return True

    def set_slashes(self, path):
        if os.platform.system() == 'Windows':
            path2 = path.replace("/", "\\")
            return path2
        elif os.platform.system() == 'Linux':
            return path
        else:
            print("Unknown platform")
            return path