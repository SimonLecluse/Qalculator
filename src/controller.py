from PySide2.QtCore import QObject, Signal, Slot
from src.view import ViewMainFrame


class controller(QObject):
    button_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self):

        # Création de la View et connexion avec Controller
        self.gui = ViewMainFrame()
        self.gui.central_widget
        self.button_signal.connect()

    Slot(str)
    def press(self):
        