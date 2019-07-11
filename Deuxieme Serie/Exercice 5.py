# -*- coding: utf8 -*-
import csv
import argparse
parser = argparse.ArgumentParser()


fname="MOCK_DATA.csv"
i = 0
max_result = 0
maxresult = 0


# genre = "male", "female"

parser.add_argument("--genre", help="définir le genre des personnes à rechercher")
parser.add_argument("--max_result", help="définir une limite aux résultats", type=int)
args = parser.parse_args()
if args.max_result is None :
    with open(fname, "r") as my_file:
        for line in my_file:
            maxresult += 1
else :
    max_result = (args.max_result)

genre = (args.genre)
maxresult = max_result

print(maxresult, max_result)

with open(fname, "r") as fichier :
    print("Voici les 30 premières personnes de la liste :")
    reader = csv.reader(fichier)
    for line in reader:
        i += 1
        if i == maxresult+1:
            break
        elif genre in line:
            print(line[1],line[2],"est le contact n°",line[0],". Il s'agit d'un Homme.")
        else:
            print(line[1],line[2], "est le contact n°",line[0],". Il s'agit d'une Femme.")