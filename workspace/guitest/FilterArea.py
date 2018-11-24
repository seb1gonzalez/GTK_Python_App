import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from GtkUtil import bold_label
from GtkUtil import create_box
from FilterWindow import run_popwindow


class FilterAreaWindow(Gtk.Box):

    filter_expression_entry = None

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)

        title = Gtk.Label()
        title.set_markup("<b><big><u>Filter Area</u></big></b>")
        title.set_xalign(0.03)
        self.pack_start(title, False, False, 0)

        self.filter_expression_entry = Gtk.Entry(width_chars=42)
        #filter_expression = filter_expression_box.get_buffer()

        filter_label = bold_label("Filter")

        apply_button = Gtk.Button(label="Apply")
        apply_button.connect("clicked", self.button_clicked)

        clear_button = Gtk.Button(label="Clear")
        clear_button.connect("clicked", self.button_clicked)

        save_button = Gtk.Button(label="Save")
        save_button.connect("clicked", self.save_button_clicked)

        saved_filter = Gtk.Label()
        saved_filter.set_markup("<b>Saved Filter</b>")

        saved_filters = Gtk.ListStore(str)
        saved_filters.append(["\t\t\t\t "])
        saved_filters.append(["ipx"])
        saved_filters.append(["tcp"])
        saved_filters.append(["udp"])
        saved_filters.append(["!(udp.port==53 || tcp.port==53)"])
        saved_filters.append(["Eth.addr == ff:ff:ff:ff"])
        filter_combo_box = Gtk.ComboBox.new_with_model(saved_filters)
        renderer_text = Gtk.CellRendererText()
        filter_combo_box.pack_start(renderer_text, True)
        filter_combo_box.add_attribute(renderer_text, "text", 0)
        #filters = SavedFilters()

        apply_saved_button = Gtk.Button(label="Apply")
        apply_saved_button.connect("clicked", self.button_clicked)

        box = create_box([Gtk.Label("   "), self.filter_expression_entry, filter_label, apply_button,  # REMOVE LATER
                          clear_button, save_button, saved_filter, filter_combo_box, apply_saved_button])
        box.set_spacing(15)
        self.pack_start(box, False, False, 0)


    def button_clicked(self, widget):
        print(widget.get_label() + " clicked")

    def save_button_clicked(self, button):
        run_popwindow(self.filter_expression_entry.get_text())



class SavedFilters(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_border_width(10)

        saved_filter = Gtk.ListStore(int, str)
        saved_filter.append([1, "ipx"])
        saved_filter.append([2, "tcp"])
        saved_filter.append([3, "udp"])
        saved_filter.append([4, "!(udp.port==53 || tcp.port==53)"])
        saved_filter.append([5, "Eth.addr == ff:ff:ff:ff"])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        name_combo = Gtk.ComboBox.new_with_model_and_entry(saved_filter)
        name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)
        vbox.pack_start(name_combo, False, False, 0)

        self.add(vbox)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

