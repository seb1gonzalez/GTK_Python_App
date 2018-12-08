from DatabaseHandler import DatabaseHandler


class DisplayFilter:

    def __init__(self):
        # DisplayFilter knows the following information
        self.filter = {}

    def getfilters(self):
        return self.filter.values()

    def add_filter(self, name, expression):
        if name in self.filter:
            return False
        else:
            self.filter[name] = _Filter(name, expression)
            return True

    def save_filter(self):
        db = DatabaseHandler()
        db.save_filters(self.filter.values())

    def delete_filter(self, name):
        if name in self.filter:
            del self.filter[name]
            return True
        else:
            return False

    def update_filter(self, old_name, new_name, new_expression):
        if old_name in self.filter and (new_name == old_name or new_name not in self.filter):
            single_filter = self.filter[old_name]
            single_filter.update(new_name, new_expression)
            self.delete_filter(old_name)
            self.filter[new_name] = single_filter
            return True
        else:
            return False

    def filter_by_name(self, name, pdmlstate):
        if name in self.filter:
            single_filter = self.filter[name]
            self.filter_by_expr(single_filter.get_expression(), pdmlstate)

    def filter_by_expr(self, expression, pdmlstate):
        expression = expression.replace(" ", "")  # remove spaces in the expression
        proto = expression.split('||')

        packet = pdmlstate.getpackets()
        plen = len(packet) - 1

        while plen >= 0:
            was_found = False
            for pr in proto:
                print pr
                if packet[plen].contains(pr):
                    was_found = True
                    break
            if was_found is False:
                pdmlstate.remove_packet(plen)
            plen -= 1


class _Filter:

    def __init__(self, the_name, the_expression):
        # a Filter knows the following information
        self.name = the_name
        self.expression = the_expression

    def get_name(self):
        return self.name

    def get_expression(self):
        return self.expression

    def update(self, new_name, new_expression):
        self.name = new_name
        self.expression = new_expression
