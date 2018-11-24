import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import GtkUtil


class WorkspaceLauncher(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")
        self.set_default_size(360, 260)

        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        instructions = Gtk.Label()
        instructions.set_markup("Select a directory as workspace: NTBSG"
                                "uses the workspace\n directory to store sessions.\n")
        box.pack_start(instructions, False, False, 0)

        workspace_entry = Gtk.Entry(width_chars=15)
        browse_workspace = Gtk.Button("Browse")
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tWorkspace    "),
                                           workspace_entry,
                                           browse_workspace]), False, False, 0)

        folder_name_entry = Gtk.Entry(width_chars=15)
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tDestination "
                                                              "\n\tFolder Name "),
                                           folder_name_entry]), False, False, 0)
        folder_path_entry = Gtk.Entry(width_chars=15)
        browse_folder = Gtk.Button("Browse")
        box.pack_start(GtkUtil.create_box([GtkUtil.bold_label("\tDestination "
                                                              "\n\tFolder Path   "),
                                           folder_path_entry,
                                           browse_folder]), False, False, 0)

        launch = Gtk.Button("Launch")
        cancel = Gtk.Button("Cancel")
        box.pack_end(GtkUtil.create_box([cancel, launch], False), False, False, 0)

        self.add(box)


def run_popwindow():
    win = WorkspaceLauncher()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
