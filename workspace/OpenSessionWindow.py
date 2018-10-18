import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class OpenSessionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Open Session")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)
        row_1 = Gtk.ListBoxRow()
        row_2 = Gtk.ListBoxRow()
        row_3 = Gtk.ListBoxRow()

        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        box_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)


        label = Gtk.Label("Open an Existing Session")
        box_1.pack_start(label,True,True,0)
        row_1.add(box_1)
        listbox.add(row_1)

        self.username = Gtk.Entry()
        self.username.set_text("Session Name")
        box_2.pack_start(self.username, True, True, 0)
        row_2.add(box_2)

        self.browse_button = Gtk.Button(label="Browse")
        self.browse_button.connect("clicked", self.openBrowse)
        box_2.pack_start(self.browse_button,True,True,0)
        listbox.add(row_2)


        self.open_button = Gtk.Button(label="Open")
        #self.open_button.connect("clicked",self.openSession)
        box_3.pack_start(self.open_button,True,True,0)

        self.cancel_button = Gtk.Button(label="Cancel")
        self.cancel_button.connect("clicked", self.cancel)
        box_3.pack_start(self.cancel_button,True,True,0)
        row_3.add(box_3)
        listbox.add(row_3)





    def openBrowse(self, widget):

        # Gtk.FileChooserAction.SELECT_FOLDER
        dialog = Gtk.FileChooserDialog("Select a file", self, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open button clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()
    def cancel(self,widget):
        self.destroy()







window = OpenSessionWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()



