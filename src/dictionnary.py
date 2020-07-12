class dico:
    def __init__(self):
        # associe numéros boutons aux fonctions View
        self.__button_dic = {
            10 : ['+', 'button_add_clicked'],
            11 : ['-', 'button_sub_clicked'],
            12 : ['*', 'button_mul_clicked'],
            13 : ['/', 'button_div_clicked'],
            14 : ['+/-', 'button_opp_clicked'],
            15 : ['sqrt', 'button_sqrt_clicked'],
            16 : ['x^2', 'button_sq_clicked'],
            17 : ['y^x', 'button_pow_clicked'],
            18 : ['clst', 'button_ac_clicked'],
            19 : ['clx', 'button_clear_clicked'],
            20 : ['ENTER', 'button_enter_clicked'],
            21 : ['LastX', 'button_lastx_clicked'] }
        # associe signaux aux fonctions Model
        self.__sig_dic = {
            '+' : 'plus',
            '-' : 'moins',
            '*' : 'mult',
            '/' : 'div',
            '*(-1)' : 'opp',
            'sqrt' : 'racine',
            'x^2' : 'carre',
            'y^x' : 'puiss',
            'AC' : 'ac',
            'c' : 'clear',
            'enter' : 'enter',
            'lastx' : 'lastx'}

    def button_dic(self):
        return self.__button_dic

    def sig_dic(self):
        return self.__sig_dic
