import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Template import Template
from Equivalency import Equivalency
from Generation import Generation
from MessageType import MessageType
from Dependency import Dependency
from backend.InteractionServer import InteractionServer


class MessageTypeArea(Gtk.Box):

    NEW_MODIFY = 0
    DEPENDENCY = 1
    TEMPLATE = 2
    EQUIVALENCY = 3
    GENERATION = 4

    def __init__(self, the_packet_area, iserver):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)

        # components of the MessageTypeArea
        self.msgtype_view = MessageType(iserver, the_packet_area)
        self.dependency_view = Dependency(iserver, the_packet_area)
        self.page_num = 0

        title = Gtk.Label()
        title.set_markup("<u><b><big> Message Type Area </big></b></u>")
        title.set_xalign(0.05)
        self.pack_start(title, True, True, 0)

        notebook = Gtk.Notebook()
        notebook.connect("switch_page", self.update_page)
        pages = [('New/Modify', self.msgtype_view),
                 ('Dependency', self.dependency_view),
                 ('Template', Template()),
                 ('Equivalency', Equivalency()),
                 ('Generation', Generation())]
        self.append_pages(notebook, pages)
        self.pack_start(notebook, True, True, 0)

    def append_pages(self, notebook, pages):
        for page in pages:
            name, content = page
            notebook.append_page(content, Gtk.Label(name))

    def insert_pairs(self, pairs):
        if self.page_num == self.NEW_MODIFY:
            self.msgtype_view.insert_fields(pairs)
        if self.page_num == self.DEPENDENCY:
            self.dependency_view.insert_fields(pairs)

    def remove_pairs(self, pairs):
        if self.page_num == self.NEW_MODIFY:
            self.msgtype_view.remove_fields(pairs)
        if self.page_num == self.DEPENDENCY:
            self.dependency_view.remove_fields(pairs)

    def update_page(self, notebook, page, page_num):
        self.page_num = page_num
        if page_num == self.NEW_MODIFY or page_num == self.DEPENDENCY:
            page.update_msgtype_cbox()





