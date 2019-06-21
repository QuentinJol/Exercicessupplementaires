# -*- coding: utf8 -*-
import random

# Creation d'une liste de 1000 nombres aléatoires
ma_liste = [ random.randint(0, 10000) for _ in range(1000) ]


# Tri de cette liste dans l'ordre croissant
ma_liste.sort()

# Affichage de la valeur la plus élevée de la liste
print("Voici la valeur la plus haute de la liste : ", ma_liste[999])

# Affichage de la valeur la plus basse de la liste
print("Voici la valeur la plus basse de la liste : ", ma_liste[0])
