from github_api_implementation import GithubApiImplementation as githubAPI
from settings import Settings
from menu import Menu
from utils import Utils
import sys
import os


def show_banner(settings):
    banner_content = os.popen("cat "+settings["banner_path"]).read()
    if banner_content != "":
        if settings["has_neofetch"]:
            print(os.popen("neofetch").read() + "\n")
        return banner_content
    return "The banner is empty try running bannerpy pull"


def init_banner(settings, git):
    message = "Are you sure that you want to initialize a banner?"
    if Menu.show_confimation(message):
        banner_content = Utils.read_file(settings["banner_path"])
        git.update_file(settings["current_hostname"], banner_content)
        return "Banner File Successfully Created"
    return "No changes were applied"


def pull_banner(settings, git):
    message = "Are you sure you want to download the remote banner?"
    if Menu.show_confimation(message):
        git_file = git.get_file_by_hostname(settings["current_hostname"])
        file_content = git_file["content"]
        Utils.write_file(settings["banner_path"], file_content)
        return "Banner File Successfully Downloaded"
    return "No changes were applied"


def push_banner(settings, git):
    message = "Are you sure you want to upload your local banner?"
    if Menu.show_confimation(message):
        banner_content = Utils.read_file(settings["banner_path"])
        git.update_file(settings["current_hostname"], banner_content)
        return "Banner File Successfully Uploaded"
    return "No changes were applied"


def main():
    isOk = Settings.check_config_files()
    if isOk:
        settings = Settings.get_settings()
        if settings is not None:
            git = githubAPI(settings["gist_url"], settings["auth_token"])
            Menu.show_greet()
            if len(sys.argv) > 1:
                # Runned with init
                if sys.argv[1] == "init":
                    Menu.show_processing_message()
                    message = init_banner(settings, git)

                # Runned with pull
                elif sys.argv[1] == "pull":
                    Menu.show_processing_message()
                    message = pull_banner(settings, git)

                # Runned with push
                elif sys.argv[1] == "push":
                    Menu.show_processing_message()
                    message = push_banner(settings, git)
                else:
                    message = "Error: the operation was not found"

            elif len(sys.argv) == 1:
                # Runned without argumens
                message = show_banner(settings)
            else:
                message = "Error: Only 0-1 arguments are available"
            Menu.clear_screen()
            print(message)


if __name__ == '__main__':
    exit(main())
