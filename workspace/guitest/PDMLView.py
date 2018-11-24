import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from FilterArea import FilterAreaWindow
from PacketArea import PacketArea
from FieldArea import FieldArea
from MessageTypeArea import MessageTypeArea
from GtkUtil import create_box
from GtkUtil import create_small_label


class PDMLView(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, spacing=20, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)

        # components of the pdml view are packet area, filter_area and pdml view bottom
        self.filter_area = FilterAreaWindow()
        self.pdml_viewbottom = _PDMLViewBottom()
        self.packet_area = PacketArea(self.pdml_viewbottom.get_fieldarea())

        head = Gtk.HeaderBar()
        head.props.title = "PDML View"
        self.add(head)

        self.pack_start(self.create_pdml_control_view(), False, False, 0)
        self.pack_start(self.filter_area, False, False, 0)
        self.pack_start(self.packet_area, False, False, 0)
        self.pack_start(self.pdml_viewbottom, False, False, 0)

    def create_pdml_control_view(self):
        new_name_entry = Gtk.Entry(width_chars=35)

        save_as_new_button = Gtk.Button()
        save_as_new_button.add(create_small_label("Save as New\nPDML State"))

        save_current_button = Gtk.Button()
        save_current_button.add(create_small_label("Save Current\nPDML State"))

        close_current_button = Gtk.Button()
        close_current_button.add(create_small_label("Close Current\nPDML State"))

        delete_current_button = Gtk.Button()
        delete_current_button.add(create_small_label("Delete Current\nPDML State"))

        rename_entry = Gtk.Entry(width_chars=35)

        rename_button = Gtk.Button()
        rename_button.add(create_small_label("Delete Current\nPDML State"))

        box = create_box([Gtk.Label(" "), new_name_entry, save_as_new_button, save_current_button,  # REMOVE LATER
                          close_current_button, delete_current_button, rename_entry, rename_button, Gtk.Label(" ")])
        box.set_spacing(5)
        return box

    def update_packet_area(self, pdmlstate):
        self.packet_area.update_packet_view(pdmlstate)


class _PDMLViewBottom(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self, column_spacing=5, row_homogeneous=False, column_homogeneous=False)
        # components of pdml view bottom is field area and message type area
        self.field_area = FieldArea()
        self.messagetype_area = MessageTypeArea()

        buttons = Gtk.Box(spacing=15, orientation=Gtk.Orientation.VERTICAL)

        plus_img = Gtk.Image.new_from_file("plus_arrow.png")
        plus_button = Gtk.Button()
        plus_button.connect("clicked", self.on_click_plus_button)
        plus_button.add(plus_img)

        minus_img = Gtk.Image.new_from_file("minus_arrow.png")
        minus_button = Gtk.Button()
        minus_button.add(minus_img)

        buttons.pack_start(plus_button, False, False, 0)
        buttons.pack_start(minus_button, False, False, 0)

        self.attach(self.field_area, 0, 0, 1, 7)
        self.attach(buttons, 1, 4, 1, 1)
        self.attach(self.messagetype_area, 2, 0, 1, 7)

    def get_fieldarea(self):
        return self.field_area

    def on_click_plus_button(self, button):
        fieldpairs = self.field_area.get_fieldpairs()        # returns array of tuples (field name, value)
        self.messagetype_area.insert_pairs(fieldpairs)


