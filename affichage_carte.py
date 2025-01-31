import matplotlib.pyplot as plt
import numpy as np
import math
import random
import os
from collections import Counter


def affichage_carte(liste_tuile, save_path=None):
    
    
    def trier_ressources_par_occurrences(ressources_generees):
        # Compter les occurrences de chaque ressource
        compteur_ressources = Counter([res[0] for res in ressources_generees])
        
        # Trier les ressources par le nombre d'occurrences (du plus fréquent au moins fréquent)
        ressources_triees = sorted(compteur_ressources.items(), key=lambda x: x[1], reverse=True)
        
        # Convertir chaque tuple en liste
        ressources_triees_listes = [[res[0], res[1]] for res in ressources_triees]
        
        return ressources_triees_listes
    
    def prox_1_case():
        liste_rec_prox_1 = []       
        for val in ressources_generees_tuile:
            if tuile[idy][idx] != 0:
                # detection des cases adjacentes
                if val[1] == idx-1 and val[2] == idy:
                    liste_rec_prox_1.append(val[0])
                if val[1] == idx and val[2] == idy-1:
                    liste_rec_prox_1.append(val[0])
                if val[1] == idx+1 and val[2] == idy-1 and idy % 2 == 1 or val[1] == idx-1 and val[2] == idy-1 and idy % 2 == 0:
                    liste_rec_prox_1.append(val[0])
        return liste_rec_prox_1
                    
    def prox_2_cases():
        liste_rec_prox_2 = []
        for val in ressources_generees_tuile:
            if tuile[idy][idx] != 0:
                # detection des cases a 2 cases de distance
                if val[1] == idx-2 and val[2] == idy:
                    liste_rec_prox_2.append(val[0])
                if val[1] == idx-2 and val[2] == idy-1 and idy % 2 == 0 or val[1] == idx-1 and val[2] == idy-1 and idy % 2 == 1:
                    liste_rec_prox_2.append(val[0])
                if val[1] == idx-1 and val[2] == idy-2: 
                    liste_rec_prox_2.append(val[0])
                if val[1] == idx and val[2] == idy-2:
                    liste_rec_prox_2.append(val[0])
                if val[1] == idx+1 and val[2] == idy-2:
                    liste_rec_prox_2.append(val[0])
                if val[1] == idx+1 and val[2] == idy-1 and idy % 2 == 0 or val[1] == idx+2 and val[2] == idy-1 and idy % 2 == 1:
                    liste_rec_prox_2.append(val[0])
        return liste_rec_prox_2    
        
                

    def generation_ressources(tuile,idx,idy):
        type_case = tuile[idy][idx]
        
        # liste ressources terrestre 
        liste_ressources = ["baleine","betail","charbon","crabe","fer","geyser","or","ruines","soie","village","merveille","cite_libre","vide"]
        ressources = ""
        couleur = ""
        forme = ""
        
        #liste des ressources proches
        ressources_proximite_1 = prox_1_case()
        ressources_proximite_2 = prox_2_cases()
        
        #gestion du bonus de proximité
        bonus_proximites_1=40
        bonus_proximites_2=10
        val_max_ressources = [25,160,250,330,460,560,660,710,830,945,1015,1125]
        
        #gestion des ressources en fonction des ressources proches et du nombre de ressources générées
        for val in ressources_proximite_1:
            a = 2
             
            if val == "baleine":
                if ressources_proximite_1.count("baleine") > a:
                    val_max_ressources[0] = 0
                else:
                    val_max_ressources[0] += 0
            elif val == "betail":
                if ressources_proximite_1.count("betail") > a:
                    val_max_ressources[1] = 0
                else:
                    val_max_ressources[1] += bonus_proximites_1
            elif val == "charbon":
                if ressources_proximite_1.count("charbon") > a:
                    val_max_ressources[2] = 0
                else:
                    val_max_ressources[2] += bonus_proximites_1
            elif val == "crabe":
                if ressources_proximite_1.count("crabe") > a:
                    val_max_ressources[3] = 0
                else:
                    val_max_ressources[3] += bonus_proximites_1
            elif val == "fer":
                if ressources_proximite_1.count("fer") > a:
                    val_max_ressources[4] = 0
                else:
                    val_max_ressources[4] += bonus_proximites_1
            elif val == "geyser":
                if ressources_proximite_1.count("geyser") > a:
                    val_max_ressources[5] = 0
                else:
                    val_max_ressources[5] += 0
            elif val == "or":
                if ressources_proximite_1.count("or") > a:
                    val_max_ressources[6] = 0
                else:
                    val_max_ressources[6] += bonus_proximites_1
            elif val == "ruines" or ressources_proximite_1.count("ruines") > 1:
                val_max_ressources[7] += 0
            elif val == "soie":
                if ressources_proximite_1.count("soie") > a:
                    val_max_ressources[8] = 0
                else:
                    val_max_ressources[8] += bonus_proximites_1
            elif val == "village" or ressources_proximite_1.count("village") > 1:
                val_max_ressources[9] = 0
            elif val == "merveille" or ressources_proximite_1.count("merveille") > 1:
                val_max_ressources[10] = 0
            elif val == "cite_libre" or ressources_proximite_1.count("cite_libre") > 1:
                val_max_ressources[11] = 0

            
        #gestion des ressources en fonction des ressources proches a 2 cases et du nombre de ressources générées
        for val2 in ressources_proximite_2:
            b = 2
            if val2 == "baleine":
                if ressources_proximite_2.count("baleine") > b:
                    val_max_ressources[0] = 0
                else:
                    val_max_ressources[0] += 0
            elif val2 == "betail":
                if ressources_proximite_2.count("betail") > b:
                    val_max_ressources[1] = 0
                else:
                    val_max_ressources[1] += bonus_proximites_2
            elif val2 == "charbon":
                if ressources_proximite_2.count("charbon") > b:
                    val_max_ressources[2] = 0
                else:
                    val_max_ressources[2] += bonus_proximites_2
            elif val2 == "crabe":
                if ressources_proximite_2.count("crabe") > b:
                    val_max_ressources[3] = 0
                else:
                    val_max_ressources[3] += bonus_proximites_2
            elif val2 == "fer":
                if ressources_proximite_2.count("fer") > b:
                    val_max_ressources[4] = 0
                else:
                    val_max_ressources[4] += bonus_proximites_2
            elif val2 == "geyser":
                if ressources_proximite_2.count("geyser") > b:
                    val_max_ressources[5] = 0
                else:
                    val_max_ressources[5] += bonus_proximites_2
            elif val2 == "or":
                if ressources_proximite_2.count("or") > b:
                    val_max_ressources[6] = 0
                else:
                    val_max_ressources[6] += bonus_proximites_2
            elif val2 == "ruines" or ressources_proximite_2.count("ruines") > 1:
                val_max_ressources[7] += 0
            elif val2 == "soie":
                if ressources_proximite_2.count("soie") > b:
                    val_max_ressources[8] = 0
                else:
                    val_max_ressources[8] += bonus_proximites_2
            elif val2 == "village" or ressources_proximite_2.count("village") > 1:
                val_max_ressources[9] = 0
            elif val2 == "merveille" or ressources_proximite_2.count("merveille") > 1:
                val_max_ressources[10] = 0
            elif val2 == "cite_libre" or ressources_proximite_2.count("cite_libre") > 1:
                val_max_ressources[11] = 0

        # génération d'une ressource en fonction du type de case
        if type_case != 0:
            while ressources == "":
                val_ressource = random.randint(0, 1200)
                
                if val_ressource > 0 and val_ressource <= val_max_ressources[0] :
                    if type_case in [0,6]:
                        ressources = liste_ressources[0]
                        couleur = "olivedrab"
                        forme = "cercle"
                elif val_ressource > 100 and val_ressource <= val_max_ressources[1] :
                    if type_case in [0,1]:
                        ressources = liste_ressources[1]
                        couleur = "yellowgreen"
                        forme = "cercle"
                elif val_ressource > 200 and val_ressource <= val_max_ressources[2] :
                    if type_case in [0,3,4]:
                        ressources = liste_ressources[2]
                        couleur = "black"
                        forme = "carre"
                elif val_ressource > 300 and val_ressource <= val_max_ressources[3]:
                    if type_case in [0,6]:
                        ressources = liste_ressources[3]
                        couleur = "aquamarine"
                        forme = "cercle"
                elif val_ressource > 400 and val_ressource <= val_max_ressources[4]:
                    if type_case in [0,3,4]:
                        ressources = liste_ressources[4]
                        couleur = "red"
                        forme = "carre"
                elif val_ressource > 500 and val_ressource <= val_max_ressources[5]:
                    if type_case in [0,3]:
                        ressources = liste_ressources[5]
                        couleur = "red"
                        forme = "cercle"
                elif val_ressource > 600 and val_ressource <= val_max_ressources[6]:
                    if type_case in [0,3,4]:
                        ressources = liste_ressources[6]
                        couleur = "gold"
                        forme = "carre"
                elif val_ressource > 700 and val_ressource <= val_max_ressources[7]:
                    if type_case in [1,2,3,5,6]:
                        ressources = liste_ressources[7]
                        couleur = "black"
                        forme = "etoile"
                elif val_ressource > 800 and val_ressource <= val_max_ressources[8]:
                    if type_case in [0,2]:
                        ressources = liste_ressources[8]
                        couleur = "violet"
                        forme = "cercle"
                elif val_ressource > 900 and val_ressource <= val_max_ressources[9]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[9]
                        couleur = "red"
                        forme = "etoile"
                elif val_ressource > 1000 and val_ressource <= val_max_ressources[10]:
                    if type_case in [1,2,3,4,6]:
                        ressources = liste_ressources[10]
                        couleur = "gold"
                        forme = "etoile"
                elif val_ressource > 1100 and val_ressource <= val_max_ressources[11]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[11]
                        couleur = "snow"
                        forme = "etoile"
                else:
                    ressources = liste_ressources[12]

            

            if ressources != "vide":    
                ressources_generees_tuile.append([ressources,idx,idy])

        return ressources,couleur,forme
    
    def transferer_listes(liste_1, liste_2):
        while len(liste_1) > 0:
            liste_2.append(liste_1.pop())
        liste_1.clear()

    # Paramètres de l'hexagone
    taille_hexagone = 1.0
    distance_x_entre_hexagones = (math.sqrt(3)) * taille_hexagone
    distance_y_entre_hexagones = 3/2 * taille_hexagone

    # Coordonnées des sommets d'un hexagone régulier
    x_hexagone = np.array([np.cos(np.pi/3 * i + np.pi/6) for i in range(6)])
    y_hexagone = np.array([np.sin(np.pi/3 * i + np.pi/6) for i in range(6)])

    # Création de la figure
    fig, ax = plt.subplots(facecolor='black')


    #variable globale pour stocker les ressources générées
    global ressources_generees_tuile
    global ressources_generees
    ressources_generees_tuile = []
    ressources_generees = []

    # Affichage des 37 hexagones
    for idtx,val in enumerate(liste_tuile):  # id colonne carte
        for idty,tuile in enumerate(val): # id ligne carte
            for idy,i in enumerate(tuile): # id ligne tuile
                for idx,j in enumerate(i): # id colonne tuile
                
                    x_offset = idx * distance_x_entre_hexagones if idy % 2 == 0 else idx * distance_x_entre_hexagones + distance_x_entre_hexagones/2
                    y_offset = -idy * distance_y_entre_hexagones
                    
                    # affichage des hexagones pour chaque colonne idtx et chaque ligne idty
                    if idtx == 0:
                        x_coords = (x_hexagone + x_offset)- 0.87*idty
                        y_coords = (y_hexagone + y_offset)+ math.sqrt(3)*6.2*idty  
                    elif idtx == 1:
                        x_coords = (x_hexagone + x_offset)+ 9.7 *idtx - 0.87*idty
                        y_coords = (y_hexagone + y_offset)+ math.sqrt(3)*6.2*idty - math.sqrt(3)*7/2 + math.sqrt(3)/1.1*idtx
                    elif idtx == 2:
                        x_coords = (x_hexagone + x_offset)+ 9.3 *idtx - 0.87*idty
                        y_coords = (y_hexagone + y_offset)+ math.sqrt(3)*6.2*idty + math.sqrt(3)/2.3*idtx
                    elif idtx == 3:
                        x_coords = (x_hexagone + x_offset)+ 9.45 *idtx - 0.87*idty
                        y_coords = (y_hexagone + y_offset)+ math.sqrt(3)*6.2*idty - math.sqrt(3)*7/2 + math.sqrt(3)/1.7*idtx
                    
                    #remplissage des couleurs en fonction du type de case
                    if j == 1:
                        ax.fill(x_coords, y_coords, edgecolor='lime', facecolor='lime')
                    elif j == 2:
                        ax.fill(x_coords, y_coords, edgecolor='darkgreen', facecolor='darkgreen')
                    elif j == 3:
                        ax.fill(x_coords, y_coords, edgecolor='yellow', facecolor='yellow')
                    elif j == 4:
                        ax.fill(x_coords, y_coords, edgecolor='lightslategrey', facecolor='lightslategrey')
                    elif j == 5:
                        ax.fill(x_coords, y_coords, edgecolor='sienna', facecolor='sienna')
                    elif j == 6:
                        ax.fill(x_coords, y_coords, edgecolor='navy', facecolor='navy')
                    elif j == 7:
                        ax.fill(x_coords, y_coords, edgecolor='red', facecolor='red')
                        
                    ressources,couleur,forme = generation_ressources(tuile,idx,idy)
                        
                    # Ajout d'un cercle au milieu de l'hexagone
                    if j != 0 and ressources != "vide":
                        center_x = np.mean(x_coords)
                        center_y = np.mean(y_coords)
                        if forme == "cercle":
                            ax.add_patch(plt.Circle((center_x, center_y), 0.2, color=couleur, fill=True, zorder=10))
                        elif forme == "triangle":
                            ax.add_patch(plt.Polygon([[center_x, center_y + 0.2], [center_x - 0.2, center_y - 0.2], [center_x + 0.2, center_y - 0.2]], color=couleur, fill=True, zorder=10))
                        elif forme == "carre":
                            ax.add_patch(plt.Polygon([[center_x - 0.2, center_y + 0.2], [center_x - 0.2, center_y - 0.2], [center_x + 0.2, center_y - 0.2], [center_x + 0.2, center_y + 0.2]], color=couleur, fill=True, zorder=10))
                        elif forme == "hexagone":
                            ax.add_patch(plt.Polygon([[center_x, center_y + 0.2], [center_x - 0.2, center_y + 0.1], [center_x - 0.2, center_y - 0.1], [center_x, center_y - 0.2], [center_x + 0.2, center_y - 0.1], [center_x + 0.2, center_y + 0.1]], color=couleur, fill=True, zorder=10))
                        elif forme == "etoile":
                            points = [[center_x, center_y + 0.2],[center_x + 0.05, center_y + 0.1],[center_x + 0.2, center_y + 0.1],[center_x + 0.1, center_y],[center_x + 0.1, center_y - 0.2],[center_x, center_y - 0.1],[center_x - 0.1, center_y - 0.2],[center_x - 0.1, center_y],[center_x - 0.2, center_y + 0.1],[center_x - 0.05, center_y + 0.1]]
                            ax.add_patch(plt.Polygon( points, color=couleur, fill=True, zorder=10))
            transferer_listes(ressources_generees_tuile, ressources_generees) # remplissage de la liste globale des ressources générées et vidage de la liste de la tuile courante
    ressources_triees = trier_ressources_par_occurrences(ressources_generees) # tri des ressources générées


    # Configuration de l'axe
    ax.set_aspect('equal')
    ax.axis('off')  # Masque les axes
    
    # Sauvegarde de la figure
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, 'carte.pdf')
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1)
        print(f'Figure saved at {file_path}')

    # Affichage de la figure
    plt.show()
    
    return ressources_triees