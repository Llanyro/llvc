from pathlib import Path
from os.path import exists
from os import walk, getcwd
from utils import get_platform, Platform
from SimpleDatabase import SimpleDatabase
import hashlib
import argparse


class llvc_client:
    __actual_root: str
    __settings_folder: str = ".llvc"
    __platform: Platform
    __database: SimpleDatabase

    __banned_extensions: list = []
    __banned_folders: list = []


    def __init__(self):
        #self.__actual_root = getcwd()
        self.__actual_root = "C:\\Users\\Fran-Administrador\\Documents\\GitHub\\Llanylib\\UsefulScripts"
        self.__platform = get_platform()
        self.__database = SimpleDatabase()

    # region Utils
    def __file_in_banned_folder(self, p: str) -> bool:
        return any([p.__contains__(folder) for folder in self.__banned_folders])

    def __is_banned_folder(self, p: str) -> bool:
        return p in self.__banned_folders

    def __has_banned_extension(self, p: str) -> bool:
        return any([p.__contains__(extension)] for extension in self.__banned_extensions)


    # endregion
    # region Checkers
    def check_all(self):
        self.__check_settings()

    def __check_settings(self) -> None:
        if exists(f"./{self.__settings_folder}/settings"):
            pass
        else:
            raise Exception("Settings file not found")

    # endregion
    # region File control
    def add(self):
        """
        Add does the same as 'git add .'
        """
        for root, subFolder, files in walk("C:\\Users\\Fran-Administrador\\Documents\\GitHub\\Llanylib\\UsefulScripts"):
            relative_path: str = root.split(self.__actual_root)[1]
            if relative_path.__len__() == 0:
                relative_path = "."
            else:
                if self.__platform == Platform.WINDOWS:
                    relative_path = relative_path[2:]
                elif self.__platform == Platform.UNIX:
                    relative_path = relative_path[1:]

            if not self.__is_banned_folder(relative_path):
                for file in files:
                    self.__database.update_file(file, relative_path)


client = llvc_client()
client.add()

"""if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script is a DHCP starvation attack.")
    parser.add_argument("-s", "--secondDelay", required=False, help="Seconds to delay the function")
    parser.add_argument("-i", "--iteration", required=False, help="Number of fakes device to connect (without counting threads)")
    parser.add_argument("-f", "--forks", required=False, help="Number of forks. Remember that forks=2^N (default 4=2^4=16)")
    args = parser.parse_args()"""


        #for a_file in Path(self.__root):
"""        for a_file in walk("C:\\Users\\Fran-Administrador\\Documents\\GitHub\\Llanylib\\UsefulScripts"):
            var: str = str(a_file)
            # If file is not a cpp
            if not self.__has_banned_extension(var):
                # If the file is in banned folder
                if not self.__file_in_banned_folder(var):
                    file_list.append(var)
"""
