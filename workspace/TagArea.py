import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

""""""""""
Name: Tag Area Panel
Author: Chris Santos
Last Modified: Oct. 17th, 2018
"""""""""""

class TagAreaPanel(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tag Area Panel")
        self.set_border_width(20)
        self.set_frame()

    """
    Creates the frame/grid for the 'Tag Area' panel in the system.
    Help lessen the # of lines in the constructor.
    """
    def set_frame(self):
        grid = Gtk.Grid()
        self.add(grid)

        ### Position of the 'Tag Area' title of panel
        area_label = self.displayLabel("Tag Area")
        grid.add(area_label)

        ### Position and layout of drop down menu of 'Saved Tag' field
        saved_tag_label = self.displayLabel("Saved Tag")
        saved_tag_menu = self.displayTagMenu()
        grid.attach_next_to(saved_tag_label, area_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(saved_tag_menu, saved_tag_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Position and layout of 'Tag Name' field
        tag_name_label = self.displayLabel("Tag Name")
        tag_name_field = self.displayEntry()
        grid.attach_next_to(tag_name_label, saved_tag_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(tag_name_field, tag_name_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Postion and layout of 'Tagged Field' field
        tagged_field_label = self.displayLabel("Tagged Field")
        tagged_field = self.displayEntry()
        grid.attach_next_to(tagged_field_label, tag_name_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(tagged_field, tagged_field_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Postion and layout of 'Tag Description' field
        tag_des_label = self.displayLabel("Tag Description")
        tag_des_field = self.displayEntry()
        grid.attach_next_to(tag_des_label, tagged_field_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(tag_des_field, tag_des_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Position and layout of 'Update' and 'Cancel' buttons
        update_bttn = Gtk.Button(label="Update")
        cancel_bttn = Gtk.Button(label="Cancel")
        grid.attach_next_to(update_bttn, tag_des_label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(cancel_bttn, update_bttn, Gtk.PositionType.RIGHT, 1, 2)

    """
    Displays the labels that are to the left of each section.
    """
    def displayLabel(self, name):
        hbox = Gtk.Box(spacing=20)

        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label()
        if (name == "Tag Area"):
            name = "<big>%s</big>" % name
            name = "<u>%s</u>" % name
            name = "<i>%s</i>" % name
            label.set_markup("<b>%s</b>" % name)
        else:
            label.set_markup("<i>%s</i>" % name)

        vbox_left.pack_start(label, True, True, 0)

        return hbox

    """
    Displays the drop down menu for the 'Saved Tag' field.
    """
    def displayTagMenu(self):
        tag_store = Gtk.ListStore(str)

        # Dummy tag to display
        tag_store.append(["test tag_1"])

        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=10)

        combo_box = Gtk.ComboBox.new_with_model_and_entry(tag_store)

        vbox.pack_start(combo_box, False, False, 0)

        return vbox

    """
    Displays the fields that can have user input.
    """
    def displayEntry(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.entry = Gtk.Entry()

        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)

        vbox.pack_start(hbox, True, True, 0)

        return vbox

window = TagAreaPanel()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()