from Session import Session


class Workspace:

    def __init__(self, the_name, the_session=None):
        # Workspace information
        self.name = the_name
        self.session = the_session

    def getsession(self):
        return self.session

    def add_session(self, name="", description=""):
        self.session = Session(name, description)
        return self.session

    def save_workspace(self, pdmlstate):
        return True

    def open_workspace(self, pdmlname):
        return True

    def switch_workspace(self, pdmlname):
        return True
