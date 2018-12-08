import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def create_box(items, align=True):
    box = Gtk.Box()
    if align:
        for item in items:
            box.pack_start(item, False, False, 0)
    else:
        for item in items:
            box.pack_end(item, False, False, 0)
    return box

def bold_label(string):
    label = Gtk.Label()
    label.set_markup("<b>" + string + "</b>")
    return label


def create_small_label(string):
    label = Gtk.Label()
    label.set_markup("<small>" + string + "</small>")
    return label


def show_error_dialog(parent, error_msg):
    dialog = Gtk.Dialog(parent, "Error", 0)
    dialog.set_default_size(200, 150)
    box = dialog.get_content_area()
    box.add(Gtk.Label("\n"+error_msg))
    dialog.show_all()
