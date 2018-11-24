import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class StateMachineView(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        box = Gtk.Box()
        state_machine_img = Gtk.Image.new_from_file("statemachine.png")
        box.pack_start(state_machine_img, False, False, 0)
        self.add(box)


def run_popwindow():
    win = StateMachineView()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

