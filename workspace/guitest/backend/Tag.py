

class Tag:

    def __init__(self, the_name, the_description, the_field_name):
        self.name = the_name
        self.description = the_description
        self.field_name = the_field_name

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_field_name(self):
        return self.field_name

    def set_name(self, the_name):
        self.name = the_name

    def set_description(self, the_description):
        self.description = the_description

    def set_field_name(self, the_field_name):
        self.field_name = the_field_name
