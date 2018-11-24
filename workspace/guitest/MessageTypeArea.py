import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import bold_label
from Template import Template
from Equivalency import Equivalency
from Generation import Generation
from MessageType import MessageType
from Dependency import Dependency


class MessageTypeArea(Gtk.Box):

    messagetype = MessageType()

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)

        title = Gtk.Label()
        title.set_markup("<u><b><big> Message Type Area </big></b></u>")
        title.set_xalign(0.05)
        self.pack_start(title, True, True, 0)

        notebook = Gtk.Notebook()
        pages = [('New/Modify', self.messagetype),
                 ('Dependency', Dependency()),
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
        self.messagetype.insert_fields(pairs)

    def is_pairs_checked(self):
        return self.messagetype.is_pairs_checked()



