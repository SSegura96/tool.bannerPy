from pathlib import Path
from utils import Utils
import socket
import json
import os


class Settings:
    APP_CONFIG_PATH = os.path.join(str(Path.home()), ".bannerpy")
    CONFIG_FILENAME = "config.json"
    CONFIG_FILENAME_EXAMPLE = "config.example.json"
    BANNER_FILENAME = "banner.info"
    BANNER_FILENAME_EXAMPLE = "banner.example.info"

    @classmethod
    def __generate_setting(self, filename_example, filename):

        settings_example_path = os.path.join(
            os.getcwd(), filename_example)

        settings_path = os.path.join(self.APP_CONFIG_PATH, filename)

        Utils.copy_file(settings_example_path, settings_path)

    @classmethod
    def check_config_files(self):
        configuration = True
        # Check if app folder exist
        if not Utils.check_folder_exist(self.APP_CONFIG_PATH):
            Utils.create_folder(self.APP_CONFIG_PATH)
            configuration = False
        # Check if config exist
        config_path = os.path.join(self.APP_CONFIG_PATH,
                                   self.CONFIG_FILENAME)
        if not Utils.check_file_exist(config_path):
            self.generate_config()
            configuration = False
        # Check if banner exist
        banner_path = os.path.join(self.APP_CONFIG_PATH,
                                   self.BANNER_FILENAME)
        if not Utils.check_file_exist(banner_path):
            self.generate_banner()
            os.system("cls || clear")
            print(Utils.read_file(banner_path))
            configuration = False
        return configuration

    @classmethod
    def generate_config(self):
        self.__generate_setting(
            self.CONFIG_FILENAME_EXAMPLE, self.CONFIG_FILENAME)

    @classmethod
    def generate_banner(self):
        self.__generate_setting(
            self.BANNER_FILENAME_EXAMPLE, self.BANNER_FILENAME)

    @ classmethod
    def get_settings(self):
        config_path = os.path.join(str(Path.home()), ".bannerpy",
                                   self.CONFIG_FILENAME)
        banner_path = os.path.join(str(Path.home()),
                                   ".bannerpy", self.BANNER_FILENAME)
        try:
            settings = {
                "current_hostname": socket.gethostname(),
                "settings_path": config_path,
                "banner_path": banner_path
            }

            # Process Json data
            json_file = open(config_path)
            data = json.load(json_file)

            # Get GitHub settings
            settings["gist_url"] = data["github"]["gist_url"]
            settings["auth_token"] = data["github"]["auth_token"]

            if settings["gist_url"] == "" or settings["auth_token"] == "":
                raise Exception("Error: Missing github configuration")

            # Get hostname settings
            settings["os"] = data["settings"]["os"]
            settings["has_neofetch"] = bool(
                data["settings"]["has_neofetch"])

            return settings
        except KeyError:
            hostname = settings["current_hostname"]
            print(f"Error: there's no configuration for the hostname {hostname} \
                    review the config.json file")
            return None
        except FileNotFoundError:
            print("Error: couldn't found the configuration files at ~/.bannerpy")
        except Exception:
            print(
                "Error: Please review the config file at ~/.bannerpy/config.json")
            return None
