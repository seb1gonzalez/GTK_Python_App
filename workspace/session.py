import gi.repository
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Create the session itself with save states below
class Session(Gtk.Box):

    def __init__(self, name="Session"):
        Gtk.Box.__init__(self, orientation = Gtk.Orientation.VERTICAL, spacing = 1)
        self.set_border_width(3)
        self.name = Gtk.Button(label = name)
        self.add(self.name)

        self.states = Gtk.ListBox()
        self.states.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(self.states)

    # add button for state to listbox
    def saveState(self, name="state"):
        state = Gtk.Button(label = name)
        self.states.add(state)


#A listbox of Sessions
class SessionView(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_border_width(10)

        head = Gtk.HeaderBar()
        head.props.title = "Session View"
        self.add(head)

        self.sessions = Gtk.ListBox()
        self.sessions.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(self.sessions)

    #Add a new session to the listbox
    def saveSession(self, name="session"):
        session = Session(name)
        self.sessions.add(session)
        return session


sessWindow = SessionView()
window = Gtk.Window()
window.add(sessWindow)

sess1 = sessWindow.saveSession("Session1")
sess2 = sessWindow.saveSession("Session2")
sess1.saveState("state1")
sess1.saveState("state2")
sess2.saveState("test")

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()