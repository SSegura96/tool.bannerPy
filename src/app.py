from src.settings import Settings
from src.github import Github
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
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print('Error: couldn\'t find "banner.info" file please run the "pull" operation first')


def pull_banner_content(settings, git):
    resp = input("Are you sure you want to download the remote banner for {settings['current_hostname']}? (y/N)")
    if resp == "y":
        git_file = git.get_file_by_hostname(settings["current_hostname"])
        file_content = git_file["content"]
        write_file(settings["banner_path"], file_content)
        return "Banner File Successfully Downloaded"
    return "No changes were applied"


def push_banner_content(settings, git):
    resp = input(f"Are you sure you want to upload your local banner for {settings['current_hostname']}? (y/N)")
    if resp == "y":
        banner_content = read_file(settings["banner_path"])
        git.update_file(settings["current_hostname"], banner_content)
        return "Banner File Successfully Uploaded"
    return "No changes were applied"


def main():
    settings = Settings.get_settings()
    git = Github()

    if len(sys.argv) > 1:
        if sys.argv[1] == "pull":
            show_processing_message(settings["os"])
            message = pull_banner_content(settings, git) 
        elif sys.argv[1] == "push":
            show_processing_message(settings["os"])
            message = push_banner_content(settings, git)
        else:
            message = "Error: the operation was not found"
        print(message)
    else:
        clear_screen(settings["os"])
        banner_content = read_file(settings["banner_path"])
        if settings["has_neofetch"]:
            print(os.popen("neofetch").read() + "\n")
        if banner_content is not None: 
            print(banner_content)


if __name__ == '__main__':
    exit(main())
