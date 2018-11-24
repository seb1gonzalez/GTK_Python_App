from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring
from xml.dom import minidom


class DatabaseHandler:

    def __init__(self):
        self.path = "/storage/"

    def save_pdmlstate(self, pdmlstate):
        top = Element('pdml')
        top.set('version', '1.0')

        packets = pdmlstate.getpackets()
        for packet in packets:
            child_packet = SubElement(top, 'packet')

            protos = packet.getprotos()
            for proto in protos:
                child_proto = SubElement(child_packet, 'proto', proto.get_dictattrib())

                fields = proto.getfields()
                for field in fields:
                    child_field = SubElement(child_proto, 'field', field.get_dictattrib())

                    ifields = field.get_internalfields()
                    for ifield in ifields:
                        SubElement(child_field, 'field', ifield.get_dictattrib())

        f = open("pdmlstate.pdml", "w+")

        rough_string = tostring(top, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        f.write(reparsed.toprettyxml())
        f.close()

    def save_filters(self, filters):
        filters_dict = {}

        for f in filters:
            filters_dict[f.name] = f.expression

        print(filters_dict)



