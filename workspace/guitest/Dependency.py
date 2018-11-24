import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil as gu


class Dependency(Gtk.Box):

    fsize_buffer = None
    csum2_buffer = None

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.pack_start(Gtk.Label(" "), False, False, 0)   #REMOVE LATER

        msg_types = Gtk.ListStore(str)
        msg_types.append(["\t\t\t\t "])
        msg_types.append(["Request"])
        msg_types.append(["Reply"])
        sel_msg_type = Gtk.ComboBox.new_with_model(msg_types)
        renderer_text = Gtk.CellRendererText()
        sel_msg_type.pack_start(renderer_text, True)
        sel_msg_type.add_attribute(renderer_text, "text", 0)
        self.pack_start(gu.create_box([gu.bold_label("\tExisting Message Type "), sel_msg_type]), False, False, 0)

        cycle_packets = Gtk.Button("Cycle Through Packets")
        self.pack_start(gu.create_box([Gtk.Label("\t"), cycle_packets], False), False, False, 0) #REMOVE LATER

        f1_name = Gtk.Entry(editable=False, width_chars=10)
        scrolledwindow = Gtk.ScrolledWindow(min_content_height=100,
                                            max_content_height=100,
                                            min_content_width=160,
                                            max_content_width=160)
        text_view = Gtk.TextView(editable=False)
        self.fsize_buffer = text_view.get_buffer()
        self.fsize_buffer.insert_at_cursor(" ")
        scrolledwindow.add(text_view)
        grid = Gtk.Grid(row_homogeneous=False, column_homogeneous=False)
        grid.attach(gu.bold_label("\tSize of Field "), 0, 0, 1, 1)
        grid.attach(f1_name, 1, 0, 1, 1)
        grid.attach(gu.create_small_label(" Depends \n on"), 2, 0, 1, 1)
        grid.attach(scrolledwindow, 3, 0, 1, 8)
        self.pack_start(grid, False, False, 0)

        p1_name = Gtk.Entry(editable=False, width_chars=10)
        f2_name = Gtk.Entry(editable=False, width_chars=10)
        packet_dependency = [gu.bold_label("    Size of Packet"),
                             p1_name,
                             gu.create_small_label(" Depends\n on"),
                             f2_name]
        box = gu.create_box(packet_dependency)
        box.set_spacing(5)
        self.pack_start(box, False, False, 0)

        csum1_name = Gtk.Entry(editable=False, width_chars=10)
        scrolledwindow = Gtk.ScrolledWindow(min_content_height=100,
                                            max_content_height=100,
                                            min_content_width=160,
                                            max_content_width=160)
        text_view = Gtk.TextView(editable=False)
        self.csum2_buffer = text_view.get_buffer()
        self.csum2_buffer.insert_at_cursor(" ")
        scrolledwindow.add(text_view)
        grid = Gtk.Grid(row_homogeneous=False, column_homogeneous=False)
        grid.attach(gu.bold_label("\t    Checksum "), 0, 0, 1, 1)
        grid.attach(csum1_name, 1, 0, 1, 1)
        grid.attach(gu.create_small_label(" Depends \n on"), 2, 0, 1, 1)
        grid.attach(scrolledwindow, 3, 0, 1, 8)
        self.pack_start(grid, False, False, 0)

        save = Gtk.Button("Save")
        clear = Gtk.Button("Clear")
        self.pack_end(gu.create_box([save, clear], False), False, False, 0)
