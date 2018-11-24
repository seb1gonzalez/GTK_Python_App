import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import create_box
from GtkUtil import bold_label


class Template(Gtk.Box):

    #field_value_pairs = None;

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)
        self.pack_start(Gtk.Label(" "), False, False, 0)  # REMOVE LATER

        msg_types = Gtk.ListStore(str)
        msg_types.append(["\t\t\t\t     "])
        msg_types.append(["Request"])
        msg_types.append(["Reply"])
        sel_msg_type = Gtk.ComboBox.new_with_model(msg_types)
        renderer_text = Gtk.CellRendererText()
        sel_msg_type.pack_start(renderer_text, True)
        sel_msg_type.add_attribute(renderer_text, "text", 0)
        self.pack_start(create_box([bold_label("\tExisting Message Type  "), sel_msg_type]), False, False, 0)

        cycle_button = Gtk.Button("Cycle Through Packets")
        self.pack_start(create_box([Gtk.Label("\t"), cycle_button], False), False, False, 0) #REMOVE LATER

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        scrolledwindow = Gtk.ScrolledWindow(min_content_height=200,
                                            max_content_height=200,
                                            min_content_width=230,
                                            max_content_width=230)
        text_view = Gtk.TextView(editable=False)
        self.buffer = text_view.get_buffer()
        self.buffer.insert_at_cursor(" ")
        scrolledwindow.add(text_view)
        box = create_box([bold_label("\tMessage Type Template \n"
                                     "\tField Value Pair(s)"),
                          scrolledwindow])
        self.pack_start(box, False, False, 0)

        save = Gtk.Button("Save")
        clear = Gtk.Button("Clear")
        self.pack_end(create_box([save, clear], False), False, False, 0)


    #def setFieldValuePairs(self, fnames, fvalues=[]):
    #    vlen = len(fvalues)
    #    if vlen == 0:
    #        for name in fnames:
    #            self.field_value_pairs.
    #    for name
