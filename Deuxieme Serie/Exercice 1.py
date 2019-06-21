# -*- coding: utf8 -*-
my_list = []


def read_file(file):
    fichier = open(file, 'r')
    return(fichier.readlines())
    fichier.close()

my_list = read_file("MOCK_DATA.csv")

i = 1
genre = "Male"

print("Voici les 30 premières personnes de la liste :")

while i < 31 :
    str1 = ''.join(my_list[i])
    list2 = str1.split(',')
    i += 1
    if genre in str1:
        print(list2[1],list2[2],"est le contact n°",list2[0],". Il s'agit d'un Homme.")
    else:
        print(list2[1],list2[2], "est le contact n°",list2[0],". Il s'agit d'une Femme.")
