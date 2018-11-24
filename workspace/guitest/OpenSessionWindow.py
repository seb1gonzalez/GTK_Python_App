import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil


class OpenSessionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Open Session")
        self.set_default_size(400, 180)

        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        instructions = GtkUtil.bold_label("\nOpen an Existing Session\n")
        box.pack_start(instructions, False, False, 0)

        pcap_name = Gtk.Entry(width_chars=15)
        browse_pcap = Gtk.Button("Browse")
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tSession Name "),
                                           pcap_name,
                                           browse_pcap]), False, False, 0)

        open_button = Gtk.Button("Open")
        cancel = Gtk.Button("Cancel")
        box.pack_end(GtkUtil.create_box([cancel, open_button], False), False, False, 0)

        self.add(box)


def run_popwindow():
    win = OpenSessionWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
