import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GtkUtil import create_box
from GtkUtil import bold_label

""""""""""
Name: Tag Area Panel
Author: Chris Santos
Last Modified: Oct. 17th, 2018
"""""""""""


class TagArea(Gtk.Grid):

    def __init__(self, the_iserver):
        Gtk.Grid.__init__(self, row_spacing=10)

        # Global variables
        self.tag_name = Gtk.Entry()
        self.tagged_field = Gtk.Entry(editable=False)
        self.iserver = the_iserver
        self.tag_cbox = None

        # Position of the 'Tag Area' title of panel
        area_label = self.displayLabel("Tag Area")
        self.add(area_label)

        # Position and layout of drop down menu of 'Saved Tag' field
        saved_tag_label = self.displayLabel("\t    Saved Tag")
        saved_tag_box = self.create_tag_cbox()
        self.attach_next_to(saved_tag_label, area_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(saved_tag_box, saved_tag_label, Gtk.PositionType.RIGHT, 1, 2)

        # Position and layout of 'Tag Name' field
        tag_name_label = self.displayLabel("\t    Tag Name")
        self.attach_next_to(tag_name_label, saved_tag_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(self.displayEntry(self.tag_name), tag_name_label, Gtk.PositionType.RIGHT, 1, 2)

        # Postion and layout of 'Tagged Field' field
        tagged_field_label = self.displayLabel("      Tagged Field")
        self.attach_next_to(tagged_field_label, tag_name_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(self.displayEntry(self.tagged_field), tagged_field_label, Gtk.PositionType.RIGHT, 1, 2)

        # Position and layout of 'Tag Description' field
        tag_des_label = self.displayLabel(" Tag Description")
        scrolledwindow = Gtk.ScrolledWindow(min_content_height=150,
                                            max_content_height=150,
                                            min_content_width=220,
                                            max_content_width=220)
        text_view = Gtk.TextView(buffer=Gtk.TextBuffer())
        self.description = text_view.get_buffer()
        scrolledwindow.add(text_view)
        self.attach_next_to(tag_des_label, tagged_field_label, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(scrolledwindow, tag_des_label, Gtk.PositionType.RIGHT, 1, 2)

        # Position and layout of 'Update' and 'Cancel' buttons
        update_bttn = Gtk.Button(label="Update")
        update_bttn.connect("clicked", self.on_clicked_update_button)
        cancel_bttn = Gtk.Button(label="Cancel")
        buttons = create_box([update_bttn, cancel_bttn], False)
        self.attach_next_to(buttons, tag_des_label, Gtk.PositionType.BOTTOM, 2, 1)

    def on_clicked_update_button(self, button):
        tag_name = self.tag_name.get_text()
        tagged_field = self.tagged_field.get_text()
        description = self.description.get_text(self.description.get_start_iter(),
                                                self.description.get_end_iter(),
                                                False)
        if tag_name != "" and tagged_field != "":
            tag_store = self.tag_cbox.get_model()
            active_index = self.tag_cbox.get_active()
            if active_index == 0:
                was_created = self.iserver.add_tag(tag_name, description, tagged_field)
                if was_created:
                    tag_store.append([tag_name])
            else:
                old_name = tag_store[active_index][0]
                was_updated = self.iserver.update_tag(old_name, tag_name, tagged_field, description)
                if was_updated:
                    tag_store[active_index][0] = tag_name

    def set_field_name(self, field_name):
        self.tagged_field.set_text(field_name)

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
        if name == "Tag Area":
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
    def create_tag_cbox(self):

        # Dummy tag to display
        tag_store = Gtk.ListStore(str)
        tag_store.append(["\t\t\t\t "])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        self.tag_cbox = Gtk.ComboBox.new_with_model(tag_store)
        renderer_text = Gtk.CellRendererText()
        self.tag_cbox.pack_start(renderer_text, True)
        self.tag_cbox.add_attribute(renderer_text, "text", 0)
        self.tag_cbox.set_active(0)
        self.tag_cbox.connect("changed", self._display_tag)

        vbox.pack_start(self.tag_cbox, False, False, 0)

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

    def _display_tag(self, cbox):
        tag_store = self.tag_cbox.get_model()
        active_index = self.tag_cbox.get_active()

        if active_index > 0:
            tag_name = tag_store[active_index][0]
            tag = self.iserver.get_tag(tag_name)

            self.tag_name.set_text(tag.get_name())
            self.tagged_field.set_text(tag.get_field_name())
            self.description.set_text(tag.get_description())


# class TagOverlay(Gtk.Window):
#
#     def __init__(self, tagname, tagfield, the_description, iserver):
#         Gtk.Window.__init__(self, title="Tag Overlay")
#         self.set_default_size(400, 320)
#
#         # Global Variables
#         self.iserver = iserver
#         self.was_created = False
#
#         box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
#         box.pack_start(Gtk.Label("\n"), False, False, 0)                # REMOVE LATER
#
#         self.tag_name = Gtk.Entry(width_chars=23)
#         self.tag_name.set_text(tagname.get_text())
#         box.pack_start(create_box([bold_label("\t\tTag Name "),
#                                    self.tag_name]), False, False, 0)
#
#         self.tag_field = Gtk.Entry(width_chars=23, editable=False)
#         self.tag_field.set_text(tagfield.get_text())
#         box.pack_start(create_box([bold_label("\t\t Tag Field "),
#                                    self.tag_field]), False, False, 0)
#
#         scrolledwindow = Gtk.ScrolledWindow(min_content_height=150,
#                                             max_content_height=150,
#                                             min_content_width=220,
#                                             max_content_width=220)
#         text_view = Gtk.TextView(buffer=Gtk.TextBuffer())
#         self.description = text_view.get_buffer()
#         self.description.insert_at_cursor(the_description.get_text(the_description.get_start_iter(),
#                                                                    the_description.get_end_iter(),
#                                                                    False))
#         scrolledwindow.add(text_view)
#         box.pack_start(create_box([bold_label("\t    Description "),
#                                    scrolledwindow]), False, False, 0)
#
#         save = Gtk.Button("Save")
#         save.connect("clicked", self.on_save_click)
#         cancel = Gtk.Button("Cancel")
#         cancel.connect("clicked", self.on_cancel_click)
#         box.pack_end(create_box([cancel, save], False), False, False, 0)
#
#         self.add(box)
#
#         self.connect("destroy", Gtk.main_quit)
#         self.show_all()
#         Gtk.main()
#
#     def on_save_click(self, button):
#         tag_name = self.tag_name.get_text()
#         tagged_field = self.tag_field.get_text()
#         description = self.description.get_text(self.description.get_start_iter(),
#                                                 self.description.get_end_iter(),
#                                                 False)
#         self.was_created = self.iserver.add_tag(tag_name, description, tagged_field)
#         self.destroy()
#
#     def on_cancel_click(self, button):
#         self.was_created = False
#         self.destroy()
#
#     def was_tag_created(self):
#         return self.was_created
#
#     def get_tag_name(self):
#         return self.tag_name.get_text()
#
#     def get_descrip_buffer(self):
#         return self.description


