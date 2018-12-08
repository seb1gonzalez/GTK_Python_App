from ProtoElement import ProtoElement


class Packet:

    def __init__(self, packet):
        self.name = ""
        self.proto = []
        self.size = packet[0].get('size')       # geninfo proto contains packet size

        for element in packet:
            # contains proto elements
            self.proto.append(ProtoElement(element))

    def getsize(self):
        return self.size

    def getprotos(self):
        return self.proto

    def getproto(self, index):
        return self.proto[index]

    def remove_proto(self, protoindex):
        del self.proto[protoindex]

    def contains(self, proto_name):
        for pr in self.proto:
            if pr.getname() == proto_name:
                return True
        return False

