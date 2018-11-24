import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from GtkUtil import bold_label
from GtkUtil import create_box


class PacketArea(Gtk.Box):

    # Position of column in the packet area
    TOGGLE = 0
    PACKET = 1
    SIZE = 2

    packet_tree = None
    pdmlstate = None

    def __init__(self, the_fieldarea):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self._fieldarea = the_fieldarea

        # title packet area
        title = bold_label("<big><u>Packet Area</u></big>")
        title.set_xalign(0.03)
        self.pack_start(title, False, False, 0)

        # Create packet area
        self.packet_view = self.generate_treeview()
        scrolled_packet = Gtk.ScrolledWindow(min_content_height=400,
                                             max_content_height=400,
                                             min_content_width=1050,
                                             max_content_width=1050)
        scrolled_packet.add(self.packet_view)

        # Create buttons to modify packet area
        btn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        remove = Gtk.Button("Remove")
        remove.connect("clicked", self.remove)
        clear = Gtk.Button("Clear")
        clear.connect("clicked", self.clear)
        btn_box.pack_end(remove, False, False, 0)
        btn_box.pack_end(clear, False, False, 0)

        # Create main container
        box = create_box([scrolled_packet, btn_box])
        box.set_spacing(15)
        self.pack_start(box, False, False, 0)

    def generate_treeview(self):
        # packet data is stored in a tree model
        # create a treestore with three columns
        packet_store = Gtk.TreeStore(bool, str, str)
        packet_store.append(None, [False, "", "0"])

        # Create a tree view on the created model
        view = Gtk.TreeView(activate_on_single_click=False)
        view.set_model(packet_store)

        # Create toggle column to select either packets or protocols
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_toggled)  # connect the cellrenderertoggle with a callback function
        column_toggle = Gtk.TreeViewColumn(" ", renderer_toggle, active=0)
        view.append_column(column_toggle)

        # Create second column to hold packet and protocol info
        renderer_packet = Gtk.CellRendererText()
        column_packet = Gtk.TreeViewColumn(" ", renderer_packet, text=1)
        view.append_column(column_packet)

        # Create third column to hold packet and protocol size
        renderer_size = Gtk.CellRendererText()
        column_size = Gtk.TreeViewColumn("Size", renderer_size, text=2)
        view.append_column(column_size)

        view.connect("row-activated", self.update_fieldvalues)

        return view

    def update_fieldvalues(self, view, path, column):
        # this 1 comes from the way each column was appended in 'generate_treeview'
        indices = path.get_indices()
        if view.get_column(1) == column and len(indices) == 2:
            # it is expected a path equal to '[n1, n2]' example '[0, 3]'
            self._fieldarea.update(self.pdmlstate, indices[0], indices[1]+1)

    def update_packet_view(self, pdmlstate):
        packet_store = self.packet_view.get_model()
        packet_store.clear()
        if pdmlstate is not None:
            packets = pdmlstate.getpackets()
            for packet in packets:
                parent = packet_store.append(None, [False, " ", "0"])

                proto = packet.getprotos()
                proto_len = len(proto)
                proto_names = ""
                for i in range(1, proto_len):
                    packet_store.append(parent, [False, proto[i].getshowname(), proto[i].getsize()])
                    proto_names = proto_names + proto[i].getname() + ", "

                # set protocol names on packet header
                packet_store[-1][self.PACKET] = "Frame: " + proto_names
                packet_store[-1][self.SIZE] = packet.getsize()

        self.packet_view.set_model(packet_store)
        self.pdmlstate = pdmlstate          # keep track of current pdmlstate in the system

    def on_toggled(self, widget, path):
        path_len = len(path)

        packet_store = self.packet_view.get_model()
        current_value = not packet_store[path][self.TOGGLE]   # toggle clicked checkbutton
        packet_store[path][self.TOGGLE] = current_value

        # if length of the path is 1 (that is, if we are selecting a packet)
        if path_len == 1:
            # get the iter associated with the path
            packet = packet_store.get_iter(path)

            # get the iter associated with its first child
            proto = packet_store.iter_children(packet)

            # while there are children, change the state of their bool value to the parent
            while proto is not None:
                packet_store[proto][self.TOGGLE] = current_value
                proto = packet_store.iter_next(proto)

    def remove(self, button):
        if self.pdmlstate is None:
            return

        packet_store = self.packet_view.get_model()

        pi = 0  # packet position to remove
        piter = packet_store.get_iter(Gtk.TreePath(0))  # packet iterator to loop through packets (view)
        while piter is not None:
            prev = piter
            piter = packet_store.iter_next(piter)
            if packet_store[prev][self.TOGGLE]:     # is packet selected
                self.pdmlstate.remove_packet(pi)    # remove packet from actual pdml
                packet_store.remove(prev)           # remove packet from packet view
            else:
                ci = 0      # proto position to remove
                citer = packet_store.iter_children(prev)
                while citer is not None:
                    prev = citer
                    citer = packet_store.iter_next(citer)
                    if packet_store[prev][self.TOGGLE]:
                        self.pdmlstate.getpacket(pi).remove_proto(ci)   # remove proto from actual pdml
                        packet_store.remove(prev)                       # remove proto from packet view
                    else:
                        ci = ci+1
                pi = pi+1     # current packet was not removed, advance packet position

    def clear(self, button):
        if self.pdmlstate is None:
            return

        packet_store = self.packet_view.get_model()
        piter = packet_store.get_iter(Gtk.TreePath(0))  # parent iterator to loop through packets
        while piter is not None:
            # Clear toggle for packet
            packet_store[piter][self.TOGGLE] = False

            citer = packet_store.iter_children(piter)   # child iterator to loop through packets
            while citer is not None:
                # Clear toggle for protocols
                packet_store[citer][self.TOGGLE] = False
                citer = packet_store.iter_next(citer)

            piter = packet_store.iter_next(piter)











