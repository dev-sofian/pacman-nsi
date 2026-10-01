import pyxel

class Pacman:
    def __init__(self, x, y):
        self.col = x
        self.lig = y
        self.vies = 3
        self.score = 0
    def get_col(self) -> int:
        return self.col
    
    def get_lig(self) -> int:
        return self.lig
    
    def set_col(self, d: int) -> None:
        self.col = self.col + d
    
    def set_lig(self, d: int) -> None:
        self.lig = self.lig + d
        