class Model:

    def __init__(self):
        self.__reste = [0, 0, 0]  # initialisation du reste de la pile [T,Z,Y]
        self.__dessus = 0       # initialisation du dessus de la pile X

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

    def x(self):
        return self.__dessus

    def yzt(self):
        return self.__reste

    # Opérations algébriques élémentaires

    def plus(self):
        """Addition des valeurs X et Y"""
        self.empile(self.depile() + self.depile())

    def moins(self):
        """Soustraction des valeurs X et Y"""
        self.empile(self.depile() - self.depile())

    def mult(self):
        """Multiplication des valeurs X et Y"""
        self.empile(self.depile() * self.depile())

    def div(self):
        """Division des valeurs X et Y"""
        self.empile(self.depile() / self.depile())

    def puiss(self):
        """X puissance Y"""
        self.empile(self.depile() ** self.depile())

    # Opérations algébriques sur la valeur du dessus

    def carre(self):
        """Carré de la valeur du dessus"""
        self.__dessus = self.__dessus ** 2

    def racine(self):
        """Racine de la valeur du dessus"""
        self.__dessus = self.__dessus ** .5

    def opp(self):
        """Transforme la valeur du dessus en son opposé"""
        self.__dessus = -self.__dessus


v = Model()
v.empile(2)
v.empile(4)
v.empile(3)
v.empile(5)
print(v.x(), v.yzt())

v.mult()
print(v.x(),v.yzt())

v.plus()
print(v.x(),v.yzt())

v.puiss()
print(v.x(),v.yzt())
