from PySide2.QtCore import QObject, Signal, Slot
from src.view import ViewMainFrame


class Controller(QObject):
    btn_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self)

        # Création de la View et connexion avec Controller
        self.gui = ViewMainFrame()
        self.gui.show()

        # Initialisation du signal btn_signal
        self.btn_signal.connect(self.pressed)
        self.gui.central_widget.btn_signal = self.btn_signal

        # Label du texte affiché
        self.txt = "|"
        self.gui.central_widget.label_txt = self.txt



    @Slot(str)
    def pressed(self, nb):
        self.txt += nb
        self.gui.central_widget.label.setText(self.txt)

