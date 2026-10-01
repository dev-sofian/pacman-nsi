from constantes import *
from random import randint, choice


class Fantome:
    def __init__(self, c: int, l: int, coul: int):
        self.couleur = coul
        self.col = c
        self.lig = l
        self.state = "None"

    def get_col(self) -> int:
        return self.col

    def get_lig(self) -> int:
        return self.lig

    def set_col(self, d: int) -> None:
        self.col = self.col + d

    def set_lig(self, d: int) -> None:
        self.lig = self.lig + d

    def choisir_dpct(self, tab: list) -> None:
        """
        change les coordonnées du fantôme
        !!ne gère pas le retour en arrière!!

        Paramètres:
            tab (list): le labyrinthe
        """
        delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
                # récupère les positions de déplacements possibles
        possibles = []
        for dx, dy in delta:
            x, y = self.col + dx, self.lig + dy
            if tab[y][x] != 0:
                possibles.append((x, y))
        # choisit le déplacement
        choix = 0
        if len(possibles) > 1:
            choix = randint(0, len(possibles)-1)
        self.col = possibles[choix][0]
        self.lig = possibles[choix][1]