from PDMLState import PDMLState
from DatabaseHandler import DatabaseHandler

class Session:

    def __init__(self, the_name, the_description, the_pdml=None):
        # session information
        self.name = the_name
        self.description = the_description
        self.pdmlstate = the_pdml

    def add_pdmlstate(self, pdmlfile):
        self.pdmlstate = PDMLState(pdmlfile)
        self.save_pdmlstate()
        return self.pdmlstate

    def save_pdmlstate(self):
        db = DatabaseHandler()
        db.save_pdmlstate(self.pdmlstate)

    def delete_pdmlstate(self, pdmlname):
        return True

    def rename_pdmlstate(self, newname):
        return True

    def open_pdmlstate(self, pdmlname):
        return True
