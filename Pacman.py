import pyxel
from math import cos, sin, radians

class Pacman:
    def __init__(self, x, y, coul):
        self.col = x
        self.lig = y
        self.vies = 3
        self.score = 0
        self.couleur = coul
        self.dir = 0

    def get_col(self) -> int:
        return self.col
    
    def get_lig(self) -> int:
        return self.lig

    def get_coul(self) -> int:
        return self.couleur
    
    def set_col(self, d: int) -> None:
        self.col = self.col + d
    
    def set_lig(self, d: int) -> None:
        self.lig = self.lig + d

    def choisir_dpct(self, tab):

        delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
                # récupère les positions de déplacements possibles
        possibles = []
        for dx, dy, in delta:
            x, y = self.col + dx, self.lig + dy
            if tab[y][x] != 0:
                possibles.append((x, y))

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dir = 0
            print("droite")
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.dir = 180
            print("gauche")
        elif pyxel.btn(pyxel.KEY_UP):
            self.dir = -90
            print("haut")
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.dir = 90
            print("bas")

        rad = radians(self.dir)

        x, y = int(cos(rad) + self.col), int(sin(rad) + self.lig)

        print((x, y), possibles)

        if (x, y) in possibles:
            print("oui")
            self.col = x
            self.lig = y