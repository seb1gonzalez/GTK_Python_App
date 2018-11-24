import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import create_box
from GtkUtil import bold_label


class SessionView(Gtk.Box):

    #field_value_pairs = None;

    def __init__(self):
        Gtk.Box.__init__(self, spacing=10, orientation=Gtk.Orientation.VERTICAL)
        self.set_homogeneous(False)
        self.set_border_width(5)

        head = Gtk.HeaderBar()
        head.props.title = "Session View"
        self.add(head)

        workspace_name = Gtk.Label("Workspace X")
        workspace_name.set_xalign(0.04)
        self.pack_start(workspace_name, False, False, 0)

        grid = Gtk.Grid()
        grid.attach(Gtk.Label("\t\t"), 0, 0, 1, 1)          #REMOVE LATER

        opened_folder = Gtk.Image.new_from_file("opened_folder.png")
        grid.attach(opened_folder, 1, 0, 1, 1,)

        session_a = Gtk.Label("Session A  ")
        grid.attach(session_a, 2, 0, 1, 1)

        state_1 = Gtk.Label("-State 1")
        grid.attach(state_1, 2, 1, 1, 1)

        state_2 = Gtk.Label()
        state_2.set_markup("<a href=\"file:/home/jesus/PycharmProjects/guitest/state_test.txt\">-State 2</a>")
        grid.attach(state_2, 2, 2, 1, 1)

        closed_folder = Gtk.Image.new_from_file("closed_folder.png")
        grid.attach(closed_folder, 1, 3, 1, 1)

        session_b = Gtk.Label()
        session_b.set_markup("<a href=\"file:/home/jesus/PycharmProjects/guitest/session_test.txt\">\nSession B</a>")
        grid.attach(session_b, 2, 3, 1, 1)

        closed_folder = Gtk.Image.new_from_file("closed_folder.png")
        grid.attach(closed_folder, 1, 4, 1, 1)

        session_c = Gtk.Label()
        session_c.set_markup("<a href=\"file:/home/jesus/PycharmProjects/guitest/session_test.txt\">\nSession C</a>")
        grid.attach(session_c, 2, 4, 1, 1)

        self.pack_start(grid, False, False, 0)



