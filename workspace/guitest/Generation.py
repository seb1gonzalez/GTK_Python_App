import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import create_box
from GtkUtil import bold_label


class Generation(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, spacing=15, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)
        self.pack_start(Gtk.Label(" "), False, False, 0)  # REMOVE LATER

        msg_types = Gtk.ListStore(str)
        msg_types.append(["\t\t\t\t "])
        msg_types.append(["Request"])
        msg_types.append(["Reply"])
        sel_msg_type = Gtk.ComboBox.new_with_model(msg_types)
        renderer_text = Gtk.CellRendererText()
        sel_msg_type.pack_start(renderer_text, True)
        sel_msg_type.add_attribute(renderer_text, "text", 0)
        self.pack_start(create_box([bold_label("\tExisting Message Type "), sel_msg_type]), False, False, 0)

        sel_output_format = Gtk.ListStore(str)
        sel_output_format.append(["\t\t\t\t "])
        sel_output_format.append(["Scapy"])
        sel_output_format = Gtk.ComboBox.new_with_model(sel_output_format)
        renderer_text = Gtk.CellRendererText()
        sel_output_format.pack_start(renderer_text, True)
        sel_output_format.add_attribute(renderer_text, "text", 0)
        outformat_title = bold_label("\t\tMessage Template \n"
                                     "\t\tOutput Format")

        self.pack_start(create_box([outformat_title, sel_output_format]), False, False, 0)

        sel_msg_template = Gtk.Entry()
        template_title = bold_label("\t\tMessage Template \n\t\tName")
        self.pack_start(create_box([template_title, sel_msg_template]), False, False, 0)

        generate = Gtk.Button("Generate")
        clear = Gtk.Button("Clear")
        self.pack_end(create_box([generate, clear], False), False, False, 0)

