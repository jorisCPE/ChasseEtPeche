from affichage_tuile import *
from affichage_carte import *
from melange_tuile import *
from rotation_tuile import *

def generer_carte():
    # liste tuile test (liste de 7*7 composée de 0 et 1)
    
    ######  12 tuiles d'origine ######
    liste_tuile_0 = [[[0, 0, 4, 1, 6, 2, 0],
                    [0, 1, 1, 4, 5, 4, 0],
                    [0, 5, 4, 5, 7, 5, 1],
                    [1, 1, 2, 4, 4, 2, 1],
                    [0, 1, 1, 1, 2, 1, 1],
                    [0, 3, 2, 1, 2, 2, 0],
                    [0, 0, 1, 4, 1, 2, 0],],"tuile_0"]
                    
                    
    tuile_0 = rotation_tuile(liste_tuile_0[0],liste_tuile_0[1])

    liste_tuile_1 = [[[0, 0, 2, 4, 1, 4, 0],
                    [0, 2, 2, 5, 6, 5, 0],
                    [0, 6, 5, 5, 6, 6, 3],
                    [3, 6, 6, 5, 6, 3, 2],
                    [0, 4, 5, 6, 6, 5, 3],
                    [0, 1, 5, 6, 6, 3, 0],
                    [0, 0, 3, 6, 4, 5, 0],],"tuile_1"]
                    

    tuile_1 = rotation_tuile(liste_tuile_1[0],liste_tuile_1[1])

    liste_tuile_2 = [[[0, 0, 2, 1, 1, 2, 0],
                    [0, 1, 5, 3, 2, 1, 0],
                    [0, 1, 1, 6, 5, 2, 4],
                    [2, 2, 3, 2, 4, 1, 2],
                    [0, 2, 1, 4, 1, 1, 2],
                    [0, 3, 3, 1, 2, 1, 0],
                    [0, 0, 3, 1, 4, 2, 0],],"tuile_2"]
                    

    tuile_2 = rotation_tuile(liste_tuile_2[0],liste_tuile_2[1])

    liste_tuile_3 = [[[0, 0, 1, 1, 1, 1, 0],
                    [0, 2, 4, 1, 1, 1, 0],
                    [0, 3, 5, 1, 1, 1, 2],
                    [2, 1, 2, 2, 1, 4, 2],
                    [0, 4, 5, 1, 5, 5, 1],
                    [0, 6, 6, 5, 5, 1, 0],
                    [0, 0, 6, 6, 2, 2, 0],],"tuile_3"]
                    

    tuile_3 = rotation_tuile(liste_tuile_3[0],liste_tuile_3[1])

    liste_tuile_4 = [[[0, 0, 7, 6, 2, 1, 0],
                    [0, 2, 3, 4, 2, 5, 0],
                    [0, 2, 3, 4, 6, 4, 7],
                    [1, 5, 7, 6, 6, 5, 1],
                    [0, 5, 3, 5, 4, 6, 2],
                    [0, 1, 2, 5, 2, 4, 0],
                    [0, 0, 4, 1, 3, 1, 0],],"tuile_4"]
                    

    tuile_4 = rotation_tuile(liste_tuile_4[0],liste_tuile_4[1])

    liste_tuile_5 = [[[0, 0, 4, 1, 1, 2, 0],
                    [0, 1, 5, 6, 1, 2, 0],
                    [0, 2, 5, 6, 6, 1, 4],
                    [2, 2, 1, 5, 1, 2, 2],
                    [0, 1, 4, 5, 1, 2, 1],
                    [0, 2, 5, 6, 6, 2, 0],
                    [0, 0, 1, 6, 6, 6, 0],],"tuile_5"]
                    

    tuile_5 = rotation_tuile(liste_tuile_5[0],liste_tuile_5[1])

    liste_tuile_6 = [[[0, 0, 2, 6, 2, 5, 0],
                    [0, 4, 5, 6, 1, 5, 0],
                    [0, 1, 1, 1, 1, 2, 1],
                    [2, 4, 3, 4, 2, 2, 1],
                    [0, 2, 2, 1, 1, 4, 2],
                    [0, 2, 7, 3, 3, 1, 0],
                    [0, 0, 2, 3, 3, 1, 0],],"tuile_6"]
                    

    tuile_6 = rotation_tuile(liste_tuile_6[0],liste_tuile_6[1])

    liste_tuile_7 = [[[0, 0, 2, 1, 6, 4, 0],
                    [0, 1, 5, 6, 5, 1, 0],
                    [0, 2, 6, 6, 6, 6, 1],
                    [2, 1, 6, 1, 2, 6, 6],
                    [0, 1, 2, 6, 6, 6, 6],
                    [0, 4, 6, 5, 6, 5, 0],
                    [0, 0, 1, 2, 6, 2, 0],],"tuile_7"]
                    

    tuile_7 = rotation_tuile(liste_tuile_7[0],liste_tuile_7[1])

    liste_tuile_8 = [[[0, 0, 4, 1, 3, 2, 0],
                    [0, 5, 5, 5, 1, 4, 0],
                    [0, 1, 2, 6, 2, 5, 5],
                    [2, 6, 5, 1, 1, 1, 2],
                    [0, 5, 5, 1, 5, 6, 1],
                    [0, 4, 5, 2, 5, 5, 0],
                    [0, 0, 1, 2, 2, 4, 0],],"tuile_8"]
                    

    tuile_8 = rotation_tuile(liste_tuile_8[0],liste_tuile_8[1])

    liste_tuile_9 = [[[0, 0, 4, 5, 5, 4, 0],
                    [0, 4, 6, 2, 2, 5, 0],
                    [0, 2, 2, 5, 2, 2, 5],
                    [4, 2, 5, 7, 2, 4, 2],
                    [0, 2, 2, 1, 1, 2, 2],
                    [0, 2, 4, 2, 2, 1, 0],
                    [0, 0, 2, 5, 2, 2, 0],],"tuile_9"]
                    

    tuile_9 = rotation_tuile(liste_tuile_9[0],liste_tuile_9[1])

    liste_tuile_10 = [[[0, 0, 2, 1, 3, 3, 0],
                    [0, 1, 1, 4, 3, 4, 0],
                    [0, 2, 2, 3, 3, 2, 1],
                    [1, 2, 1, 1, 1, 4, 2],
                    [0, 1, 5, 6, 5, 2, 2],
                    [0, 1, 6, 6, 6, 1, 0],
                    [0, 0, 6, 6, 5, 5, 0],],"tuile_10"]
                    

    tuile_10 = rotation_tuile(liste_tuile_10[0],liste_tuile_10[1])

    liste_tuile_11 = [[[0, 0, 4, 1, 1, 6, 0],
                    [0, 1, 1, 5, 6, 6, 0],
                    [0, 2, 2, 2, 2, 1, 3],
                    [1, 2, 4, 2, 7, 3, 1],
                    [0, 1, 2, 2, 2, 4, 3],
                    [0, 1, 2, 1, 1, 1, 0],
                    [0, 0, 2, 1, 4, 3, 0],],"tuile_11"]
                    

    tuile_11 = rotation_tuile(liste_tuile_11[0],liste_tuile_11[1])
    
    ###### 12 nouvelles tuiles ######
    
    liste_tuile_0_2 = [[[0, 0, 2, 5, 6, 3, 0],
                    [0, 2, 2, 5, 6, 3, 0],
                    [0, 2, 1, 1, 2, 6, 3],
                    [5, 5, 1, 6, 6, 3, 3],
                    [0, 1, 5, 6, 3, 3, 3],
                    [0, 5, 6, 3, 3, 3, 0],
                    [0, 0, 5, 6, 3, 3, 0],],"tuile_0_2"]
                    
                    
    tuile_0_2 = rotation_tuile(liste_tuile_0_2[0],liste_tuile_0_2[1])

    liste_tuile_1_2 = [[[0, 0, 1, 1, 4, 6, 0],
                    [0, 2, 4, 4, 6, 6, 0],
                    [0, 1, 4, 1, 6, 6, 6],
                    [4, 1, 1, 6, 1, 6, 6],
                    [0, 4, 2, 1, 1, 6, 6],
                    [0, 5, 1, 6, 6, 6, 0],
                    [0, 0, 2, 5, 5, 6, 0],],"tuile_1_2"]
                    

    tuile_1_2 = rotation_tuile(liste_tuile_1_2[0],liste_tuile_1_2[1])

    liste_tuile_2_2 = [[[0, 0, 2, 1, 4, 2, 0],
                    [0, 1, 4, 4, 1, 2, 0],
                    [0, 4, 4, 1, 1, 1, 6],
                    [4, 1, 1, 1, 1, 2, 1],
                    [0, 1, 4, 2, 1, 1, 1],
                    [0, 2, 4, 1, 1, 2, 0],
                    [0, 0, 4, 1, 2, 6, 0],],"tuile_2_2"]
                    

    tuile_2_2 = rotation_tuile(liste_tuile_2_2[0],liste_tuile_2_2[1])

    liste_tuile_3_2 = [[[0, 0, 2, 4, 1, 2, 0],
                    [0, 1, 7, 1, 1, 2, 0],
                    [0, 4, 4, 1, 1, 1, 6],
                    [4, 1, 1, 1, 1, 2, 1],
                    [0, 1, 4, 2, 1, 1, 1],
                    [0, 2, 4, 1, 2, 2, 0],
                    [0, 0, 4, 1, 2, 6, 0],],"tuile_3_2"]
                    

    tuile_3_2 = rotation_tuile(liste_tuile_3_2[0],liste_tuile_3_2[1])

    liste_tuile_4_2 = [[[0, 0, 6, 6, 3, 3, 0],
                    [0, 6, 3, 3, 3, 3, 0],
                    [0, 6, 6, 3, 3, 3, 5],
                    [6, 6, 3, 3, 3, 5, 2],
                    [0, 6, 6, 3, 4, 4, 2],
                    [0, 6, 6, 5, 2, 4, 0],
                    [0, 0, 6, 6, 6, 1, 0],],"tuile_4_2"]
                    

    tuile_4_2 = rotation_tuile(liste_tuile_4_2[0],liste_tuile_4_2[1])

    liste_tuile_5_2 = [[[0, 0, 5, 5, 2, 1, 0],
                    [0, 4, 6, 6, 6, 6, 0],
                    [0, 4, 4, 4, 6, 6, 6],
                    [4, 6, 6, 6, 6, 6, 1],
                    [0, 1, 6, 6, 6, 5, 2],
                    [0, 5, 6, 6, 6, 5, 0],
                    [0, 0, 2, 5, 5, 1, 0],],"tuile_5_2"]
                    

    tuile_5_2 = rotation_tuile(liste_tuile_5_2[0],liste_tuile_5_2[1])

    liste_tuile_6_2 = [[[0, 0, 6, 6, 2, 1, 0],
                    [0, 6, 6, 5, 2, 6, 0],
                    [0, 6, 6, 6, 1, 2, 2],
                    [6, 6, 6, 1, 7, 6, 6],
                    [0, 6, 2, 2, 1, 1, 6],
                    [0, 5, 2, 5, 5, 6, 0],
                    [0, 0, 5, 1, 5, 5, 0],],"tuile_6_2"]
                    

    tuile_6_2 = rotation_tuile(liste_tuile_6_2[0],liste_tuile_6_2[1])

    liste_tuile_7_2 = [[[0, 0, 3, 3, 1, 2, 0],
                    [0, 6, 3, 1, 3, 1, 0],
                    [0, 6, 3, 6, 6, 6, 2],
                    [6, 6, 6, 6, 6, 6, 5],
                    [0, 6, 6, 1, 7, 6, 5],
                    [0, 6, 1, 2, 6, 6, 0],
                    [0, 0, 6, 6, 6, 6, 0],],"tuile_7_2"]
                    

    tuile_7_2 = rotation_tuile(liste_tuile_7_2[0],liste_tuile_7_2[1])

    liste_tuile_8_2 = [[[0, 0, 5, 4, 1, 1, 0],
                    [0, 1, 4, 2, 1, 4, 0],
                    [0, 5, 5, 4, 1, 4, 2],
                    [2, 1, 1, 1, 6, 4, 1],
                    [0, 1, 4, 1, 2, 4, 6],
                    [0, 4, 2, 1, 1, 4, 0],
                    [0, 0, 1, 2, 2, 1, 0],],"tuile_8_2"]
                    

    tuile_8_2 = rotation_tuile(liste_tuile_8_2[0],liste_tuile_8_2[1])

    liste_tuile_9_2 = [[[0, 0, 1, 4, 1, 3, 0],
                    [0, 4, 4, 1, 7, 4, 0],
                    [0, 2, 2, 1, 1, 4, 6],
                    [1, 1, 1, 4, 2, 5, 6],
                    [0, 7, 4, 1, 1, 1, 6],
                    [0, 2, 2, 4, 2, 5, 0],
                    [0, 0, 2, 4, 5, 6, 0],],"tuile_9_2"]
                    

    tuile_9_2 = rotation_tuile(liste_tuile_9_2[0],liste_tuile_9_2[1])

    liste_tuile_10_2 = [[[0, 0, 4, 1, 1, 1, 0],
                    [0, 1, 4, 4, 1, 4, 0],
                    [0, 5, 1, 2, 1, 1, 2],
                    [5, 2, 1, 1, 1, 1, 2],
                    [0, 2, 5, 1, 1, 1, 1],
                    [0, 6, 1, 2, 1, 1, 0],
                    [0, 0, 6, 5, 2, 1, 0],],"tuile_10_2"]
                    

    tuile_10_2 = rotation_tuile(liste_tuile_10_2[0],liste_tuile_10_2[1])

    liste_tuile_11_2 = [[[0, 0, 2, 2, 1, 2, 0],
                    [0, 2, 5, 2, 5, 2, 0],
                    [0, 1, 5, 2, 2, 5, 1],
                    [1, 2, 5, 5, 2, 5, 2],
                    [0, 2, 5, 2, 5, 1, 1],
                    [0, 6, 2, 5, 2, 5, 0],
                    [0, 0, 6, 6, 2, 5, 0],],"tuile_11_2"]
                    

    tuile_11_2 = rotation_tuile(liste_tuile_11_2[0],liste_tuile_11_2[1])
    
    ###### tuiles vide ######

    vide =      [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],]




    liste_tuile = [tuile_0, tuile_1, tuile_2, tuile_3, tuile_4, tuile_5, tuile_6, tuile_7, tuile_8, tuile_9, tuile_10, tuile_11]
    liste_tuile_2 = [tuile_0_2, tuile_1_2, tuile_2_2, tuile_3_2, tuile_4_2, tuile_5_2, tuile_6_2, tuile_7_2, tuile_8_2, tuile_9_2, tuile_10_2, tuile_11_2]

    liste_tuile_melangee, liste_nom_tuile_melangee = melange_tuile(liste_tuile, vide)
    liste_tuile_melangee_2, liste_nom_tuile_melangee_2 = melange_tuile(liste_tuile_2, vide)

    nb_lignes = 3
    nb_colonnes = 3

    liste_ressources_tuile = affichage_carte(liste_tuile_melangee , 'carte')
    
    return liste_nom_tuile_melangee, liste_ressources_tuile

    #affichage_tuile(tuile_1,nb_lignes,nb_colonnes)
