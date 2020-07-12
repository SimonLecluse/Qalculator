from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtCore import Qt
from src.dictionnary import dico
from PySide2.QtGui import QPalette, QColor


class ViewMainFrame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("calculatrice")
        self.central_widget = ViewMainWidget()
        self.setCentralWidget(self.central_widget)


class ViewMainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        w = 75      # largeur des boutons
        h = 50      # hauteur des touches

        self.pos_btn = [(5,2)] + [(4 - i//3,i % 3 + 1) for i in range(9)] + [(5-i,4) for i in range(4)] + [(1,4-i) for i in range(4)] + [(6,i+1) for i in range(3)] + [(5,3)]
        self.btn = []           # Liste des objets Boutons
        self.d = dico()
        self.btn_dic = self.d.button_dic()     # Boutons Opérations et Fonctionnalités liés à leurs fonctions correspondantes

        # Boutons Chiffres
        for i in range(10):
            self.btn.append(VButtonNum((self.pos_btn[i][0], self.pos_btn[i][1]), (w, h), i, self.button_num_clicked))

        # Boutons Opérations / Fonctionnalités
        for i in range(10,22):
            self.btn.append(VButtonNum((self.pos_btn[i][0], self.pos_btn[i][1]), (w,h), self.btn_dic[i][0], eval("self."+self.btn_dic[i][1])))

        self.display = Screen()

        # Affichage des boutons sur la grille
        self.__set_layout()

        self.btn_signal = None      # Definition du signal


    def __set_layout(self):

        layout_btn = QGridLayout()          # Layout des boutons
        layout_screen = QVBoxLayout()       # Layout de l'écran

        for btn_i in self.btn:              # Ajout des boutons dans la layout
            if btn_i.name == "ENTER":
                layout_btn.addWidget(btn_i, btn_i.pos[0], btn_i.pos[1], 1, 2)
            else:
                layout_btn.addWidget(btn_i, btn_i.pos[0], btn_i.pos[1])
        layout_screen.addWidget(self.display)
        layout_screen.addLayout(layout_btn)

        self.setLayout(layout_screen)

    def button_num_clicked(self, n):
        self.btn_signal.emit(str(n))
    def button_add_clicked(self):
        self.btn_signal.emit('+')
    def button_sub_clicked(self):
        self.btn_signal.emit('-')
    def button_mul_clicked(self):
        self.btn_signal.emit('*')
    def button_div_clicked(self):
        self.btn_signal.emit('/')
    def button_opp_clicked(self):
        self.btn_signal.emit('*(-1)')
    def button_sqrt_clicked(self):
        self.btn_signal.emit('sqrt')
    def button_sq_clicked(self):
        self.btn_signal.emit('x^2')
    def button_pow_clicked(self):
        self.btn_signal.emit('y^x')
    def button_ac_clicked(self):
        self.btn_signal.emit('AC')
    def button_clear_clicked(self):
        self.btn_signal.emit('c')
    def button_enter_clicked(self):
        self.btn_signal.emit('enter')
    def button_lastx_clicked(self):
        self.btn_signal.emit('lastx')



class VButtonNum(QPushButton):
    def __init__(self, pos, dim, name, callback):
        QPushButton.__init__(self, str(name))
        self.setFixedHeight(dim[1])
        self.pos = pos
        self.name = str(name)

        if type(name) is int:
            self.clicked.connect(lambda: callback(name))
            self.setStyleSheet("color: blue; border: 1px solid blue")
        else:
            if name == "ENTER":
                self.setStyleSheet("color: orange;")
            self.clicked.connect(callback)

class Screen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Création de la zone de texte
        self.label_pile_txt = "0\n0\n0\n0\n0"
        self.label_names_txt = "Last x\nt\nz\ny\nx"

        self.label_pile = QLabel()
        self.label_pile.setAlignment(Qt.AlignRight)
        self.label_pile.setText(self.label_pile_txt)
        self.label_pile.setStyleSheet("color: white;")

        self.label_names = QLabel()
        self.label_names.setAlignment(Qt.AlignLeft)
        self.label_names.setText(self.label_names_txt)
        self.label_names.setStyleSheet("color: white;")

        self.layout_names = QHBoxLayout()        # Layout noms des lignes
        self.layout_names.addWidget(self.label_names, alignment=Qt.AlignLeft)
        self.layout_names.addWidget(self.label_pile, alignment=Qt.AlignRight)

        self.setLayout(self.layout_names)

        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor("green"))
        self.setPalette(pal)

