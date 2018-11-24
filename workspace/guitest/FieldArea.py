import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FieldArea(Gtk.Box):

    TOGGLE = 0
    NAME = 1
    SHOWNAME = 2
    SIZE = 3
    VALUE = 6

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        # components of field area is the field view
        self.fieldview = self._generate_treeview()
        self.current_proto = None

        # put the field view in a scrolled view
        scrolledview = Gtk.ScrolledWindow(min_content_height=430,
                                          max_content_height=430,
                                          min_content_width=600,
                                          max_content_width=600)
        scrolledview.add(self.fieldview)

        # Create title of the field area
        title = Gtk.Label(xalign=0.05)
        title.set_markup("<u><b><big> Field Area </big></b></u>")

        # Create options at the bottom of the field area
        allfields_btn = Gtk.CheckButton("Select all fields")    # check button to select all fields
        allfields_btn.connect("toggled", self.select_allfields)

        field_label = Gtk.Label()
        field_label.set_markup("<small>Field Name, Showname, Value, and Length are editable fields</small>")

        # Create container for the options at the bottom of the field area
        box = Gtk.Box(spacing=15)
        box.pack_start(allfields_btn, False, False, 0)
        box.pack_start(field_label, False, False, 0)

        self.pack_start(title, False, False, 0)
        self.pack_start(scrolledview, False, False, 0)
        self.pack_start(box, False, False, 0)

    def _generate_treeview(self):
        # field data is stored in a tree model
        # create a liststore with 8 columns
        field_store = Gtk.TreeStore(bool, str, str, str, str, str, str, str)
        field_store.append(None, [False, "", "", "", "", "", "", ""])

        # Create a tree view on the created model
        view = Gtk.TreeView(activate_on_single_click=False)
        view.set_model(field_store)

        # Create a toggle column to select fields
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_toggled)  # connect the cellrenderertoggle with a callback function
        column_toggle = Gtk.TreeViewColumn(" ", renderer_toggle, active=0)
        view.append_column(column_toggle)

        # Field attributes to display and whether the attribute is editable
        attribute = ['Field Name', 'Showname', 'Size', 'Position', 'Show', 'Value', 'Entropy']
        editable = [True, True, True, False, False, True, False]
        for i in range(0, len(attribute)):
            # Create column to hold attribute information
            renderer_packet = Gtk.CellRendererText(editable=editable[i])
            if editable[i]:
                renderer_packet.connect("edited", self._update_field)
            column_packet = Gtk.TreeViewColumn(attribute[i], renderer_packet, text=i+1)
            view.append_column(column_packet)

        view.connect("row_activated", self.tag_field)
        return view

    def update(self, pdmlstate, packet_pos, proto_pos):
        proto = pdmlstate.getpacket(packet_pos).getproto(proto_pos)
        field_store = self.fieldview.get_model()
        field_store.clear()

        # Assume columns 1 to 8 are those of field attributes
        fields = proto.getfields()
        self._updatefields(field_store, None, fields)
        self.fieldview.set_model(field_store)
        self.current_proto = proto

    def _updatefields(self, field_store, parent, fields):
        for field in fields:
            new_parent = field_store.append(parent, [False, field.getname(), field.getshowname(), field.getsize(),
                                            field.getposition(), field.getshow(), field.getvalue(), field.getentropy()])
            self._updatefields(field_store, new_parent, field.get_internalfields())

    def on_toggled(self, widget, path):
        field_store = self.fieldview.get_model()

        # Update toggle view; flip current value
        field_store[path][self.TOGGLE] = not field_store[path][self.TOGGLE]

    def _update_field(self, cell_renderer_text, path, new_text):
        field_store = self.fieldview.get_model()
        path = Gtk.TreePath(path)
        old_text = cell_renderer_text.props.text

        # Get internal field if any
        indices = path.get_indices()
        size = len(indices)
        field = self.current_proto.getfield(indices[0])
        for i in range(1, size):
            field = field.get_internalfield(indices[i])

        # Update the specific row
        if old_text == field_store[path][self.NAME]:
            field_store[path][self.NAME] = new_text
            field.set_name(new_text)
        elif old_text == field_store[path][self.SHOWNAME]:
            field_store[path][self.SHOWNAME] = new_text
            field.set_showname(new_text)
        elif old_text == field_store[path][self.SIZE]:
            field_store[path][self.SIZE] = new_text
            field.set_size(new_text)
        elif old_text == field_store[path][self.VALUE]:
            field_store[path][self.VALUE] = new_text
            field.set_value(new_text)

    def select_allfields(self, button):
        field_store = self.fieldview.get_model()
        root_iter = field_store.get_iter_first()
        self._select_allfields_helper(field_store, root_iter, button.get_active())

    def _select_allfields_helper(self, field_store, root_iter, flag):
        while root_iter is not None:
            field_store[root_iter][self.TOGGLE] = flag
            if field_store.iter_has_child(root_iter):
                childiter = field_store.iter_children(root_iter)
                self._select_allfields_helper(field_store, childiter, flag)
            root_iter = field_store.iter_next(root_iter)

    def tag_field(self, view, path, column):
        print("tag")

    def get_fieldpairs(self):
        fieldpair = []
        field_store = self.fieldview.get_model()

        root_iter = field_store.get_iter_first()
        fields = self.current_proto.getfields()
        self._get_fieldpairs_helper(field_store, root_iter, fields, fieldpair)
        return fieldpair

    def _get_fieldpairs_helper(self, field_store, root_iter, fields, fieldpair):
        for field in fields:
            if field_store[root_iter][self.TOGGLE]:
                fieldpair.append((field.getname(), field.getvalue()))
            if field_store.iter_has_child(root_iter):
                childiter = field_store.iter_children(root_iter)
                internalfields = field.get_internalfields()
                self._get_fieldpairs_helper(field_store, childiter, internalfields, fieldpair)
            root_iter = field_store.iter_next(root_iter)

