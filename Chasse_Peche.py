import tkinter as tk
import random
from generer_carte import generer_carte

def afficher_carte():
    nom,ressources = generer_carte()
    
    #creer un fichier txt avec les ressources
    creer_recapitulatif(ressources)
    
    # Dessiner trois hexagones avec un label de texte à l'intérieur de chacun
    hexagone_size = 50
    offset_y = hexagone_size * (3 ** 0.5)  # Distance verticale entre les centres des hexagones
    dessiner_hexagone(canvas, 50, 50 + 0.9*hexagone_size, hexagone_size, nom[2])
    dessiner_hexagone(canvas, 50, 50 + offset_y + 0.9*hexagone_size, hexagone_size, nom[1])
    dessiner_hexagone(canvas, 50, 50 + 2 * offset_y + 0.9*hexagone_size, hexagone_size, nom[0])

    dessiner_hexagone(canvas, 50 +  hexagone_size * 1.5, 50 , hexagone_size, nom[6])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 1.5, 50 + offset_y , hexagone_size, nom[5])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 1.5, 50 + 2 * offset_y , hexagone_size, nom[4])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 1.5, 50 + 3 * offset_y , hexagone_size, nom[3])

    dessiner_hexagone(canvas, 50 +  hexagone_size * 3, 50 + 0.9*hexagone_size, hexagone_size, nom[9])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 3, 50 + offset_y + 0.9*hexagone_size, hexagone_size, nom[8])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 3, 50 + 2 * offset_y + 0.9*hexagone_size, hexagone_size, nom[7])

    dessiner_hexagone(canvas, 50 +  hexagone_size * 4.5, 50 + offset_y , hexagone_size, nom[11])
    dessiner_hexagone(canvas, 50 +  hexagone_size * 4.5, 50 + 2 * offset_y , hexagone_size, nom[10])
        
    
    

def generer_nombre_aleatoire():
    nombre_aleatoire = random.randint(0, 100)
    label_nombre.config(text=f"Évènement : {nombre_aleatoire}")

def dessiner_hexagone(canvas, x, y, size, text):
    # Calculer les coordonnées des sommets de l'hexagone
    points = [
        x + size * 0.5, y,
        x + size * 1.5, y,
        x + size * 2, y + size * (3 ** 0.5) / 2,
        x + size * 1.5, y + size * (3 ** 0.5),
        x + size * 0.5, y + size * (3 ** 0.5),
        x, y + size * (3 ** 0.5) / 2
    ]
    # Dessiner l'hexagone
    canvas.create_polygon(points, outline='black', fill='white', width=2)
    # Ajouter un label de texte à l'intérieur de l'hexagone
    canvas.create_text(x + size, y + size * (3 ** 0.5) / 2, text=text, font=("Helvetica", 8))
    
def creer_recapitulatif(ressources):
    # Ouvrir un fichier en mode écriture
    with open("recap_ressources.txt", "w") as fichier:
        nb_ressources = 0
        fichier.write("Recapitulatif des ressources :\n")
        for ressource in ressources:
            fichier.write(f"{ressource[1]} {ressource[0]}\n")
            nb_ressources += ressource[1] 
        fichier.write(f"Il y a {nb_ressources} ressources sur la carte \n")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chasse et Pêche")
root.geometry("1000x800")  # Dimensions de la fenêtre

# Ajout d'une étiquette (texte)
label = tk.Label(root, text="Chasse et Pêche", font=("Helvetica", 40))
label.pack()  # Affiche l'étiquette dans la fenêtre

# Ajout d'un bouton
button = tk.Button(root, text="Génération de map", command=afficher_carte)
button.pack(anchor="nw", padx=10, pady=10)  # Affiche le bouton en haut à gauche

# Création d'un Canvas pour dessiner les hexagones
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(anchor="ne", padx=20, pady=20)



# Ajout d'un bouton pour générer un nombre aléatoire
button_generer = tk.Button(root, text="Générer un nombre aléatoire", command=generer_nombre_aleatoire)
button_generer.pack(anchor="sw", padx=10, pady=10)  # Ajoute de la marge autour du bouton

# Étiquette pour afficher le nombre généré
label_nombre = tk.Label(root, text="", font=("Helvetica", 16))
label_nombre.pack(anchor="sw", padx=10, pady=10)

# Lancement de la boucle principale
root.mainloop()
