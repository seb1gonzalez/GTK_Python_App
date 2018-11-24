from Workspace import Workspace


class User:

    def __init__(self, the_name="", the_workspace=None):
        # User information
        self.name = the_name
        self.workspace = the_workspace

    def getname(self):
        return self.name

    def getworkspace(self):
        return self.workspace

    def add_workspace(self, name=""):
        self.workspace = Workspace(name)  # create empty workspace
        return self.workspace

    def save_workspace(self):
        return True

    def open_workspace(self, workspace_name):
        return True

    def switch_workspace(self, workspace_name):
        return True
