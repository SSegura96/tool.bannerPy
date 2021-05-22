from src.settings import Settings
import requests
import json


class Github():
    def __init__(self):
        settings = Settings.get_settings()

        self.url = settings["gist_url"]
        self.headers = {
            'Authorization': f'Token {settings["auth_token"]}',
            'Content-Type': 'application/json'
        }

    def __get_request(self):
        response = requests.request(
            "GET", url=self.url, headers=self.headers)
        return json.loads(response.text)

    def __patch_request(self, body):
        response = requests.request(
            "PATCH", url=self.url, headers=self.headers, data=body)
        return json.loads(response.text)

    def get_all_files(self):
        response = self.__get_request()
        return response["files"]

    def get_file_by_hostname(self, hostname):
        response = self.__get_request()
        return response["files"][hostname]

    def update_file(self, hostname, content):
        body = json.dumps({"files": {hostname: {"content": content}}})
        self.__patch_request(body)
