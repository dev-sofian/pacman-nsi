import pyxel
import csv
from constantes import *
from Fantome import Fantome
from Pacgomme import Pacgomme
from Pacman import Pacman

class Moteur:
    def __init__(self):
        # initialisations des objets du jeu
        self.labyrinthe = self.initialiser_labyrinthe()
        self.pacman = Pacman(24, 1)
        self.un_fantome = Fantome(1, 1, 8)

        # initialisation de pyxel
        pyxel.init(TAILLE*TAILLE_CEL, TAILLE*TAILLE_CEL, fps=5)
        pyxel.load("ressources.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """
        met à jour à chaque cycle de pyxel
        """
        self.update_fantomes()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.update_pacman(-1, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.update_pacman(1, 0)
        elif pyxel.btn(pyxel.KEY_UP):
            self.update_pacman(0, -1)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.update_pacman(0, 1)


    def draw(self):
        """
        dessine à chaque cycle de pyxel
        """
        pyxel.cls(0)
        self.dessiner_labyrinthe()
        self.dessiner_fantome(self.un_fantome)
        self.dessiner_pacman

    def initialiser_labyrinthe(self) -> list:
        """
        Crée un labyrinthe de test
        Doit normalement s'appuyer sur le fichier csv

        Renvoie:
            list: tableau représentatif du labyrinthe
        """
        tableau = []
        with open('labyrinthe.csv', newline='') as labyrinthe:
            reader = csv.reader(labyrinthe)
            lignes = list(reader)
            for i in range(len(lignes)):
                tableau.append([])
                for j in range(len(lignes[i])):
                    if lignes[i][j] != "0":
                        tableau[i].append(Pacgomme())
                    else:
                        tableau[i].append(int(lignes[i][j]))

        return tableau

    def update_fantomes(self) -> None:
        """
        bouge les fantômes
        """
        self.un_fantome.choisir_dpct(self.labyrinthe)

    def update_pacman(self, posx, posy):
        self.pacman.set_col(posx)
        self.pacman.set_lig(posy)

    def dessiner_labyrinthe(self):
        for l in range(TAILLE):
            for c in range(TAILLE):
                if isinstance(self.labyrinthe[l][c], Pacgomme):
                    self.dessiner_pacgomme(c, l)
                elif self.labyrinthe[l][c] == 0:
                    self.dessiner_mur(c, l)

    def dessiner_mur(self, c: int, l: int):
        """
        dessine un mur bleu

        Params:
            c (int): colonne
            l (int): ligne
        """
        pyxel.rect(c*TAILLE_CEL, l*TAILLE_CEL, TAILLE_CEL, TAILLE_CEL, 5)

    def dessiner_fantome(self, fant: Fantome) -> None:
        """
        dessine un fantôme

        Paramètres:
            fant (Fantome): instance du fantôme dessiné
        """    
        c = fant.get_col()
        l = fant.get_lig()
        pyxel.blt(c*TAILLE_CEL, l*TAILLE_CEL, 0,
                  TAILLE_CEL, 0, TAILLE_CEL, TAILLE_CEL, 0)

    def dessiner_pacman(self, pac: Pacman) -> None:
        c = pac.get_col()
        l = pac.get_lig()
        pyxel.blt(c*TAILLE_CEL, l*TAILLE_CEL, 0,
                  TAILLE_CEL, 0, TAILLE_CEL, TAILLE_CEL, 0)

    def dessiner_pacgomme(self, c: int, l: int):
        pyxel.circ((c+0.5)*TAILLE_CEL, (l+0.5) *
                   TAILLE_CEL, TAILLE_CEL//5, 10)


# programme principal
Moteur()
