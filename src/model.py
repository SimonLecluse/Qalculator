class Model:

    def __init__(self):
        self.__reste = [0, 0, 0]        # initialisation du reste de la pile [t, z, y]
        self.__dessus = 0               # initialisation du dessus de la pile X
        self.change = False             # si il y a eu opération sur le nombre x, prochain nombre tapé empile
        self.error = False              # erreur de racine négative / division par 0
        self.etat_enter = False             # si enter, si on tape un nb, x doit etre remplacé
        self.mode_singe = False
        self.last_x = self.__dessus

    def empile(self, val):
        """Empile val sur la pile"""
        self.__reste.append(self.__dessus)
        self.__reste.pop(0)
        self.__dessus = val

    def depile(self):
        """Retourne la valeur du dessus de la pile, et la retire de la pile"""
        r = self.__dessus
        self.__dessus = self.__reste[-1]
        self.__reste.insert(0,self.__reste[0])
        self.__reste.pop(-1)

        return r

    # Dessus de la pile
    def x(self):
        return self.__dessus
    def set_x(self, x1):
        self.__dessus = x1

    #Reste de la pile [t,z,y]
    def yzt(self):
        return self.__reste
    def set_yzt(self, reste1):
        self.__reste = reste1

    # Opérations algébriques élémentaires

    def plus(self):
        """Y + X"""
        self.last_x = self.__dessus
        if self.__dessus == 1 and self.__reste[-1] == 1 and eval(self.mode_singe):
            self.depile()
            self.depile()
            self.empile(3)
        else:
            self.empile(self.depile() + self.depile())
        self.change = True

    def moins(self):
        """Y - X"""
        self.last_x = self.__dessus
        x2 = self.depile()
        y2 = self.depile()
        self.empile(y2 - x2)
        self.change = True

    def mult(self):
        """Y * X"""
        self.last_x = self.__dessus
        self.empile(self.depile() * self.depile())
        self.change = True

    def div(self):
        """Y / X"""
        self.last_x = self.__dessus
        if self.last_x == 0:
            self.empile(0)
        else:
            x2 = self.depile()
            y2 = self.depile()
            self.empile(y2 / x2)
        self.change = True

    def puiss(self):
        """Y puissance X"""
        self.last_x = self.__dessus
        x2 = self.depile()
        y2 = self.depile()
        if y2 == 0:
            self.empile(0)
        else:
            self.empile(y2 ** x2)
        self.change = True

    # Opérations algébriques sur la valeur du dessus

    def carre(self):
        """Carré de la valeur du dessus"""
        self.last_x = self.__dessus
        self.__dessus = self.__dessus ** 2
        self.change = True

    def racine(self):
        """Racine de la valeur du dessus"""
        self.last_x = self.__dessus
        if self.last_x < 0:
            self.__dessus = 0
        else:
            self.__dessus = self.__dessus ** .5
        self.change = True



    def opp(self):
        """Transforme la valeur du dessus en son opposé"""
        self.last_x = self.__dessus
        self.__dessus = -self.__dessus
        self.change = True

    def enter(self):
        """Action de la touche ENTER"""
        self.__reste.append(self.__dessus)
        self.__reste.pop(0)
        self.etat_enter = True

    def clear(self):
        """Efface x"""
        self.__dessus = 0

    def ac(self):
        """Clear la pile entière"""
        self.__dessus = 0
        self.__reste = [0, 0, 0]

    def lastx(self):
        """Empile la derniere valeur de x"""
        self.empile(self.last_x)

