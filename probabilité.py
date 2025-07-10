import random

def average_successes(nb_dice, threshold, iterations=100000):
    total_successes = 0
    for _ in range(iterations):
        dice_to_roll = [1] * nb_dice
        successes = 0
        while dice_to_roll:
            new_dice = []
            for _ in dice_to_roll:
                roll = random.randint(1, 6)
                if roll >= threshold:
                    successes += 1
                if roll == 6:
                    new_dice.append(1)  # 6 explosif = 1 dé en plus
            dice_to_roll = new_dice
        total_successes += successes
    return total_successes / iterations

# Exemple d'utilisation
for d in range(1, 11):  # de 1d6 à 10d6
    avg = average_successes(nb_dice=d, threshold=5)
    print(f"{d}d6 (seuil 5+): {avg:.3f} succès moyens")
