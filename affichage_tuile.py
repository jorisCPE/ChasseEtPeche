import matplotlib.pyplot as plt
import numpy as np
import math
import random


def affichage_tuile(tuile_test,nb_lignes,nb_colonnes):
    def case_proximite(tuile,idx,idy):
        # liste les cases a deux case de la case idx,idy
        liste_rec_prox = []
        for val in ressources_generees:
            if tuile[idy][idx] != 0:
                # detection des cases adjacentes
                if val[1] == idx-1 and val[2] == idy:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx and val[2] == idy-1:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx+1 and val[2] == idy-1 and idy % 2 == 1 or val[1] == idx-1 and val[2] == idy-1 and idy % 2 == 0:
                    liste_rec_prox.append([val[0],idx,idy])
                    
                # detection des cases a 2 cases de distance
                if val[1] == idx-2 and val[2] == idy:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx-2 and val[2] == idy-1 and idy % 2 == 0 or val[1] == idx-1 and val[2] == idy-1 and idy % 2 == 1:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx-1 and val[2] == idy-2: 
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx and val[2] == idy-2:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx+1 and val[2] == idy-2:
                    liste_rec_prox.append([val[0],idx,idy])
                if val[1] == idx+1 and val[2] == idy-1 and idy % 2 == 0 or val[1] == idx+2 and val[2] == idy-1 and idy % 2 == 1:
                    liste_rec_prox.append([val[0],idx,idy])
                
        
        return liste_rec_prox
                

    def generation_ressources(tuile,idx,idy):
        type_case = tuile[idy][idx]
        
        # liste ressources terrestre 
        liste_ressources = ["baleine","betail","charbon","chevaux","crabe","fer","gemme","geyser","or","ruines","soie","village","merveille","cite_libre","vide"]

        
        ressources = ""
        couleur = ""
        forme = ""
        
        #liste des ressources proches
        ressources_proximite = case_proximite(tuile,idx,idy)
        print(ressources_proximite)
        
        #gestion du bonus de proximité
        bonus_proximites=50
        val_max_ressources = [30,150,250,350,450,540,640,750,850,950,1050,1150,1250,1350]
        
        for val in ressources_proximite:
            if val[0] == "baleine":
                val_max_ressources[0] += bonus_proximites
            elif val[0] == "betail":
                val_max_ressources[1] += bonus_proximites
            elif val[0] == "charbon":
                val_max_ressources[2] += bonus_proximites
            elif val[0] == "chevaux":
                val_max_ressources[3] += bonus_proximites
            elif val[0] == "crabe":
                val_max_ressources[4] += bonus_proximites
            elif val[0] == "fer":
                val_max_ressources[5] += bonus_proximites
            elif val[0] == "gemme":
                val_max_ressources[6] += bonus_proximites
            elif val[0] == "geyser":
                val_max_ressources[7] += bonus_proximites
            elif val[0] == "or":
                val_max_ressources[8] += bonus_proximites
            elif val[0] == "ruines":
                val_max_ressources[9] += bonus_proximites
            elif val[0] == "soie":
                val_max_ressources[10] += bonus_proximites
            elif val[0] == "village" or ressources_generees.count("village") > 2:
                val_max_ressources[11] = 0
            elif val[0] == "merveille" or ressources_generees.count("merveille") > 2:
                val_max_ressources[12] = 0
            elif val[0] == "cite_libre" or ressources_generees.count("cite_libre") > 2:
                val_max_ressources[13] = 0
            elif val[0] == "vide":
                val_max_ressources[14] += bonus_proximites
                
        print(val_max_ressources)
        
        # génération d'une ressource en fonction du type de case
        if type_case != 0:
            while ressources == "":
                val_ressource = random.randint(0, 1400)
                
                if val_ressource > 0 and val_ressource <= val_max_ressources[0] :
                    if type_case in [6]:
                        ressources = liste_ressources[0]
                        couleur = "lightblue"
                        forme = "cercle"
                elif val_ressource > 100 and val_ressource <= val_max_ressources[1] :
                    if type_case in [1]:
                        ressources = liste_ressources[1]
                        couleur = "hotpink"
                        forme = "cercle"
                elif val_ressource > 200 and val_ressource <= val_max_ressources[2] :
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[2]
                        couleur = "black"
                        forme = "cercle"
                elif val_ressource > 300 and val_ressource <= val_max_ressources[3]:
                    if type_case in [1]:
                        ressources = liste_ressources[3]
                        couleur = "saddlebrown"
                        forme = "cercle"
                elif val_ressource > 400 and val_ressource <= val_max_ressources[4]:
                    if type_case in [6]:
                        ressources = liste_ressources[4]
                        couleur = "orange"
                        forme = "cercle"
                elif val_ressource > 500 and val_ressource <= val_max_ressources[5]:
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[5]
                        couleur = "grey"
                        forme = "cercle"
                elif val_ressource > 600 and val_ressource <= val_max_ressources[6]:
                    if type_case in [3,4]:
                        ressources = liste_ressources[6]
                        couleur = "blueviolet"
                        forme = "cercle"
                elif val_ressource > 700 and val_ressource <= val_max_ressources[7]:
                    if type_case in [3]:
                        ressources = liste_ressources[7]
                        couleur = "paleturquoise"
                        forme = "cercle"
                elif val_ressource > 800 and val_ressource <= val_max_ressources[8]:
                    if type_case in [1,3,4]:
                        ressources = liste_ressources[8]
                        couleur = "gold"
                        forme = "cercle"
                elif val_ressource > 900 and val_ressource <= val_max_ressources[9]:
                    if type_case in [1,2,5,6]:
                        ressources = liste_ressources[9]
                        couleur = "grey"
                        forme = "triangle"
                elif val_ressource > 1000 and val_ressource <= val_max_ressources[10]:
                    if type_case in [2]:
                        ressources = liste_ressources[10]
                        couleur = "seashell"
                        forme = "cercle"
                elif val_ressource > 1100 and val_ressource <= val_max_ressources[11]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[11]
                        couleur = "saddlebrown"
                        forme = "triangle"
                elif val_ressource > 1200 and val_ressource <= val_max_ressources[12]:
                    if type_case in [1,2,3,4,5,6]:
                        ressources = liste_ressources[12]
                        couleur = "gold"
                        forme = "carre"
                elif val_ressource > 1300 and val_ressource <= val_max_ressources[13]:
                    if type_case in [1,2,3,5]:
                        ressources = liste_ressources[13]
                        couleur = "white"
                        forme = "triangle"
                else:
                    ressources = liste_ressources[14]
            if ressources != "vide":    
                ressources_generees.append([ressources,idx,idy])
        
        return ressources,couleur,forme




    # Paramètres de l'hexagone
    taille_hexagone = 1.0
    distance_x_entre_hexagones = (math.sqrt(3)) * taille_hexagone
    distance_y_entre_hexagones = 3/2 * taille_hexagone

    # Coordonnées des sommets d'un hexagone régulier
    x_hexagone = np.array([np.cos(np.pi/3 * i + np.pi/6) for i in range(6)])
    y_hexagone = np.array([np.sin(np.pi/3 * i + np.pi/6) for i in range(6)])

    # Création de la figure
    fig, ax = plt.subplots()


    #variable globale pour stocker les ressources générées
    global ressources_generees
    ressources_generees = []



    # Affichage des 37 hexagones
    for ligne in range(1,nb_lignes+1):
        for col in range(1,nb_colonnes+1):
            for idy,i in enumerate(tuile_test):
                for idx,j in enumerate(i):
                
                    x_offset = idx * distance_x_entre_hexagones if idy % 2 == 0 else idx * distance_x_entre_hexagones + distance_x_entre_hexagones/2
                    y_offset = -idy * distance_y_entre_hexagones
                    
                    
                    x_coords = (x_hexagone + x_offset)+20*col
                    y_coords = (y_hexagone + y_offset)+20*ligne
                    
                    if j == 0:
                        ax.fill(x_coords, y_coords, edgecolor='white', facecolor='white')
                    elif j == 1:
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
                        
                    ressources,couleur,forme = generation_ressources(tuile_test,idx,idy)
                        
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
                
    print(ressources_generees)    

    # Configuration de l'axe
    ax.set_aspect('equal')
    ax.axis('off')  # Masque les axes

    # Affichage de la figure
    plt.show()