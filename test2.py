import tkinter as tk

from generer_carte import generer_carte
from generation_evenement import tirer_evenement

#################################################################################################################

def afficher_carte():
    nom, ressources = generer_carte()
    
    # Créer un fichier txt avec les ressources
    creer_recapitulatif(ressources)
    
    # Dessiner les hexagones avec des labels de texte à l'intérieur
    hexagone_size = 50
    offset_y = hexagone_size * (3 ** 0.5)  # Distance verticale entre les centres des hexagones
    dessiner_hexagone(canvas, 50, 50 + 0.9 * hexagone_size, hexagone_size, nom[2])
    dessiner_hexagone(canvas, 50, 50 + offset_y + 0.9 * hexagone_size, hexagone_size, nom[1])
    dessiner_hexagone(canvas, 50, 50 + 2 * offset_y + 0.9 * hexagone_size, hexagone_size, nom[0])

    dessiner_hexagone(canvas, 50 + hexagone_size * 1.5, 50, hexagone_size, nom[6])
    dessiner_hexagone(canvas, 50 + hexagone_size * 1.5, 50 + offset_y, hexagone_size, nom[5])
    dessiner_hexagone(canvas, 50 + hexagone_size * 1.5, 50 + 2 * offset_y, hexagone_size, nom[4])
    dessiner_hexagone(canvas, 50 + hexagone_size * 1.5, 50 + 3 * offset_y, hexagone_size, nom[3])

    dessiner_hexagone(canvas, 50 + hexagone_size * 3, 50 + 0.9 * hexagone_size, hexagone_size, nom[9])
    dessiner_hexagone(canvas, 50 + hexagone_size * 3, 50 + offset_y + 0.9 * hexagone_size, hexagone_size, nom[8])
    dessiner_hexagone(canvas, 50 + hexagone_size * 3, 50 + 2 * offset_y + 0.9 * hexagone_size, hexagone_size, nom[7])

    dessiner_hexagone(canvas, 50 + hexagone_size * 4.5, 50 + offset_y, hexagone_size, nom[11])
    dessiner_hexagone(canvas, 50 + hexagone_size * 4.5, 50 + 2 * offset_y, hexagone_size, nom[10])

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
        
        
###################################################################################################################3

root=tk.Tk()
root.geometry("360x360")

frame=tk.Frame(root,bg='lightblue')
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

def page1():
    # Ajout d'une étiquette (texte)
    label = tk.Label(root, text="Chasse et Pêche", font=("Helvetica", 40))
    label.pack()  # Affiche l'étiquette dans la fenêtre
    
    # Ajout d'un bouton
    button = tk.Button(root, text="Génération de map", command=afficher_carte)
    button.pack(anchor="nw", padx=10, pady=10)  # Affiche le bouton en haut à gauche

    # Création d'un Canvas pour dessiner les hexagones
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(anchor="ne", padx=20, pady=20)

def page2():
    label=tk.Label(frame,text='this is the page2')
    label.place(relx=0.3,rely=0.4)

def page3():
    label=tk.Label(frame,text='this is the page3')
    label.place(relx=0.3,rely=0.4)

bt=tk.Button(root,text='page1',command=page1)
bt.grid(column=0,row=0)

bt1=tk.Button(root,text='page2',command=page2)
bt1.grid(row=0,column=1)

bt2=tk.Button(root,text='page3',command=page3)
bt2.grid(row=0,column=2)

root.mainloop()