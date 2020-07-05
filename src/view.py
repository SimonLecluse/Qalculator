from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PySide2.QtCore import Qt
import sys


class ViewMainFrame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("calculatrice")
        self.central_widget = ViewMainWidget()
        self.setCentralWidget(self.central_widget)


class ViewMainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        w = 50      # largeur des boutons
        h = 30      # hauteur des touches

        self.pos_btn = [(4,2)] + [(4 - i//3,i % 3 + 1) for i in range(9)] + [(5-i,4) for i in range(4)] + [(1,4-i) for i in range(4)] + [(6,i+1) for i in range(3)]
        self.btn = []           # Liste des objets Boutons
        self.dic = dico()       # Boutons Opérations et Fonctionnalités liés à leurs fonctions correspondantes

        # Boutons Chiffres
        for i in range(10):
            self.btn.append(VButtonNum((self.pos_btn[i][0], self.pos_btn[i][1]), (w, h), i, self.button_num_clicked))
        # Boutons Opérations
        for i in range(10,21):
            self.btn.append(VButtonNum((self.pos_btn[i][0], self.pos_btn[i][1]), (w,h), self.dic.button_dic()[i][0], eval("self."+self.dic.button_dic()[i][1])))

        # Création de la zone de texte
        self.label_txt = ""
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignRight)
        self.label.setText(self.label_txt)

        # Affichage des boutons sur la grille
        self.__set_layout()

        self.btn_signal = None      # Definition du signal


    def __set_layout(self):
        layout_btn = QGridLayout()          # Layout des boutons
        layout_screen = QVBoxLayout()       # Layout écran + boutons

        for btn_i in self.btn:              # Ajout des boutons dans la layout
            layout_btn.addWidget(btn_i, btn_i.pos[0], btn_i.pos[1])

        layout_screen.addWidget(self.label, alignment=Qt.AlignRight)
        layout_screen.addLayout(layout_btn)

        self.setLayout(layout_screen)


    def button_num_clicked(self, n):
        self.btn_signal.emit(str(n))
    def button_add_clicked(self):
        print('+')
    def button_sub_clicked(self):
        print('-')
    def button_mul_clicked(self):
        print('x')
    def button_div_clicked(self):
        print('%')
    def button_opp_clicked(self):
        print('<->')
    def button_sqrt_clicked(self):
        print('sqrt')
    def button_sq_clicked(self):
        print('x^2')
    def button_pow_clicked(self):
        print('^')
    def button_ac_clicked(self):
        print('AC')
    def button_clear_clicked(self):
        print('c')
    def button_enter_clicked(self):
        self.label.setText("enter")


class VButtonNum(QPushButton):
    def __init__(self, pos, dim, name, callback):
        QPushButton.__init__(self, str(name))
        self.setFixedSize(dim[0], dim[1])
        self.pos = pos

        if type(name) is int:
            self.clicked.connect(lambda: callback(name))
        else:
            self.clicked.connect(callback)

class dico:
    def __init__(self):
        self.__button_dic = {
            10 : ['+', 'button_add_clicked'],
            11 : ['-', 'button_sub_clicked'],
            12 : ['x', 'button_mul_clicked'],
            13 : ['%', 'button_div_clicked'],
            14 : ['*(-1)', 'button_opp_clicked'],
            15 : ['sqrt', 'button_sqrt_clicked'],
            16 : ['x^2', 'button_sq_clicked'],
            17 : ['x^y', 'button_pow_clicked'],
            18 : ['AC', 'button_ac_clicked'],
            19 : ['clear', 'button_clear_clicked'],
            20 : ['ENTER', 'button_enter_clicked'] }

    def button_dic(self):
        return self.__button_dic
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ViewMainFrame()
    gui.show()


    sys.exit(app.exec_())"""
