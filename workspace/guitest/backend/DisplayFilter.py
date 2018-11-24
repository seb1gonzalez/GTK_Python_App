from DatabaseHandler import DatabaseHandler
from PDMLState import PDMLState


class DisplayFilter:

    def __init__(self):
        # DisplayFilter knows the following information
        self.filter = {}

    def getfilters(self):
        return self.filter.items()

    def add_filter(self, name, expression):
        if name in self.filter:
            return False
        else:
            self.filter[name] = _Filter(name, expression)
            return True

    def save_filter(self):
        db = DatabaseHandler()
        db.save_filters(self.filter.items())

    def delete_filter(self, name):
        if name in self.filter:
            del self.filter[name]
            return True
        else:
            return False

    def update_filter(self, name, new_name, new_expression):
        if self.delete_filter(name):
            return self.add_filter(new_name, new_expression)
        else:
            return False

    def filter_out(self, name, pdmlstate):
        print pdmlstate.getpackets()
        if name in self.filter:
            filter = self.filter[name]
            packet = pdmlstate.getpackets() #list of Packets in pdml
            proto_names = filter.name.split("||")

            pi = 0
            packet_len = len(packet)
            while pi < packet_len:
                for proto_name in proto_names:
                    if packet[pi].contains(proto_name):
                        print 'found '+ proto_name
                        pi += 1
                    else:
                        print pdmlstate.remove_packet(pi)
                        packet_len -= 1

        print pdmlstate.getpackets()


       

        return False


class _Filter:

    def __init__(self, the_name, the_expression):
        # a Filter knows the following information
        self.name = the_name
        self.expression = the_expression

    def update(self, new_name, new_expression):
        self.name = new_name
        self.expression = new_expression

    def get_name(self):
        return self.name
    def get_expression(self):
        return self.expression



pdmlstate = PDMLState('../output2.pdml')
filter = DisplayFilter()
filter.add_filter('icmp','icmp')
filter.add_filter('tcp','tcp')

filter.filter_out('icmp',pdmlstate)




