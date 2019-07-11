# -*- coding: utf8 -*-

class Personne:
    def __init__(self, prenom, nom, age, sexe, argent, items):

        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.argent = argent
        self.items = []

    def vieillir(self):
        self.age = self.age + 1

    def presenter(self):
         print("Je m'appelle", self.prenom, self.nom, ".J'ai", self.age, "ans et je suis", self.sexe,". Voici les items que je possède :", self.items)

    def saluer(self):
        print("Bonjour", self.prenom, "! Comment vas-tu ?")

    def travailler(self):
        self.argent = self.argent + 50

    def acheter(self, item, prix):
        if self.argent < prix :
            print("Vous n'avez pas assez d'argent !")
        else :
            self.items.append(item)
            self.argent = self.argent - prix


class Item:
    def __init__(self, intitule, valeur):
        self.intitule = intitule
        self.valeur = valeur



first_person = Personne('Simon', 'LARNE', 25, 'un homme', 250, ["Parapluie"])
second_person = Personne('Audrey', 'OVI', 40, 'une femme', 500, 1)
third_person = Personne("Romain", "DURAND", 34, "un homme", 50, 5)

voiture = Item("Voiture", 500)
parapluie = Item("Parapluie", 50)


def main():
    Personne.presenter(first_person)
    Personne.travailler(first_person)
    print(first_person.argent)
    Personne.acheter(voiture.intitule, voiture.valeur)

main()