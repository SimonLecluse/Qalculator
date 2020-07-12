# Controller

from PySide2.QtCore import QObject, Signal, Slot
from src.view import ViewMainFrame
from src.model import Model
from src.dictionnary import dico
from configparser import ConfigParser


class Controller(QObject):
    btn_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self)

        self.operations = ["+", "-", "*", "/", "sqrt", "sq", "**", "(-)" ]

        self.config = ConfigParser()
        self.config.read("config.ini")

        # Création de la View et connexion avec Controller
        self.gui = ViewMainFrame()
        self.gui.show()

        # Initialisation du signal btn_signal
        self.btn_signal.connect(self.pressed)
        self.gui.central_widget.btn_signal = self.btn_signal

        # Pour associer signal aux fonction de Model)
        self.d = dico()
        self.dico_sig = self.d.sig_dic()

        # Récupère les éléments de la pile, et définition du mode singe
        self.m = Model()
        self.dessus = self.m.x()
        self.reste = self.m.yzt()
        self.m.mode_singe = self.gui.central_widget.btn_singe.isChecked()

    @Slot(str)
    def pressed(self, x):
        self.m.mode_singe = self.gui.central_widget.btn_singe.isChecked()
        if x in '1234567890':
            if self.m.change:
                self.m.empile(0)
                self.m.change = False
            elif self.m.etat_enter:         # Enter est la derniere action => ne doit pas ajouter x mais remplacer
                self.m.set_x(0)
                self.m.etat_enter = False
            self.m.set_x(int( str(self.m.x()) + str(x)))
        else:
            eval('self.m.' + self.dico_sig[x])()

        self.gui.central_widget.display.label_pile.setText(str(self.m.last_x) + '\n' + str(self.m.yzt()[-3]) + '\n' + str(self.m.yzt()[-2]) +'\n' + str(self.m.yzt()[-1]) + '\n' + str(self.m.x()))

