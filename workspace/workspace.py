import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Window(Gtk.Window):

    def __init__(self):

        #window setup
        Gtk.Window.__init__(self, title="Team 9 App")
        self.set_border_width(10)
        self.set_default_size(1200, 800)
        #header bar / title bar
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Network Traffic Based Software Generation"
        self.set_titlebar(hb)

        #create a grid that will be inserted into a notebook
        grid = Gtk.Grid()

        #create buttons
        self.create_session_button = Gtk.Button(label="Create Session")
        self.create_session_button.connect("clicked", self.create_session_clicked)


        self.open_session_button = Gtk.Button(label="Open Session")
        self.open_session_button.connect("clicked", self.open_session_clicked)


        self.close_session_button = Gtk.Button(label="Close Session")
        self.close_session_button.connect("clicked", self.close_session_clicked)


        self.switch_workspace_button = Gtk.Button(label="Switch Workspace")
        self.switch_workspace_button.connect("clicked", self.switch_workspace_clicked)


        self.open_pcap_button = Gtk.Button(label="Open PCAP")
        self.open_pcap_button .connect("clicked", self.open_pcap_clicked)


        self.open_terminal_button = Gtk.Button(label="Terminal")
        self.open_terminal_button.connect("clicked", self.open_terminal_clicked)

        #attach buttons together in grid
        grid.attach(self.create_session_button, 0, 0, 2, 2)
        grid.attach_next_to(self.open_session_button, self.create_session_button, Gtk.PositionType.RIGHT, 2, 2)
        grid.attach_next_to(self.close_session_button, self.open_session_button, Gtk.PositionType.RIGHT, 2, 2)
        grid.attach_next_to(self.switch_workspace_button, self.close_session_button, Gtk.PositionType.RIGHT, 2, 2)
        grid.attach_next_to(self.open_pcap_button, self.switch_workspace_button, Gtk.PositionType.RIGHT, 2, 2)
        grid.attach_next_to(self.open_terminal_button, self.open_pcap_button, Gtk.PositionType.RIGHT, 2, 2)

        #create notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # First tab
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)

        #adding the grid to the notebook
        self.page1.add(grid)
        self.notebook.append_page(self.page1, Gtk.Label('First Tab'))

        # Second tab
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('Tab 2 contents.'))

        self.notebook.append_page(self.page2, Gtk.Label('Second Tab'))

        # Third tab
        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Label('Tab 3 contents.'))

        self.notebook.append_page(self.page3, Gtk.Label('Third Tab'))







    def create_session_clicked(self, widget):
        print "create session clicked"


    def open_session_clicked(self, widget):
        print("open_session_clicked")


    def close_session_clicked(self, widget):
        print("close_session_clicked")


    def switch_workspace_clicked(self, widget):
        print("switch_workspace_clicked")

    def open_pcap_clicked(self, widget):
        print("open_pcap_clicked")

    def open_terminal_clicked(self, widget):
        print("open_terminal_clicked")

win =Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()