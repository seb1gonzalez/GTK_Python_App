from DatabaseHandler import DatabaseHandler
from PDMLState import PDMLState


class DisplayFilter:

    def __init__(self):
        # DisplayFilter knows the following information
        self.filter = {}

    def getfilters(self):
        return self.filter.items()

    def add_filter(self, name, expression):
        if name in self.filter:#if already exists
            return False
        else:#if does not exist, then add it
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
        print_flag = True
        name_list = name.split('||')
        for n in range(len(name_list)):
            if self.filter.get(name_list[n]) == None:
                self.add_filter(name_list[n],name_list[n])
                if print_flag:
                    print 'Added filter(s)\n' + name_list[n]
                    print_flag = False

                else:
                    print name_list[n]

        packet = pdmlstate.getpackets()  # list of Packets in pdml
        pi, packet_len = 0, len(packet)
        proto_names = self.filter.keys()  # list of filter keys
        pn,names_len = 0,len(proto_names)

        while pn < names_len:
            while pi < packet_len:
                print 'current filter is: '+proto_names[pn]
                if packet[pi].contains(proto_names[pn]):
                    print 'found '+ proto_names[pn]
                    pi += 1
                    pn += 1
                    break

                else:
                    pdmlstate.remove_packet(pi)
                    packet_len -= 1
                    break
            pn += 1




       

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


filter.filter_out('tcp||icmp||dns',pdmlstate)




