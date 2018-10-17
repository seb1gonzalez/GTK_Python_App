import gi.repository
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

"""
Author: Topher Tighe
10/17/18
"""

class SessionPopout(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "New Session", parent, Gtk.DialogFlags.MODAL, (
            "Create", Gtk.ResponseType.OK, #Create Buttons
            "Cancel", Gtk.ResponseType.CANCEL
        ))
        self.set_default_size(500, 300)
        self.set_border_width(10)

        area = self.get_content_area()
        area.add(Gtk.Label("Create a new session."))
        grid = Gtk.Grid()
        area.add(grid)

        #Create label and first text box
        nameLabel = Gtk.Label("Session Name:")
        grid.attach(nameLabel, 0, 0, 1, 1)
        self.sessName = Gtk.Entry()
        self.sessName.set_text("Project Name")
        grid.attach(self.sessName, 1, 0, 1, 1)

        #Create label and second text box
        descLabel = Gtk.Label("Description:")
        grid.attach(descLabel, 0, 1, 1, 1)
        self.desc = Gtk.Entry()
        self.desc.set_text("Project Description")
        grid.attach(self.desc, 1, 1, 1, 1) #I couldn't make this one bigger for some reason.
        self.show_all()

    #This will be called to make the session objects.
    def getValues(self):
        return self.sessName.get_text(), self.desc.get_text()


#This is copied from the tutorial videos Seb G sent us.
#It only exists to test SessionPopout.
class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="TESTER")
        self.set_default_size(200, 100)
        self.set_border_width(10)
        button = Gtk.Button("test")
        button.connect("clicked", self.button_clicked)
        self.add(button)

    def button_clicked(self, widget):
        dialog = SessionPopout(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print dialog.getValues()
        elif response == Gtk.ResponseType.CANCEL:
            print "Butterscotch"

        dialog.destroy()


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
