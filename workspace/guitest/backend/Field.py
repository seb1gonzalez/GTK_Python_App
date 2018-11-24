

class Field:

    def __init__(self, field):
        self.internal_field = []
        self.attrib = field.attrib  # dictionary containing attributes
        self.entropy = "0"

        for element in field:
            self.internal_field.append(Field(element))  # some fields may have internal fields

    # Get attributes
    def getname(self):
        return self.attrib['name'] if 'name' in self.attrib else ""

    def getshowname(self):
        return self.attrib['showname'] if 'showname' in self.attrib else ""

    def getsize(self):
        return self.attrib['size'] if 'size' in self.attrib else ""

    def getposition(self):
        return self.attrib['pos'] if 'pos' in self.attrib else ""

    def getshow(self):
        return self.attrib['show'] if 'show' in self.attrib else ""

    def getvalue(self):
        if self.getname() is "eth.dst":
            print self.attrib['value']
        return self.attrib['value'] if 'value' in self.attrib else ""

    def getentropy(self):
        return self.entropy

    def get_internalfields(self):
        return self.internal_field

    def get_iternalfield(self, index):
        return self.internal_field[index]

    # Modify fields
    def set_name(self, new_name):
        self.attrib['name'] = new_name

    def set_showname(self, new_showname):
        self.attrib['showname'] = new_showname

    def set_size(self, new_size):
        self.attrib['size'] = new_size

    def set_value(self, new_value):
        self.attrib['value'] = new_value

    def get_dictattrib(self):
        return self.attrib
