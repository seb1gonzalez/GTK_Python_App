

class MessageType:

    def __init__(self, the_name, the_color, the_fieldpairs):
        # A Message Type knows the following information
        self.name = the_name
        self.color = the_color
        self.fieldpairs = the_fieldpairs
        self.template_fieldpairs = []

    def set_name(self, the_name):
        self.name = the_name

    def set_fieldpairs(self, the_fieldpairs):
        self.fieldpairs = the_fieldpairs

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_fieldpairs(self):
        return self.fieldpairs


class FieldValuePair:

    def __init__(self, the_name, the_value):
        # A Field Value Pair knows the following information
        self.name = the_name
        self.value = the_value

    def getname(self):
        return self.name

    def getvalue(self):
        return self.value
