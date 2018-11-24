import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import bold_label
from GtkUtil import create_box


class MessageType(Gtk.Box):

    pairs_buffer = None
    is_pairs_set = True

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)

        instructions = Gtk.Label()
        instructions.set_markup("To create a new message type, please enter a \n"
                                "message type name and select message type field \n"
                                "value pair(s). To update/delete an existing \n"
                                "message type, please select from the existing \n"
                                "message type first and the previously selected \n"
                                "name and field value pair(s) will be pre-populated.\n")
        self.pack_start(instructions, False, False, 0)

        msgtype_store = Gtk.ListStore(str)
        msgtype_store.append(["\t\t\t\t "])
        msgtype_store.append(["Request"])
        msgtype_store.append(["Reply"])
        sel_msg_type = Gtk.ComboBox.new_with_model(msgtype_store)
        renderer_text = Gtk.CellRendererText()
        sel_msg_type.pack_start(renderer_text, True)
        sel_msg_type.add_attribute(renderer_text, "text", 0)
        self.pack_start(create_box([bold_label("\t   Existing Message Type "), sel_msg_type]), False, False, 0)

        set_msg_type_name = Gtk.Entry()
        self.pack_start(create_box([bold_label("\t\tMessage Type Name "), set_msg_type_name]), False, False, 0)

        fv_scrolledwindow = Gtk.ScrolledWindow(min_content_height=100,
                                               max_content_height=100,
                                               min_content_width=160,
                                               max_content_width=160)
        text_view = Gtk.TextView(editable=False)
        self.pairs_buffer = text_view.get_buffer()
        self.pairs_buffer.insert_at_cursor(" ")
        fv_scrolledwindow.add(text_view)
        self.pack_start(create_box([bold_label("\t\t  Message Type Field \n\t\t  Value Pair(s)"),
                                    fv_scrolledwindow]), False, False, 0)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        fname_and_fvalue = Gtk.RadioButton.new_with_label_from_widget(None, "Select both field name and value")
        fname_and_fvalue.connect("toggled", self.on_radiobutton_toggled, "Both")
        fname = Gtk.RadioButton.new_with_label_from_widget(fname_and_fvalue, "Select field name only")
        fname.connect("toggled", self.on_radiobutton_toggled, "Only one")
        box.pack_start(fname, False, False, 0)
        box.pack_start(fname_and_fvalue, False, False, 0)
        self.pack_start(box, False, False, 5)

        save = Gtk.Button("Save")
        delete = Gtk.Button("Delete")
        clear = Gtk.Button("Clear")
        self.pack_end(create_box([save, delete, clear], False), False, False, 0)

    def insert_fields(self, pairs):
        self.pairs_buffer.set_text("")
        for pair in pairs:
            name, value = pair
            self.pairs_buffer.insert_at_cursor(name + ", " + value + "\n")

    def on_radiobutton_toggled(self, button, name):
        if name == "Both":
            self.is_pairs_set = True
        else:
            self.is_pairs_set = False;


class ExistingMessageType(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, spacing=10)
        sel_msg_type = Gtk.ComboBox.new_with_model_and_entry(Gtk.ListStore(str))

        label = Gtk.Label()
        label.set_markup("<b>Existing Message Type</b>")

        self.pack_start(label, False, False, 0)
        self.pack_start(sel_msg_type, False, False, 0)


def create_small_label(string):
    label = Gtk.Label()
    label.set_markup("<small>" + string + "</small>")
    return label
