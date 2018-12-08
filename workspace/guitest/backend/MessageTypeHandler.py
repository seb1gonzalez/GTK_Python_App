from MessageType import MessageType
from MessageType import FieldValuePair
import random


class MessageTypeHandler:

    def __init__(self):
        self.msgtypes = {}
        self.add_msgtype("tst", [("tcp.port", "")])

    def getmsgtypes(self):
        return self.msgtypes.values()

    def getmsgtype(self, name):
        return self.msgtypes[name] if name in self.msgtypes else None

    def add_msgtype(self, msgtype_name, pairs):
        if msgtype_name in self.msgtypes or len(pairs) < 1:
            return False
        else:
            color = self._generatecolor()
            fieldpairs = self._generate_fieldpairs(pairs)
            self.msgtypes[msgtype_name] = MessageType(msgtype_name, color, fieldpairs)
            return True

    def delete_msgtype(self, name):
        if name in self.msgtypes:
            del self.msgtypes[name]
            return True
        else:
            return False

    def update_msgtype(self, old_name, new_name, new_pairs):
        if old_name in self.msgtypes and (new_name == old_name or new_name not in self.msgtypes):
            msgtype = self.msgtypes[old_name]
            msgtype.set_name(new_name)
            msgtype.set_fieldpairs(self._generate_fieldpairs(new_pairs))
            self.delete_msgtype(old_name)
            self.msgtypes[new_name] = msgtype
            return True
        else:
            return False

    def classify_proto(self, msgtype_name, proto):
        msgtype = self.msgtypes[msgtype_name]
        fv_pairs = msgtype.get_fieldpairs()

        for pair in fv_pairs:
            if proto.find(pair.getname(), pair.getvalue()) is False:
                return False

        return True

    def _generatecolor(self):
        r = lambda: random.randint(130, 230)
        return '#%02X%02X%02X' % (r(), r(), r())

    def _generate_fieldpairs(self, pairs):
        fieldpairs = []
        for pair in pairs:
            name, value = pair
            fieldpairs.append(FieldValuePair(name, value))
        return fieldpairs

