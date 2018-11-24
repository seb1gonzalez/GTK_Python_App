import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import create_box
import TagOverlay as to

""""""""""
Name: Tag Area Panel
Author: Chris Santos
Last Modified: Oct. 17th, 2018
"""""""""""


class TagArea(Gtk.Grid):

    tag_name_field = None
    tagged_field = None
    description = None


    def __init__(self):
        Gtk.Grid.__init__(self, row_spacing=10)

        ### Position of the 'Tag Area' title of panel
        area_label = self.displayLabel("Tag Area")
        self.add(area_label)

        ### Position and layout of drop down menu of 'Saved Tag' field
        saved_tag_label = self.displayLabel("\t    Saved Tag")
        saved_tag_menu = self.displayTagMenu()
        self.attach_next_to(saved_tag_label, area_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(saved_tag_menu, saved_tag_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Position and layout of 'Tag Name' field
        tag_name_label = self.displayLabel("\t    Tag Name")
        self.tag_name_field = Gtk.Entry()
        self.attach_next_to(tag_name_label, saved_tag_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(self.displayEntry(self.tag_name_field), tag_name_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Postion and layout of 'Tagged Field' field
        tagged_field_label = self.displayLabel("      Tagged Field")
        self.tagged_field = Gtk.Entry()
        self.attach_next_to(tagged_field_label, tag_name_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(self.displayEntry(self.tagged_field), tagged_field_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Postion and layout of 'Tag Description' field
        tag_des_label = self.displayLabel(" Tag Description")
        scrolledwindow = Gtk.ScrolledWindow(min_content_height=150,
                                            max_content_height=150,
                                            min_content_width=220,
                                            max_content_width=220)
        text_view = Gtk.TextView()
        self.description = text_view.get_buffer()
        self.description.insert_at_cursor(" ")
        scrolledwindow.add(text_view)
        self.attach_next_to(tag_des_label, tagged_field_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(scrolledwindow, tag_des_label, Gtk.PositionType.RIGHT, 1, 2)

        ### Position and layout of 'Update' and 'Cancel' buttons
        update_bttn = Gtk.Button(label="Update")
        update_bttn.connect("clicked", self.on_clicked_update_button)
        cancel_bttn = Gtk.Button(label="Cancel")
        buttons = create_box([update_bttn, cancel_bttn], False)
        self.attach_next_to(buttons, tag_des_label, Gtk.PositionType.BOTTOM, 2, 1)


    def on_clicked_update_button(self, button):
        to.run_popwindow(self.tag_name_field, self.tagged_field, self.description)

    """
    Displays the labels that are to the left of each section.
    """
    def displayLabel(self, name):
        hbox = Gtk.Box(spacing=10)

        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label()
        if (name == "Tag Area"):
            name = "<big>%s</big>" % name
            name = "<u>%s</u>" % name
            label.set_markup("<b>%s</b>" % name)
        else:
            label.set_markup("<b>%s</b>" % name)

        vbox_left.pack_start(label, True, True, 0)

        return hbox

    """
    Displays the drop down menu for the 'Saved Tag' field.
    """
    def displayTagMenu(self):

        # Dummy tag to display
        tag_store = Gtk.ListStore(str)
        tag_store.append(["\t\t\t\t "])
        tag_store.append(["test tag_1"])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        combo_box = Gtk.ComboBox.new_with_model(tag_store)
        renderer_text = Gtk.CellRendererText()
        combo_box.pack_start(renderer_text, True)
        combo_box.add_attribute(renderer_text, "text", 0)

        vbox.pack_start(combo_box, False, False, 0)

        return vbox

    """
    Displays the fields that can have user input.
    """
    def displayEntry(self, entry):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        vbox.pack_start(entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)

        vbox.pack_start(hbox, True, True, 0)

        return vbox

