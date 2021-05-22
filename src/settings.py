from pathlib import Path
import json
import os


class Settings:
    @classmethod
    def get_settings(self):
        try:
            settings = {
                "current_hostname": os.popen("hostname").read().strip(),
                "banner_path": os.path.join(str(Path.home()), "banner.info")
            }

            # Process Json data
            json_file = open(os.path.join(str(Path.home()), ".config.json"))
            data = json.load(json_file)

            # Get GitHub settings
            settings["gist_url"] = data["github"]["gist_url"]
            settings["auth_token"] = data["github"]["auth_token"]

            # Get hostname settings
            settings["os"] = data["hostnames"][settings["current_hostname"]]["os"]
            settings["has_neofetch"] = bool(data["hostnames"][settings["current_hostname"]]["has_neofetch"])

            return settings
        except KeyError:
            hostname = settings["current_hostname"]
            print(f"Error: there's no configuration for the hostname {hostname} \
                    review the config.json file")
        except FileNotFoundError:
            path = str(os.path.join(str(Path.home()), ".config.json"))
            print(f"Error: couldn't find the config.json file at path {path}")
