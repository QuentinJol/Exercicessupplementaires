# -*- coding: utf8 -*-
from operator import itemgetter
my_list = []


def read_file(file):
    fichier = open(file, 'r')
    return(fichier.readlines())
    fichier.close()

my_list = read_file("MOCK_DATA.csv")

i = 1
genre = "Female"
list2 = []

for contact in my_list :
    if genre in contact:
        list2.append(contact.split(","))


# female_list = []

# for contact in list2 :
#     str1 = ''.join(contact)
#     list3 = str1.split(',')
#     female_list.append(list3)

classed_female_list = []
#female_list_tuples = [tuple(l) for l in female_list]

classed_female_list = sorted(list2, key=itemgetter(3))


fichier2 = open("Contacts feminins.csv", "w")
fichier2.write("Voici les contacts féminins de la liste, triés par ordre alphabétique :\n \n" )


for contact in classed_female_list :
    line = ",".join(contact)
    fichier2.write(line)

fichier2.close()
