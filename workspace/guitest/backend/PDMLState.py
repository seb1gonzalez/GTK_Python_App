from xml.etree.ElementTree import parse
from Packet import Packet


class PDMLState:

    def __init__(self, pdml_file):
        # PDML state information
        self.packet = []
        self.name = ""
        self.analyst = ""
        self.description = ""
        self.timestamp = ""
        self.date = ""
        self.stage = ""

        # Create pdml tree from given pdml_file
        pdml_tree = parse(pdml_file)
        pdml = pdml_tree.getroot()

        # saving packets of this pdml
        for element in pdml:
            self.packet.append(Packet(element))

    def getpackets(self):
        return self.packet

    def getpacket(self, index):
        return self.packet[index]

    def remove_packet(self, index):
        print self.packet
        del self.packet[index]
