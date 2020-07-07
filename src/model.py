class Model:

    def __init__(self):
        self.__reste = [0, 0, 0]        # initialisation du reste de la pile [T,Z,Y]
        self.__dessus = 0               # initialisation du dessus de la pile X
        self.change = False              # si il y a eu opération sur le nombre x, n'empile pas 0

    def empile(self, val):
        """Empile val sur la pile"""
        self.__reste.append(self.__dessus)
        self.__reste.pop(0)
        self.__dessus = val

    def depile(self):
        """Retourne la valeur du dessus de la pile, et la retire de la pile"""
        r = self.__dessus
        self.__dessus = self.__reste[-1]
        self.__reste.insert(0, 0)
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
        """Addition des valeurs X et Y"""
        self.empile(self.depile() + self.depile())
        self.change = True

    def moins(self):
        """Soustraction des valeurs X et Y"""
        self.empile(self.depile() - self.depile())
        self.change = True

    def mult(self):
        """Multiplication des valeurs X et Y"""
        self.empile(self.depile() * self.depile())
        self.change = True

    def div(self):
        """Division des valeurs X et Y"""
        self.empile(self.depile() / self.depile())
        self.change = True

    def puiss(self):
        """X puissance Y"""
        self.empile(self.depile() ** self.depile())
        self.change = True

    # Opérations algébriques sur la valeur du dessus

    def carre(self):
        """Carré de la valeur du dessus"""
        self.__dessus = self.__dessus ** 2
        self.change = True

    def racine(self):
        """Racine de la valeur du dessus"""
        self.__dessus = self.__dessus ** .5
        self.change = True

    def opp(self):
        """Transforme la valeur du dessus en son opposé"""
        self.__dessus = -self.__dessus
        self.change = True

    def enter(self):
        """Action de la touche ENTER"""
        self.__reste.append(self.__dessus)
        self.__dessus = 0
        self.__reste.pop(0)

    def clear(self):
        """Efface valeur du dessus"""
        self.__dessus = 0

    def ac(self):
        """Clear la pile entière"""
        self.__dessus = 0
        self.__reste = [0, 0, 0]


"""
v = Model()

v.empile(2)
v.empile(4)
v.empile(3)
v.empile(5)


v.clear()
print(v.x(), v.yzt())
v.enter()
print(v.x(), v.yzt())
v.ac()
print(v.x(), v.yzt()) """