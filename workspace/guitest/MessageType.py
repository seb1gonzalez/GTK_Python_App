import GtkUtil as gu
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MessageType(Gtk.Box):

    def __init__(self, the_iserver, the_packet_area):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)

        # Global variables
        self.fieldpairs = []
        self.iserver = the_iserver
        self.packet_area = the_packet_area
        self.ispairs_selected = True
        self.pairs_txtview = None
        self.msgtype_entry = None
        self.msgtype_cbox = None

        # Display instructions on the message type notebook
        instructions = Gtk.Label()
        instructions.set_markup("To create a new message type, please enter a \n"
                                "message type name and select message type field \n"
                                "value pair(s). To update/delete an existing \n"
                                "message type, please select from the existing \n"
                                "message type first and the previously selected \n"
                                "name and field value pair(s) will be pre-populated.\n")
        self.pack_start(instructions, False, False, 0)

        # Create combo box for the existing message types
        msgtype_store = Gtk.ListStore(str)
        msgtype_store.append(["\t\t\t\t\t\t"])
        self.msgtype_cbox = Gtk.ComboBox.new_with_model(msgtype_store)
        renderer_text = Gtk.CellRendererText(width_chars=19)
        self.msgtype_cbox.pack_start(renderer_text, True)
        self.msgtype_cbox.add_attribute(renderer_text, "text", 0)
        self.msgtype_cbox.set_active(0)
        self.msgtype_cbox.connect("changed", self._display_msgtype)

        # Create entry for input of the message type name
        self.msgtype_entry = Gtk.Entry(width_chars=23)

        # Create scrolledwindow for the field pairs
        self.pairs_txtview = Gtk.TextView(buffer=Gtk.TextBuffer(), editable=False)
        fv_scrolledwindow = Gtk.ScrolledWindow(min_content_height=100,
                                               max_content_height=100,
                                               min_content_width=220,
                                               max_content_width=220)
        fv_scrolledwindow.add(self.pairs_txtview)

        # Create radiobuttons for the selection of only field names or both field name and value
        rbtn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)  
        rbtn1 = Gtk.RadioButton.new_with_label_from_widget(None, "Select both field name and value")
        rbtn1.connect("toggled", self.rbtn_ontoggled)
        rbtn2 = Gtk.RadioButton.new_with_label_from_widget(rbtn1, "Select field name only")
        rbtn2.connect("toggled", self.rbtn_ontoggled)
        rbtn_box.pack_start(rbtn2, False, False, 0)
        rbtn_box.pack_start(rbtn1, False, False, 0)

        # Create buttons for different options
        save = Gtk.Button("Save")
        save.connect("clicked", self._save)
        delete = Gtk.Button("Delete")
        delete.connect("clicked", self._delete)
        clear = Gtk.Button("Clear")
        clear.connect("clicked", self._clear)

        # Append components to the message type view
        self.pack_start(gu.create_box([gu.bold_label("\t   Existing Message Type "), self.msgtype_cbox]), False, False, 0)
        self.pack_start(gu.create_box([gu.bold_label("\t\tMessage Type Name "), self.msgtype_entry]), False, False, 0)
        self.pack_start(gu.create_box([gu.bold_label("\t\t  Message Type Field \n\t\t  Value Pair(s)"), fv_scrolledwindow]),
                        False, False, 0)
        self.pack_start(rbtn_box, False, False, 5)
        self.pack_end(gu.create_box([save, delete, clear], False), False, False, 0)

    def insert_fields(self, pairs):
        if pairs is not None:
            txtbuffer = Gtk.TextBuffer()
            if self.ispairs_selected:
                for pair in pairs:
                    name, value = pair
                    end_iter = txtbuffer.get_end_iter()
                    txtbuffer.insert(end_iter, name + " , " + value + "\n")
            else:
                for pair in pairs:
                    name, value = pair
                    end_iter = txtbuffer.get_end_iter()
                    txtbuffer.insert(end_iter, name + "\n")
            self.pairs_txtview.set_buffer(txtbuffer)
            self.fieldpairs = pairs

    def remove_fields(self, remove_pairs):
        # Given pairs are those who stay
        if remove_pairs is not None:
            new_fieldpairs = []
            for fp in self.fieldpairs:
                is_removed = False
                for rv in remove_pairs:
                    if rv[0] == fp[0] and rv[1] == fp[1]:
                        is_removed = True
                        break
                if is_removed is False:
                    new_fieldpairs.append(fp)
            self.insert_fields(new_fieldpairs)

    def rbtn_ontoggled(self, button):
        if button.get_active() and button.get_label() == "Select both field name and value":
            self.ispairs_selected = True
        else:
            self.ispairs_selected = False

    def update_msgtype_cbox(self):
        self._clear(None)
        msgtype_store = self.msgtype_cbox.get_model()
        msgtype_store.clear()
        msgtype_store.append(["\t\t\t\t\t\t"])
        self.msgtype_cbox.set_active(0)

        msgtype = self.iserver.getmsgtypes()
        for mt in msgtype:
            msgtype_store.append([mt.get_name()])
            self.packet_area.color_protos(self.iserver, mt.get_name())

    def _clear(self, button):
        self.msgtype_entry.set_text("")
        self.pairs_txtview.set_buffer(Gtk.TextBuffer())
        self.msgtype_cbox.set_active(0)
        self.fieldpairs = []

    def _delete(self, button):
        msgtype_store = self.msgtype_cbox.get_model()
        active_index = self.msgtype_cbox.get_active()

        if active_index > 0:
            msgtype_name = msgtype_store[active_index][0]
            was_deleted = self.iserver.delete_msgtype(msgtype_name)
            if was_deleted:
                msgtype_store.remove(self.msgtype_cbox.get_active_iter())
                self._clear(button)
        # ADD ERROR MESSAGE WHEN NOT SELECTED A MESSAGE TYPE

    def _display_msgtype(self, cbox):
        msgtype_store = self.msgtype_cbox.get_model()
        active_index = self.msgtype_cbox.get_active()

        if active_index > 0:
            msgtype_name = msgtype_store[active_index][0]
            msgtype = self.iserver.getmsgtype(msgtype_name)

            self.msgtype_entry.set_text(msgtype.get_name())
            fieldpairs = msgtype.get_fieldpairs()
            pairs = []
            for fv in fieldpairs:
                pairs.append((fv.getname(), fv.getvalue()))
            self.insert_fields(pairs)

    def _save(self, button):
        # Get the name of the new message type
        msgtype_name = str.strip(self.msgtype_entry.get_text())

        # there must be at least one pair of field name and value
        # if self.fieldpairs is [] or msgtype_name is "":
        #     gu.show_error_dialog("Please enter missing entries!")
        # else:
        msgtype_store = self.msgtype_cbox.get_model()
        active_index = self.msgtype_cbox.get_active()
        if active_index == 0:       # if 0 then we are creating a new message type
            was_added = self.iserver.add_msgtype(msgtype_name, self.fieldpairs)
            if was_added:
                msgtype_store.append([msgtype_name])    # Add to the combo box; # ADD A DIALOG HERE
                self.packet_area.color_protos(self.iserver, msgtype_name)
        else:
            old_msgtype_name = msgtype_store[active_index][0]
            was_added = self.iserver.update_msgtype(old_msgtype_name, msgtype_name, self.fieldpairs)
            if was_added:
                msgtype_store[active_index][0] = msgtype_name





