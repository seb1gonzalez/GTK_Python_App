import gi
import GtkUtil
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from backend import PCAPHandler


class PCAPWindow(Gtk.Window):

    pdmlfile = None
    pcap_path = Gtk.Entry(width_chars=15)
    dissector_path = Gtk.Entry(width_chars=15, editable=False)

    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")
        self.set_default_size(400, 220)

        container = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        container.pack_start(GtkUtil.bold_label("\nOpen a PCAP File\n"), False, False, 0)

        # Create button and text field to ask the user to browse the pcap file
        pcap_button = Gtk.Button("Browse")
        pcap_button.connect("clicked", self.ask_for_pcap, self)
        container.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\t\tPCAP Name"),
                                                 self.pcap_path, pcap_button]),
                             False, False, 0)

        # Create button and text field to ask the user to browse the dissector file
        dstr_button = Gtk.Button("Browse")
        container.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tDissector Name"),
                                                 self.dissector_path, dstr_button]),
                             False, False, 0)

        convert = Gtk.Button("Convert to PDML")
        convert.connect("clicked", self.convert_pcap)
        cancel = Gtk.Button("Cancel")
        cancel.connect("clicked", self.close)
        container.pack_end(GtkUtil.create_box([cancel, convert], False), False, False, 0)

        self.add(container)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def ask_for_pcap(self, button, parent):
        dialog = Gtk.FileChooserDialog(title="Open PCAP",
                                       parent=parent,
                                       buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                                Gtk.STOCK_OK, Gtk.ResponseType.OK))
        dialog.show()
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            text = dialog.get_filename()
            self.pcap_path.set_text(text)
        dialog.destroy()

    def convert_pcap(self, button):
        pcap_path = self.pcap_path.get_text()
        if pcap_path == "":
            GtkUtil.show_error_dialog(self, "Please enter a pcap file!")
        else:
            handler = PCAPHandler.PCAPHandler()         # convert PCAP to PDML
            self.pdmlfile = handler.convert(pcap_path)
            self.destroy()

    def close(self, button):
        self.destroy()

    def get_pdmlfile(self):
        created_pdml = self.pdmlfile
        self.pdmlfile = None
        return created_pdml
