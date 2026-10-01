import csv

tableau = []
with open('labyrinthe.csv', newline='') as labyrinthe:
    reader = csv.reader(labyrinthe)
    lignes = list(reader)
    for i in range(len(lignes)):
        tableau.append([])
        for j in range(len(lignes[i])):
            tableau[i].append(lignes[i][j])

print(tableau)
print(len(tableau))