from DatabaseHandler import DatabaseHandler


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

    def filter_out(self, name, pdmlfile):
        return True


class _Filter:

    def __init__(self, the_name, the_expression):
        # a Filter knows the following information
        self.name = the_name
        self.expression = the_expression

    def update(self, new_name, new_expression):
        self.name = new_name
        self.expression = new_expression

