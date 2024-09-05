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

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Ajout d'une étiquette (texte)
        label = tk.Label(root, text="Chasse et Pêche", font=("Helvetica", 40))
        label.pack()  # Affiche l'étiquette dans la fenêtre
       
        # Ajout d'un bouton
        button = tk.Button(root, text="Génération de map", command=afficher_carte)
        button.pack(anchor="nw", padx=10, pady=10)  # Affiche le bouton en haut à gauche

        # Création d'un Canvas pour dessiner les hexagones
        canvas = tk.Canvas(root, width=400, height=400, bg="white")
        canvas.pack(anchor="ne", padx=20, pady=20)

class Page2(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Ajout d'une étiquette (texte)
        label = tk.Label(root, text="Chasse et Pêche", font=("Helvetica", 40))
        label.pack()  # Affiche l'étiquette dans la fenêtre
       
        
        # Ajout d'une zone de texte pour entrer un nombre
        entry_nombre = tk.Entry(root)
        entry_nombre.pack(anchor="sw", padx=10, pady=10)

        # Bouton pour tirer un événement d'été
        button_generer_ete = tk.Button(root, text="Event été", command=lambda: tirer_evenement("events_ete", int(entry_nombre.get())))
        button_generer_ete.pack(anchor="sw", padx=10, pady=10)

        # Bouton pour tirer un événement d'hiver
        button_generer_hiver = tk.Button(root, text="Event hiver", command=lambda: tirer_evenement("events_hiver", int(entry_nombre.get())))
        button_generer_hiver.pack(anchor="sw", padx=10, pady=10)

        # Étiquette pour afficher des informations
        label_nombre = tk.Label(root, text="", font=("Helvetica", 16))
        label_nombre.pack(anchor="sw", padx=10, pady=10)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Génération map", command=p1.show)
        b2 = tk.Button(buttonframe, text="Evenements", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()