import pathlib
import shutil
import os


class Utils:

    @classmethod
    def copy_file(self, origin, destiny):
        shutil.copyfile(origin, destiny)

    @classmethod
    def write_file(self, file_path, body):
        with open(file_path, "w") as file:
            file.write(body)

    @classmethod
    def read_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(
                'Error: couldn\'t find "banner.info" file please run the "pull" operation first')

    @classmethod
    def check_file_exist(self, file_path):
        try:
            with open(file_path):
                return True
        except IOError:
            return False

    @classmethod
    def check_folder_exist(self, folder_path):
        return pathlib.Path(folder_path).is_dir()

    @classmethod
    def create_folder(self, folder_path):
        os.mkdir(folder_path)
