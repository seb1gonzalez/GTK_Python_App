from Field import Field


class ProtoElement:

    def __init__(self, proto):
        self.field = []         # contains fields of this protocol
        self.attrib = proto.attrib

        for element in proto:
            self.field.append(Field(element))

    def getfields(self):
        return self.field

    def getfield(self, index):
        return self.field[index]

    def getname(self):
        return self.attrib['name'] if 'name' in self.attrib else ""

    def getshowname(self):
        return self.attrib['showname'] if 'showname' in self.attrib else ""

    def getsize(self):
        return self.attrib['size'] if 'size' in self.attrib else ""

    def get_dictattrib(self):
        return self.attrib
