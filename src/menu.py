import os


class Menu:
    @classmethod
    def show_greet(self):
        username = os.popen("whoami").read().strip()
        print(f"Welcome back {username} !!!\n")

    @classmethod
    def clear_screen(self):
        os.system("clear")

    @classmethod
    def show_processing_message(self):
        self.clear_screen()
        print("Processing ...\n")

    @classmethod
    def show_confimation(self, message):
        self.clear_screen()
        resp = input(message+" (y/N)"+"\n").lower()
        if resp == "y":
            return True
        return False
