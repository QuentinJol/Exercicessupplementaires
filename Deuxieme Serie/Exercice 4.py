# -*- coding: utf8 -*-
import csv



i = 0
genre = "Male"
fname="MOCK_DATA.csv"
with open(fname, "r") as fichier :
    print("Voici les 30 premières personnes de la liste :")
    reader = csv.reader(fichier)
    for line in reader:
        i += 1
        if i == 32:
            break
        elif genre in line:
            print(line[1],line[2],"est le contact n°",line[0],". Il s'agit d'un Homme.")
        else:
            print(line[1],line[2], "est le contact n°",line[0],". Il s'agit d'une Femme.")

