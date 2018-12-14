from MessageTypeHandler import MessageTypeHandler
from DisplayFilter import DisplayFilter
from TagHandler import TagHandler


class InteractionServer:

    def __init__(self):
        # A Interaction Server knows the following information
        self.msgtype_handler = MessageTypeHandler()
        self.display_filter = DisplayFilter()
        self.tag_handler = TagHandler()

    """
    Message Type Handler Functions
    """

    def getmsgtypes(self):
        print "Message Types = []"
        #return self.msgtype_handler.getmsgtypes()

    def getmsgtype(self, name):
        print "Message Type = ["+str(name)+"]"
        #return self.msgtype_handler.getmsgtype(name)

    def add_msgtype(self, msgtype_name, pairs):
        print 'Added: '+msgtype_name+" :["+pairs+"]"
        #return self.msgtype_handler.add_msgtype(msgtype_name, pairs)

    def delete_msgtype(self, name):
        print "Deleted: "+name
        #return self.msgtype_handler.delete_msgtype(name)

    def update_msgtype(self, old_name, new_name, new_pairs):
        print "Updated: "+old_name+"; To:"+new_name+" with pairs"+new_pairs
        #return self.msgtype_handler.update_msgtype(old_name, new_name, new_pairs)

    def classify_proto(self, msgtype_name, proto):
        print "Classified: "+ msgtype_name+"\nWith proto: "+str(proto)
        # return self.msgtype_handler.classify_proto(msgtype_name, proto)

    """
    Tag Handler Functions
    """
    def get_tags(self):
        print "Tags: [Tag1, Tag2, Tag3]"
        # return self.tag_handler.get_tags()

    def get_tag(self, name):
        print "Tag: [Tag2] "
        # return self.tag_handler.get_tag(name)

    def add_tag(self, tag_name, tag_description, field_name):
        print "Tag added: "+tag_name+ "\nDescription: "+tag_description+"\nField Name: "+ field_name
        # return self.tag_handler.add_tag(tag_name, tag_description, field_name)

    def delete_tag(self, name):
        print "Tag deleted: " + name
        # return self.tag_handler.delete_tag(name)

    def update_tag(self, old_name, new_name, new_field, new_description):
        print "Tag updated from: "+old_name+"; To: "+new_name
        # return self.tag_handler.update_tag(old_name, new_name, new_field, new_description)

    """
    Display Filter Functions
    """
    def getfilters(self):
        print "Filters: [Filter1, Filter2, Filter3]"
        # return self.display_filter.getfilters()

    def add_filter(self, name, expression):
        print "Added Filter: "+name+ "\nValue: "+ expression
        # return self.display_filter.add_filter(name, expression)

    def save_filter(self):
        print "Saved Filter"
        # return self.display_filter.save_filter()

    def delete_filter(self, name):
        print "Deleted filter: "+ name
        # return self.display_filter.delete_filter(name)

    def update_filter(self, name, new_name, new_expression):
        print "Updated filter: "+name+"\n To: "+new_name
        # return self.display_filter.update_filter(name, new_name, new_expression)

    def filter_by_name(self, name, pdmlstate):
        print "Filtered by name: [Filter_Stub]"
        # return self.display_filter.filter_by_name(name, pdmlstate)

    def filter_by_expr(self, expression, pdmlstate):
        print "Filtered by Expression: [Expression_stub]"
        # return self.display_filter.filter_by_expr(expression, pdmlstate)

