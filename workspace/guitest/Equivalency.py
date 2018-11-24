import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil as gu


class Equivalency(Gtk.Box):

    curr_row = 0
    grid = Gtk.Grid()

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)
        self.pack_start(Gtk.Label(" "), False, False, 0)  # REMOVE LATER

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.add(self.grid)
        self.pack_start(scrolledwindow, True, True, 0)

        title = gu.bold_label("\tField Equivalency ")
        plus_button = Gtk.Button("+")
        plus_button.connect("clicked", self.on_click_plus_button)
        self.grid.attach(title, 0, 0, 1, 1)
        self.grid.attach(plus_button, 4, 1, 1, 1)

        self.add_equivalency()

        save = Gtk.Button("Save")
        clear = Gtk.Button("Clear")
        self.pack_start(gu.create_box([save, clear], False), False, False, 0)

    def on_click_plus_button(self, button):
        self.add_equivalency()

    def add_equivalency(self):
        fname1 = Gtk.Entry(editable=False, width_chars=10)
        self.grid.attach(fname1, 1, self.curr_row, 1, 1)
        self.grid.attach(gu.create_small_label("Of"), 2, self.curr_row, 1, 1)
        msgtype1 = Gtk.Entry(editable=False, width_chars=10)
        self.grid.attach(msgtype1, 3, self.curr_row, 1, 1)
        self.grid.attach(Gtk.Label("="), 4, self.curr_row, 1, 1)

        self.curr_row = self.curr_row + 1

        fname1 = Gtk.Entry(editable=False, width_chars=10)
        self.grid.attach(fname1, 1, self.curr_row, 1, 1)
        self.grid.attach(gu.create_small_label("Of"), 2, self.curr_row, 1, 1)
        msgtype1 = Gtk.Entry(editable=False, width_chars=10)
        self.grid.attach(msgtype1, 3, self.curr_row, 1, 1)







