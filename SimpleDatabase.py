import hashlib


class SimpleDatabase:
    __files: dict
    __commit: list
    __read_file_size: int = 1024

    def update_file(self, filename: str, relative_path: str):
        if self.is_file_registered(filename, relative_path):
            md5_dig: str = self.__get_md5(filename, relative_path)
            if not self.__files[filename]["md5"] == md5_dig:
                # File updated
                self.__files[filename] = self.__get_file_data_no_md5(filename, relative_path, md5_dig)
            else:
                # Do nothing
                pass
        else:
            self.__files[filename] = self.__get_file_data(filename, relative_path)
            pass

    def is_file_registered(self, filename: str, relative_path: str) -> bool:
        return filename in self.__files and self.__files[filename]["path"] == relative_path

    def __get_md5(self, filename: str, relative_path: str) -> str:
        md5 = hashlib.md5()
        with open(f"./{relative_path}/{filename}", 'rb') as f:
            while True:
                data = f.read(self.__read_file_size)
                if not data:
                    break
                md5.update(data)
                if data.__len__() < self.__read_file_size:
                    break
        return md5.hexdigest()

    def __get_file_data(self, filename: str, relative_path: str) -> dict:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        with open(f"./{relative_path}/{filename}", 'rb') as f:
            while True:
                data = f.read(self.__read_file_size)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha256.update(data)
                if data.__len__() < self.__read_file_size:
                    break
        return {"md5": md5.hexdigest(), "sha1": sha1.hexdigest(), "sha256": sha256.hexdigest(), "path": relative_path}

    def __get_file_data_no_md5(self, filename: str, relative_path: str, md5_dig: str) -> dict:
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        with open(f"./{relative_path}/{filename}", 'rb') as f:
            while True:
                data = f.read(self.__read_file_size)
                if not data:
                    break
                sha1.update(data)
                sha256.update(data)
                if data.__len__() < self.__read_file_size:
                    break
        return {"md5": md5_dig, "sha1": sha1.hexdigest(), "sha256": sha256.hexdigest(), "path": relative_path}

