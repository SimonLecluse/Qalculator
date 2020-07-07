from PySide2.QtCore import QObject, Signal, Slot
from src.view import ViewMainFrame
from src.model import Model
from src.dictionnary import dico

class Controller(QObject):
    btn_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self)

        self.operations = ["+", "-", "*", "/", "sqrt", "sq", "**", "(-)" ]

        # Création de la View et connexion avec Controller
        self.gui = ViewMainFrame()
        self.gui.show()

        # Initialisation du signal btn_signal
        self.btn_signal.connect(self.pressed)
        self.gui.central_widget.btn_signal = self.btn_signal

        # Label du texte affiché
        self.txt = "|"
        self.gui.central_widget.label_txt = self.txt

        # Pour associer signal aux fonction de Model)
        self.d = dico()
        self.dico_sig = self.d.sig_dic()

        # Récupère les éléments de la pile
        self.m = Model()
        self.dessus = self.m.x()
        self.reste = self.m.yzt()

        #self.gui.central_widget.label.setText('self.dessus' + '/n' + self.reste[-1] + '/n' + self.reste[-2] + '/n' + self.reste[-3])

    @Slot(str)
    def pressed(self, x):
        if x in '1234567890':
            self.m.set_x(int( str(self.m.x()) + str(x)))
        else:
            eval('self.m.' + self.dico_sig[x])()


        self.gui.central_widget.label.setText(str(self.m.yzt()[-3]) + '\n' + str(self.m.yzt()[-2]) +'\n' + str(self.m.yzt()[-1]) + '\n' + str(self.m.x()))

