# -*- coding: utf8 -*-
my_list = []


def read_file(file):
    fichier = open(file, 'r')
    return(fichier.readlines())
    fichier.close()

my_list = read_file("MOCK_DATA.csv")

i = 1
genre = "Male"

fichier2 = open("Contacts masculins.csv", "w")
fichier2.write("Voici les contacts masculin de la liste :\n \n" )

for contact in my_list :
    if genre in contact:
        fichier2.write(contact)
    else:
        pass

fichier2.close()