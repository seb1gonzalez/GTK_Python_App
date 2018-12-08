import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil as gu


class Dependency(Gtk.Box):

    fsize_buffer = None
    csum2_buffer = None

    def __init__(self, the_iserver, the_packet_area):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)

        # Global variables of this class
        self.msgtype_cbox = None
        self.packet_area = the_packet_area
        self.iserver = the_iserver
        self.head_packet = None     # variable used to cycle through packets
        self.curr_packet = None
        self.dependency_view = None

        # Create combo box for the existing message types
        msgtype_store = Gtk.ListStore(str)
        msgtype_store.append(["\t\t\t\t\t\t"])
        self.msgtype_cbox = Gtk.ComboBox.new_with_model(msgtype_store)
        renderer_text = Gtk.CellRendererText(width_chars=19)
        self.msgtype_cbox.pack_start(renderer_text, True)
        self.msgtype_cbox.add_attribute(renderer_text, "text", 0)
        self.msgtype_cbox.set_active(0)
        self.msgtype_cbox.connect("changed", self._reset_cycle_packets)

        # Create button to cycle through packets
        cycle_packets = Gtk.Button("Cycle Through Packets")
        cycle_packets.connect("clicked", self._cycle_packets)

        # Create input fields for the size of a field dependency
        self.dependency_view = self.create_dependency_view()
        scrolled_window = Gtk.ScrolledWindow(min_content_height=120,
                                             max_content_height=300,
                                             min_content_width=200,
                                             max_content_width=200)
        scrolled_window.add(self.dependency_view)

        save = Gtk.Button("Save")
        clear = Gtk.Button("Clear")

        # Append components to class Gtk.Box
        self.pack_start(Gtk.Label(" "), False, False, 0)  # REMOVE LATER
        self.pack_start(gu.create_box([gu.bold_label("\t\tExisting Message Type "), self.msgtype_cbox]),
                        False, False, 0)
        self.pack_start(gu.create_box([Gtk.Label("\t"), cycle_packets], False), False, False, 0)  # REMOVE LATER
        self.pack_start(scrolled_window, False, False, 0)
        self.pack_end(gu.create_box([save, clear], False), False, False, 0)

    def create_dependency_view(self):
        # field data is stored in a tree model
        # create a liststore with 8 columns
        field_store = Gtk.TreeStore(str, str, str, str)
        field_store.append(None, ["Size of Field", "", "depends on", ""])
        field_store.append(None, ["Size of Packet", "", "depends on", ""])
        field_store.append(None, ["Checksum", "", "depends on", ""])

        # Create a tree view on the created model
        view = Gtk.TreeView()
        sel = view.get_selection()
        sel.set_mode(Gtk.SelectionMode.NONE)
        view.set_model(field_store)

        # Create column for titles example "Size of Field", "Size of Packet"
        renderer_packet = Gtk.CellRendererText(font="Bold")
        column_packet = Gtk.TreeViewColumn(" ", renderer_packet, text=0)
        view.append_column(column_packet)

        # Create column for depender
        renderer_packet = Gtk.CellRendererText()
        column_packet = Gtk.TreeViewColumn(" ", renderer_packet, text=1)
        view.append_column(column_packet)

        # Create column for text "depends on"
        renderer_packet = Gtk.CellRendererText(font="10")
        column_packet = Gtk.TreeViewColumn(" ", renderer_packet, text=2)
        view.append_column(column_packet)

        # Create column for provider
        renderer_packet = Gtk.CellRendererText()
        column_packet = Gtk.TreeViewColumn(" ", renderer_packet, text=3)
        view.append_column(column_packet)

        view.connect("row_activated", self.display_selected_cell)
        return view

    #def insert_fields(self, pairs, view, path, column):

    def update_msgtype_cbox(self):
        self._clear(None)
        msgtype_store = self.msgtype_cbox.get_model()
        msgtype_store.clear()
        msgtype_store.append(["\t\t\t\t\t\t"])
        self.msgtype_cbox.set_active(0)

        msgtype = self.iserver.getmsgtypes()
        for mt in msgtype:
            msgtype_store.append([mt.get_name()])

    def display_selected_cell(self, view, path, column):
        print self.dependency_view.get_column(0)
        self.dependency_view.set_cursor(path, None, True)
        return True

    def _clear(self, button):
        return True

    def _cycle_packets(self, button):
        active_index = self.msgtype_cbox.get_active()

        if active_index > 0:
            msgtype_store = self.msgtype_cbox.get_model()
            msgtype_name = msgtype_store[active_index][0]

            if self.head_packet is None:            # find_next returns the path of a protocol
                self.head_packet = self.packet_area.find_next(msgtype_name, None)
                self.curr_packet = self.head_packet
            else:
                packet_index = self.curr_packet.get_indices()[0]        # find next after the current packet
                self.curr_packet = self.packet_area.find_next(msgtype_name, Gtk.TreePath(packet_index))
                if self.curr_packet is None:
                    self.curr_packet = self.head_packet

            if self.curr_packet is not None:
                self.packet_area.set_cursor(self.curr_packet)

    def _reset_cycle_packets(self, button):
        self.head_packet = None
        self.curr_packet = None

