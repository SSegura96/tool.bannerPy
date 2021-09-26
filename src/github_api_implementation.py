import requests
import json


class GithubApiImplementation():
    def __init__(self, githubAPI_url, githubAPI_token):
        self.url = githubAPI_url
        self.headers = {
            'Authorization': "Token " + githubAPI_token,
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
