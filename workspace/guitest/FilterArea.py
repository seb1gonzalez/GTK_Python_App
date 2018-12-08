import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from GtkUtil import bold_label
from GtkUtil import create_box
from FilterWindow import run_popwindow


class FilterArea(Gtk.Box):

    def __init__(self, the_packet_area, the_iserver):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # Global variables
        self.iserver = the_iserver
        self.pdmlstate = None
        self.packet_area = the_packet_area
        self.expr_entry = None
        self.filter_cbox = None

        # Creates the title of the Filter Area
        title = Gtk.Label()
        title.set_markup("<b><big><u>Filter Area</u></big></b>")
        title.set_xalign(0.03)
        self.pack_start(title, False, False, 0)

        # Create entry for filter expression input
        self.expr_entry = Gtk.Entry(width_chars=42)

        # Create buttons of the Filter Area
        apply_btn = Gtk.Button(label="Apply")
        apply_btn.connect("clicked", self.on_apply_click)

        clear_btn = Gtk.Button(label="Clear")
        clear_btn.connect("clicked", self.on_clear_click)

        save_btn = Gtk.Button(label="Save")
        save_btn.connect("clicked", self.on_save_click)

        apply_saved_btn = Gtk.Button(label="Apply")
        apply_saved_btn.connect("clicked", self.on_apply_click)

        # Create combo box for saved filters
        saved_filters = Gtk.ListStore(str)
        saved_filters.append(["\t\t\t\t "])
        self.filter_cbox = Gtk.ComboBox.new_with_model(saved_filters)
        renderer_text = Gtk.CellRendererText()
        self.filter_cbox.pack_start(renderer_text, True)
        self.filter_cbox.add_attribute(renderer_text, "text", 0)

        box = create_box([Gtk.Label("   "), self.expr_entry, bold_label("Filter"), apply_btn, clear_btn,
                          save_btn, bold_label("Saved Filter"), self.filter_cbox, apply_saved_btn])
        box.set_spacing(15)
        self.pack_start(box, False, False, 0)

    def on_apply_click(self, button):
        if self.pdmlstate is not None:
            self.iserver.filter_by_expr(self.expr_entry.get_text(), self.pdmlstate)
            self.packet_area.update_packet_view(self.pdmlstate)

    def on_clear_click(self, button):
        self.expr_entry.set_text(" ")
        self.filter_cbox.set_active(0)

    def on_save_click(self, button):
        run_popwindow(self.expr_entry.get_text())

    def on_apply_saved_click(self, button):
        print(button.get_label() + " clicked")

    def update_pdmlstate(self, the_pdmlstate):
        self.pdmlstate = the_pdmlstate

