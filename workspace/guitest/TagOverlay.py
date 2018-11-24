import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil


class SessionWindow(Gtk.Window):

    tag_name = None
    tag_field = None
    description = None

    def __init__(self, tagname, tagfield, the_description):
        Gtk.Window.__init__(self, title="Tag Overlay")
        self.set_default_size(400, 320)

        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(Gtk.Label("\n"), False, False, 0)                # REMOVE LATER

        self.tag_name = Gtk.Entry(width_chars=23)
        self.tag_name.set_text(tagname.get_text())
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\t\tTag Name "),
                                           self.tag_name]), False, False, 0)

        self.tag_field = Gtk.Entry(width_chars=23)
        self.tag_field.set_text(tagfield.get_text())
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\t\t Tag Field "),
                                           self.tag_field]), False, False, 0)

        scrolledwindow = Gtk.ScrolledWindow(min_content_height=150,
                                            max_content_height=150,
                                            min_content_width=220,
                                            max_content_width=220)
        text_view = Gtk.TextView()
        text_view.set_buffer(the_description)
        self.description = text_view.get_buffer()
        self.description.insert_at_cursor(" ")
        scrolledwindow.add(text_view)
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\t    Description "),
                                           scrolledwindow]), False, False, 0)

        save = Gtk.Button("Save")
        cancel = Gtk.Button("Cancel")
        box.pack_end(GtkUtil.create_box([cancel, save], False), False, False, 0)

        self.add(box)


def run_popwindow(tagname, tagfield, the_description):
    win = SessionWindow(tagname, tagfield, the_description)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
