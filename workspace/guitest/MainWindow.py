import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PDMLView import PDMLView
from SessionView import SessionView
import GtkUtil as gu
import WorkspaceLauncher as wl
from PCAPwindow import PCAPWindow
import SessionPopout as sp
from TagArea import TagArea
from os import system
import OpenSessionWindow as osw
import StateMachineView as smv
from backend.User import User


class MainWindow(Gtk.Window):
    user = None
    pdmlview = None

    def __init__(self):
        Gtk.Window.__init__(self, title="NTBSG")
        container = Gtk.Grid(row_spacing=20, column_spacing=7)

        self.user = User()
        self.user.add_workspace().add_session()     # default create user, workspace, and session

        header = self.create_window_header()
        container.attach(header, 0, 0, 4, 1)

        buttons_box = self.create_stages_buttons()
        container.attach(buttons_box, 0, 1, 4, 1)

        self.pdml_view = PDMLView()
        container.attach(self.pdml_view, 1, 2, 3, 2)

        session_view = SessionView()
        container.attach(session_view, 0, 2, 1, 1)

        tag_area = TagArea()
        container.attach(tag_area, 0, 3, 1, 1)

        self.add(container)

    def create_window_header(self):
        system_title = gu.bold_label("  Network Traffic Based Software Generation")
        create_session = Gtk.Button("Create Session")
        create_session.connect("clicked", self.on_clicked_create_session)

        open_session = Gtk.Button("Open Session")
        open_session.connect("clicked", self.on_clicked_open_session)

        close_session = Gtk.Button("Close Session")

        switch_workspace = Gtk.Button("Switch Workspace")
        switch_workspace.connect("clicked", self.on_clicked_switch_workspace)

        open_pcap = Gtk.Button("Open PCAP")
        open_pcap.connect("clicked", self.on_clicked_open_pcap)

        terminal = Gtk.Button("Terminal")
        terminal.connect("clicked", self.on_clicked_terminal)

        box = gu.create_box([system_title, create_session, open_session,
                             close_session, switch_workspace, open_pcap, terminal])
        box.set_spacing(15)
        return box

    def on_clicked_switch_workspace(self, button):
        wl.run_popwindow()

    def on_clicked_open_pcap(self, button):
        pcap_window = PCAPWindow()

        created_pdml = pcap_window.get_pdmlfile()
        if created_pdml is not None:
            session = self.user.getworkspace().getsession()
            pdmlstate = session.add_pdmlstate(created_pdml)
            self.pdml_view.update_packet_area(pdmlstate)

    def on_clicked_create_session(self, button):
        sp.run_popwindow()

    def on_clicked_open_session(self, button):
        osw.run_popwindow()

    def on_clicked_terminal(self, button):
        test_path = "/home/jesus/PycharmProjects/code/"
        system("gnome-terminal -e 'bash -c \"cd '" + test_path + "'; exec bash\"'")

    def create_stages_buttons(self):
        stage1_img = Gtk.Image.new_from_file("stage1.png")
        stage1_button = Gtk.Button()
        stage1_button.add(stage1_img)

        stage2_img = Gtk.Image.new_from_file("stage2.png")
        stage2_button = Gtk.Button()
        stage2_button.add(stage2_img)

        stage3_img = Gtk.Image.new_from_file("stage3.png")
        stage3_button = Gtk.Button()
        stage3_button.connect("clicked", self.on_clicked_stage3)
        stage3_button.add(stage3_img)

        stage4_img = Gtk.Image.new_from_file("stage4.png")
        stage4_button = Gtk.Button()
        stage4_button.add(stage4_img)

        buttons = gu.create_box([Gtk.Label("\t\t"), stage1_button, stage2_button,  # REMOVE LATER
                                 stage3_button, stage4_button])
        buttons.set_spacing(70)
        return buttons

    def on_clicked_stage3(self, button):
        smv.run_popwindow()


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

