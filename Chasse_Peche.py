import tkinter as tk
from generer_carte import generer_carte, generer_carte_14

import random
import json


def centrer_fenetre(fenetre):
    fenetre.update_idletasks()
    largeur_fenetre = fenetre.winfo_width()
    hauteur_fenetre = fenetre.winfo_height()
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()
    x = (largeur_ecran // 2) - (largeur_fenetre // 2)
    y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)
    fenetre.geometry(f'{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}')

root = tk.Tk()
root.geometry("800x800")  # Adjusted window size for better fit
centrer_fenetre(root)

frame = tk.Frame(root)
frame.place(relx=0.1, rely=0.1, relheight=0.9, relwidth=0.9)


def clear_frame():
    # Clears the content of the frame before loading a new page
    for widget in frame.winfo_children():
        widget.destroy()

def page1():
    clear_frame()
    
    def afficher_carte():
        nom, ressources = generer_carte()
        
        # Create recap file
        creer_recapitulatif(ressources)
        
        hexagone_size = 50
        offset_y = hexagone_size * (3 ** 0.5)  # Vertical distance between centers of hexagons

        # Drawing hexagons on canvas
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
        
    def afficher_carte_14():
        print("generer carte 14 :")
        nom, ressources = generer_carte_14()
        
        # Create recap file
        creer_recapitulatif(ressources)
        
        hexagone_size = 50
        offset_y = hexagone_size * (3 ** 0.5)  # Vertical distance between centers of hexagons

        # Drawing hexagons on canvas
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
        points = [
            x + size * 0.5, y,
            x + size * 1.5, y,
            x + size * 2, y + size * (3 ** 0.5) / 2,
            x + size * 1.5, y + size * (3 ** 0.5),
            x + size * 0.5, y + size * (3 ** 0.5),
            x, y + size * (3 ** 0.5) / 2
        ]
        canvas.create_polygon(points, outline='black', fill='white', width=2)
        canvas.create_text(x + size, y + size * (3 ** 0.5) / 2, text=text, font=("Helvetica", 8))
        
    def creer_recapitulatif(ressources):
        with open("recap_ressources.txt", "w") as fichier:
            nb_ressources = 0
            fichier.write("Recapitulatif des ressources :\n")
            for ressource in ressources:
                fichier.write(f"{ressource[1]} {ressource[0]}\n")
                nb_ressources += ressource[1] 
            fichier.write(f"Il y a {nb_ressources} ressources sur la carte \n")
    
    button = tk.Button(frame, text="Génération de map 12 tuiles", command=afficher_carte)
    button.pack(anchor="nw", padx=10, pady=10)
    
    button2 = tk.Button(frame, text="Génération de map 14 tuiles", command=afficher_carte_14)
    button2.pack(anchor="nw", padx=10, pady=10)

    canvas = tk.Canvas(frame, width=350, height=350, bg="white")  # Adjusted canvas size
    canvas.pack(anchor="ne", padx=20, pady=20)

def page2():
    clear_frame()
    label = tk.Label(frame, text="Events et Dynasties", font=("Helvetica", 40))
    label.pack()

    def tirer_evenement(saison, amplitude_joueur):
        try:
            # Charger le fichier JSON des événements
            with open('JSON/Evenements.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            label_evenement.config(text="Fichier Evenements.json introuvable.")
            return None

        # Vérifier si la saison est valide
        if saison not in data:
            label_evenement.config(text="Saison invalide.")
            print(saison)
            print(data[saison])
            return None

        evenements = data[saison]
        events_pondere = []
        for evenement in evenements:
            if 'nombre_occurences' in evenement:
                events_pondere.extend([evenement] * evenement['nombre_occurences'])

        # Choisir un événement aléatoire
        evenement = random.choice(events_pondere)
        amplitude_aleatoire = random.randint(1, 8)
        
        # Vérifier si le nombre du joueur est valide
        if amplitude_joueur < 0 or amplitude_joueur > 3:
            label_evenement.config(text="Nombre invalide. Veuillez entrer un nombre entre 0 et 3.")
            return

        # Calculer l'amplitude finale
        amplitude_finale = amplitude_aleatoire + amplitude_joueur
        description = ""
        
        # Déterminer la description de l'événement en fonction de l'amplitude
        if evenement['ampleur_low_1'] <= amplitude_finale <= evenement['ampleur_high_1']:
            description = evenement['ampleur_description_1']
        elif evenement['ampleur_low_2'] <= amplitude_finale <= evenement['ampleur_high_2']:
            description = evenement['ampleur_description_2']
        elif evenement['ampleur_low_3'] <= amplitude_finale <= evenement['ampleur_high_3']:
            description = evenement.get('ampleur_description_3', "Aucune description pour cette ampleur.")
        
        # Mettre à jour le texte du label avec les informations de l'événement
        texte_evenement = (
            f"Événement: {evenement['nom']}\n"
            f"Amplitude : {amplitude_finale}\n"
            f"Description: {description}"
        )
        label_evenement.config(text=texte_evenement)

    def tirer_dynastie():
        try:
            # Charger le fichier JSON des événements
            with open('JSON/Dynasties.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
        except FileNotFoundError:
            label_dynastie.config(text="Fichier Dynasties.json introuvable.")
            return None

        # Choisir un événement aléatoire
        dynastie = random.choice(data2['Dynasties'])
        
        
        # Mettre à jour le texte du label avec les informations de l'événement
        texte_dynastie = (
            f"Dynastie: {dynastie['nom']}\n"
            f"Description: {dynastie['description']}"
        )
        label_dynastie.config(text=texte_dynastie)
    
    # Fonction pour obtenir la saisie utilisateur
    def get_user_input():
        try:
            return int(entry_nombre.get())
        except ValueError:
            return 0  # Si l'entrée est invalide, retourne 0

    # Zone d'entrée pour le nombre du joueur
    entry_nombre = tk.Entry(frame)
    entry_nombre.pack(anchor="sw", padx=10, pady=10)

    # Boutons pour générer des événements selon la saison
    button_generer_ete = tk.Button(frame, text="Event été", command=lambda: tirer_evenement("events_ete", get_user_input()))
    button_generer_ete.pack(anchor="sw", padx=10, pady=10)

    button_generer_hiver = tk.Button(frame, text="Event hiver", command=lambda: tirer_evenement("events_hiver", get_user_input()))
    button_generer_hiver.pack(anchor="sw", padx=10, pady=10)
    
    # Créer un label pour afficher les informations de l'événement
    label_evenement = tk.Label(frame, text="", font=("Helvetica", 15), justify="left", wraplength=400)
    label_evenement.pack(anchor="sw", padx=10, pady=10)
    
    # Bouton pour générer une dynastie
    button_generer_dynastie = tk.Button(frame, text="Dynastie", command=tirer_dynastie)
    button_generer_dynastie.pack(anchor="sw", padx=10, pady=10)
    
    # Créer un label pour afficher les informations de la dynastie
    label_dynastie = tk.Label(frame, text="", font=("Helvetica", 15), justify="left", wraplength=400)
    label_dynastie.pack(anchor="sw", padx=10, pady=10)



def page3():
    clear_frame()
    label = tk.Label(frame, text="Naissances", font=("Helvetica", 40))
    label.pack()
    
    def tirer_Naissance():
        try:
            # Charger le fichier JSON des événements
            with open('JSON/Naissances.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            label_evenement.config(text="Fichier Evenements.json introuvable.")
            return None

        
        # Choix du genre
        genres = data['Genre']
        genres_pondere = []
        for genre in genres:
            if 'nombre_occurences' in genre:
                genres_pondere.extend([genre] * genre['nombre_occurences'])
        genre = random.choice(genres_pondere)

        # Choix de l'orientation sexuelle
        orientation_sexuelle = data['Orientation sexuelle']
        orientation_sexuelle_pondere = []
        for orientation in orientation_sexuelle:
            if 'nombre_occurences' in orientation:
                orientation_sexuelle_pondere.extend([orientation] * orientation['nombre_occurences'])
        orientation = random.choice(orientation_sexuelle_pondere)
        
        # choix du trait génétique
        traits_genetiques = data['Genetique']
        traits_genetiques_pondere = []
        for trait in traits_genetiques:
            if 'nombre_occurences' in trait:
                traits_genetiques_pondere.extend([trait] * trait['nombre_occurences'])
        trait = random.choice(traits_genetiques_pondere)
    

        
        # Mettre à jour le texte du label avec les informations de l'événement
        texte_evenement = (
            f"Genre: {genre['nom']}\n"
            f"Orientation Sexuelle : {orientation['nom']}\n"
            f"Trait génétique: {trait['nom']}\n\n"
            f"Description: {trait['description']}"
        )
        label_evenement.config(text=texte_evenement)
        
    # Bouton pour générer une Naissance
    button_generer_Naissance = tk.Button(frame, text="Naissance", command=tirer_Naissance)
    button_generer_Naissance.pack(anchor="sw", padx=10, pady=10)
        
    # Créer un label pour afficher les informations de la naissance
    label_evenement = tk.Label(frame, text="", font=("Helvetica", 15), justify="left", wraplength=400)
    label_evenement.pack(anchor="sw", padx=10, pady=10)
    
def page4():
    clear_frame()
    label = tk.Label(frame, text="Village", font=("Helvetica", 40))
    label.pack()
    
    def tirer_village():
        try:
            # Charger le fichier JSON des événements
            with open('JSON/Villages.json', 'r', encoding='utf-8') as file:
                data3 = json.load(file)
        except FileNotFoundError:
            label_village.config(text="Fichier Dynasties.json introuvable.")
            return None
        
        # Choisir un événement aléatoire
        villages = data3['Villages']
        events_pondere = []
        for village in villages:
            if 'nombre_occurences' in village:
                events_pondere.extend([village] * village['nombre_occurences'])
                
        vill = random.choice(data3['Villages'])
        
        if vill['nom'] == 'Offrande':
            village_offrande = random.choice(vill['description'])
            # Mettre à jour le texte du label avec les informations de l'événement
            texte_village = (
                f"village: {vill['nom']}\n"
                f"Description: {village_offrande['description']}\n"
            )
            label_village.config(text=texte_village)
        else:
            # Mettre à jour le texte du label avec les informations de l'événement
            texte_village = (
                f"village: {vill['nom']}\n"
                f"Description: {vill['description']}"
            )
            label_village.config(text=texte_village)
            
    # Bouton pour générer un village
    button_generer_village = tk.Button(frame, text="Village", command=tirer_village)
    button_generer_village.pack(anchor="sw", padx=10, pady=10)
    
    # Créer un label pour afficher les informations du village
    label_village = tk.Label(frame, text="", font=("Helvetica", 15), justify="left", wraplength=400)
    label_village.pack(anchor="sw", padx=10, pady=10)
    
def page5():
    clear_frame()
    label = tk.Label(frame, text="Maladies", font=("Helvetica", 40))
    label.pack()
    
    def tirer_maladie():
        try:
            # Charger le fichier JSON des événements
            with open('JSON/Maladies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            label_maladie.config(text="Fichier Evenements.json introuvable.")
            return None
        
        #choix de la maladie aléatoire
        maladie = random.choice(data['Maladies'])
        
        # Mettre à jour le texte du label avec les informations de l'événement
        texte_maladie = (
            f"Maladie: {maladie['nom']}\n"
            f"sexuellement transmissible : {maladie['sexuellement_transmissible']}\n"
            f"héréditaire : {maladie['hereditaire']}\n\n"
            f"Description: {maladie['description']}"
        )
        label_maladie.config(text=texte_maladie)
    
    #bouton pour générer une maladie
    button_generer_maladie = tk.Button(frame, text="Maladie", command=tirer_maladie)
    button_generer_maladie.pack(anchor="sw", padx=10, pady=10)
    
    # Créer un label pour afficher les informations de la maladie
    label_maladie = tk.Label(frame, text="", font=("Helvetica", 15), justify="left", wraplength=400)
    label_maladie.pack(anchor="sw", padx=10, pady=10)
    

label = tk.Label(frame, text="Chasse et Pêche", font=("Helvetica", 40))
label.pack()

bt = tk.Button(root, text='Carte', command=page1)
bt.grid(column=0, row=0)

bt1 = tk.Button(root, text='Evenements et Dynasties', command=page2)
bt1.grid(row=0, column=1)

bt2 = tk.Button(root, text='Naissance', command=page3)
bt2.grid(row=0, column=2)

bt3 = tk.Button(root, text='Villages', command=page4)
bt3.grid(row=0, column=3)

bt4 = tk.Button(root, text='Maladies', command=page5)
bt4.grid(row=0, column=4)

root.mainloop()
