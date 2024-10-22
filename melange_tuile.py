import random

def melange_tuile(liste_tuile,vide):
    random.shuffle(liste_tuile)
    
    liste_tuile_melangee = [[],[],[],[]]
    liste_nom_tuile_melangee = []
    for i in range(3):
        liste_tuile_melangee[0].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    for i in range(3,7):
        liste_tuile_melangee[1].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    for i in range(7,10):
        liste_tuile_melangee[2].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    
    liste_tuile_melangee[3].append(vide)
    liste_tuile_melangee[3].append(liste_tuile[10][0])
    liste_nom_tuile_melangee.append(liste_tuile[10][1])
    liste_tuile_melangee[3].append(liste_tuile[11][0])
    liste_nom_tuile_melangee.append(liste_tuile[11][1])
    liste_tuile_melangee[3].append(vide)
    
    return liste_tuile_melangee,liste_nom_tuile_melangee


def melange_tuile_14(liste_tuile,vide):
    random.shuffle(liste_tuile)
    
    liste_tuile_melangee = [[],[],[],[],[]]
    liste_nom_tuile_melangee = []
    
    
    liste_tuile_melangee[0].append(vide)
    for i in range(2):
        liste_tuile_melangee[0].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    liste_tuile_melangee[1].append(vide)
    for i in range(2,5):
        liste_tuile_melangee[1].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    for i in range(5,9):
        liste_tuile_melangee[2].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    liste_tuile_melangee[3].append(vide)
    for i in range(9,12):
        liste_tuile_melangee[3].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    liste_tuile_melangee[4].append(vide)
    for i in range(12,14):
        liste_tuile_melangee[4].append(liste_tuile[i][0])
        liste_nom_tuile_melangee.append(liste_tuile[i][1])
    
    
    return liste_tuile_melangee,liste_nom_tuile_melangee