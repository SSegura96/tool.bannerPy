from settings import Settings
from github import Github
import sys
import os


def clear_screen(os_type):
    keyword = ""
    if os_type == "Windows":
        keyword = "cls"
    else:
        keyword = "clear"
    os.system(keyword)


def show_processing_message(host_os):
    clear_screen(host_os)
    username = os.popen("whoami").read().strip()
    print(f"Welcome back {username} !!!")
    print("Processing ...")


def write_file(file_path, body):
    with open(file_path, "w") as file:
        file.write(body)


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def pull_banner_content(settings, git):
    git_file = git.get_file_by_hostname(settings["current_hostname"])
    file_content = git_file["content"]
    write_file(settings["banner_path"], file_content)


def push_banner_content(settings, git):
    banner_content = read_file(settings["banner_path"])
    git.update_file(settings["current_hostname"], banner_content)


if __name__ == '__main__':
    settings = Settings.get_settings()
    git = Github()

    if len(sys.argv) > 1:
        if sys.argv[1] == "pull":
            show_processing_message(settings["os"])
            pull_banner_content(settings, git)
            message = "Banner File Successfully Downloaded"
        elif sys.argv[1] == "push":
            show_processing_message(settings["os"])
            push_banner_content(settings, git)
            message = "Banner File Successfully Uploaded"
        else:
            message = "Error: the operation was not found"
        print(message)
    else:
        clear_screen(settings["os"])
        banner_content = read_file(settings["banner_path"])
        if settings["has_neofetch"]:
            print(os.popen("neofetch").read() + "\n")
        print(banner_content)
