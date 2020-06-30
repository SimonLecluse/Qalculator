from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout
import sys


class ViewMainFrame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("calculatrice")
        self.setCentralWidget(ViewMainWidget())


class ViewMainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        w = 50      # largeur des boutons
        h = 30      # hauteur des touches

        self.btn_nums = []
        row, col = 4, 2
        for i in range(10):
            self.btn_nums.append(VButtonNum((row, col), (w, h), i, self.button_num_clicked))
            row = 3 - i//3
            col = i % 3 + 1

        # Boutons opérations
        self.bouton_add = QPushButton('+')
        self.bouton_add.setFixedSize(w, h)
        self.bouton_add.clicked.connect(self.button_add_clicked)
        self.bouton_sub = QPushButton('-')
        self.bouton_sub.setFixedSize(w, h)
        self.bouton_sub.clicked.connect(self.button_sub_clicked)
        self.bouton_mul = QPushButton('x')
        self.bouton_mul.setFixedSize(w, h)
        self.bouton_mul.clicked.connect(self.button_mul_clicked)
        self.bouton_div = QPushButton('%')
        self.bouton_div.setFixedSize(w, h)
        self.bouton_div.clicked.connect(self.button_div_clicked)
        self.bouton_opp = QPushButton('(-)')
        self.bouton_opp.setFixedSize(w, h)
        self.bouton_opp.clicked.connect(self.button_opp_clicked)
        self.bouton_sqrt = QPushButton('sqrt')
        self.bouton_sqrt.setFixedSize(w, h)
        self.bouton_sqrt.clicked.connect(self.button_sqrt_clicked)
        self.bouton_sq = QPushButton('x^2')
        self.bouton_sq.setFixedSize(w, h)
        self.bouton_sq.clicked.connect(self.button_sq_clicked)
        self.bouton_pow = QPushButton('x^y')
        self.bouton_pow.setFixedSize(w, h)
        self.bouton_pow.clicked.connect(self.button_pow_clicked)

        # Boutons fonctionnalités
        self.bouton_ac = QPushButton('AC')
        self.bouton_ac.setFixedSize(w, h)
        self.bouton_ac.clicked.connect(self.button_ac_clicked)
        self.bouton_c = QPushButton('C')
        self.bouton_c.setFixedSize(w, h)
        self.bouton_c.clicked.connect(self.button_clear_clicked)
        self.bouton_ent = QPushButton('ENTER')
        self.bouton_ent.setFixedSize(w, h)
        self.bouton_ent.clicked.connect(self.button_enter_clicked)

        self.__set_layout()


        # self.bouton1.clicked.connect(self.on_button_clicked)



    def __set_layout(self):
        layout = QGridLayout()

        for btn in self.btn_nums:
            layout.addWidget(btn, btn.pos[0], btn.pos[1])

        layout.addWidget(self.bouton_add, 4, 4)
        layout.addWidget(self.bouton_sub, 3, 4)
        layout.addWidget(self.bouton_mul, 2, 4)
        layout.addWidget(self.bouton_div, 1, 4)
        layout.addWidget(self.bouton_opp, 0, 4)
        layout.addWidget(self.bouton_sqrt, 0, 3)
        layout.addWidget(self.bouton_sq, 0, 2)
        layout.addWidget(self.bouton_pow, 0, 1)

        layout.addWidget(self.bouton_ac, 5, 1)
        layout.addWidget(self.bouton_c, 5, 2)
        layout.addWidget(self.bouton_ent, 5, 3)


        self.setLayout(layout)

    def button_num_clicked(self, n):
        print(n)
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
        print('ENTER')


class VButtonNum(QPushButton):
    def __init__(self, pos, dim, num, callback):
        QPushButton.__init__(self, str(num))
        self.setFixedSize(dim[0], dim[1])
        self.pos = pos
        self.clicked.connect(lambda: callback(num))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ViewMainFrame()
    gui.show()

    sys.exit(app.exec_())
