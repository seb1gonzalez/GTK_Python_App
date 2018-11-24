import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ast import literal_eval
from GtkUtil import bold_label
from GtkUtil import create_box


class FilterWindow(Gtk.Window):

    def __init__(self, the_filter_expresion):
        Gtk.Window.__init__(self, title="Filter")
        self.set_default_size(400, 260)
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        filter_section = Gtk.Box(spacing=15)

        scrolledwindow = Gtk.ScrolledWindow(min_content_height=170,
                                            max_content_height=210,
                                            min_content_width=500,
                                            max_content_width=600)
        scrolledwindow.add(create_box([FilterTable()]))
        scrolledwindow.set_hadjustment(Gtk.Adjustment(value=1000, lower=1000))
        filter_section.pack_start(scrolledwindow, False, False, 0)

        buttons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        copy = Gtk.Button("Copy")
        buttons.pack_end(copy, False, False, 0)
        update = Gtk.Button("Update")
        buttons.pack_end(update, False, False, 0)
        delete = Gtk.Button("Delete")
        buttons.pack_end(delete, False, False, 0)
        filter_section.pack_start(buttons, False, False, 0)
        box.pack_start(filter_section, False, False, 0)

        instructions = bold_label("\nCreate/Update a Filter\n")
        box.pack_start(instructions, False, False, 0)

        filter_name = Gtk.Entry(width_chars=15)
        box.pack_start(create_box([bold_label("\t\t\t  Filter Name "),
                                   filter_name]), False, False, 0)

        filter_expression = Gtk.Entry(width_chars=15)
        filter_expression.set_text(the_filter_expresion)
        box.pack_start(create_box([bold_label("\t\tFilter Expression "),
                                   filter_expression]), False, False, 0)

        save = Gtk.Button("Save")
        cancel = Gtk.Button("Cancel")
        box.pack_end(create_box([cancel, save], False), False, False, 0)

        self.add(box)


class FilterTable(Gtk.Grid):

    filters = []
    check_buttons = []

    def __init__(self):
        Gtk.Grid.__init__(self, column_homogeneous=False, row_spacing=10, column_spacing=10)

        headers = [Gtk.Label(""), bold_label("  Saved Filter  "), bold_label("  Filter Expression  ")]
        self.fill_row(0, headers)
        self.update_filters("filter_default.txt")

    def fill_row(self, row, items):
        for index, item in enumerate(items):
            self.attach(item, index, row, 1, 1)

    def update_filters(self, filename):
        f = open(filename, "r")

        row = 1
        line = f.readline().strip('\n')
        while line:
            dict_filter = literal_eval(line)
            self.filters.append(dict_filter)
            self.build_filter_row(row, dict_filter)
            line = f.readline().strip('\n')
            row = row + 1
        f.close()

    def build_filter_row(self, row, dict_filter):
        check_button = Gtk.CheckButton()
        self.check_buttons.append(check_button)

        filtername = Gtk.Label(dict_filter['filtername'])
        expression = Gtk.Label(dict_filter['expression'])

        items = [check_button, filtername, expression]
        self.fill_row(row, items)


def run_popwindow(filter_expression):
    win = FilterWindow(filter_expression)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
