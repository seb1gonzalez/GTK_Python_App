import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil


class SessionWindow(Gtk.Window):

    session_name = None
    description = None

    def __init__(self):
        Gtk.Window.__init__(self, title="New Session")
        self.set_default_size(400, 320)

        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        instructions = GtkUtil.bold_label("\nCreate a new session\n")
        box.pack_start(instructions, False, False, 0)

        session_name = Gtk.Entry(width_chars=23)
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tSession Name "),
                                           session_name]), False, False, 0)

        scrolledwindow = Gtk.ScrolledWindow(min_content_height=150,
                                            max_content_height=150,
                                            min_content_width=220,
                                            max_content_width=220)
        text_view = Gtk.TextView()
        self.description = text_view.get_buffer()
        self.description.insert_at_cursor("Project Description")
        scrolledwindow.add(text_view)
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\t    Description "),
                                           scrolledwindow]), False, False, 0)

        create = Gtk.Button("Create")
        cancel = Gtk.Button("Cancel")
        box.pack_end(GtkUtil.create_box([cancel, create], False), False, False, 0)

        self.add(box)

    # This will be called to make the session objects.
    def get_values(self):
        return self.session_name.get_text(), self.description.get_text()


def run_popwindow():
    win = SessionWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()





