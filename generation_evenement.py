import json
import random



def tirer_evenement(saison, amplitude_joueur):
    # Charger le fichier JSON depuis le dossier JSON/Evenements.json
    with open('JSON/Evenements.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Vérifier si la saison existe dans le fichier
    if saison not in data:
        print("Saison invalide.")
        return None
    
    # Extraire la liste des événements de la saison
    evenements = data[saison]
    
    # Créer une liste pondérée d'événements en fonction de 'nombre_occurences'
    events_pondere = []
    for evenement in evenements:
        if 'nombre_occurences' in evenement and evenement['nombre_occurences'] is not None:
            events_pondere.extend([evenement] * evenement['nombre_occurences'])
    
    # Choisir un événement au hasard dans cette liste pondérée
    evenement = random.choice(events_pondere)
    
    # Générer une amplitude aléatoire entre 1 et 8
    amplitude_aleatoire = random.randint(1, 8)
    print(f"Amplitude générée aléatoirement: {amplitude_aleatoire}")
    
    # Demander au joueur de saisir un nombre entre 1 et 3
    try:
        if amplitude_joueur < 1 or amplitude_joueur > 3:
            print("Nombre invalide. Veuillez entrer un nombre entre 1 et 3.")
            return
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return
    
    # Ajouter le nombre du joueur à l'amplitude aléatoire
    amplitude_finale = amplitude_aleatoire + amplitude_joueur
    
    
    # Déterminer la description en fonction de l'amplitude finale
    description = ""
    if evenement['ampleur_low_1'] <= amplitude_finale <= evenement['ampleur_high_1']:
        description = evenement['ampleur_description_1']
    elif evenement['ampleur_low_2'] <= amplitude_finale <= evenement['ampleur_high_2']:
        description = evenement['ampleur_description_2']
    elif evenement['ampleur_low_3'] <= amplitude_finale <= evenement['ampleur_high_3']:
        description = evenement.get('ampleur_description_3', "Aucune description pour cette ampleur.")

    # Afficher l'événement et les détails
    print(f"\nÉvénement: {evenement['nom']}")
    print(f"Amplitude : {amplitude_finale}")
    print(f"Description: {description}")

