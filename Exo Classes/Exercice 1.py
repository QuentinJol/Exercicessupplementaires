# -*- coding: utf8 -*-

class Personne:
    def __init__(self, prenom, nom, age, sexe):

        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sexe = sexe

    def vieillir(self):
        self.age = self.age + 1

    def presenter(self):
         print("Je m'appelle", self.prenom, self.nom, ".J'ai", self.age, "ans et je suis", self.sexe,".")

    def saluer(self):
        print("Bonjour", self.prenom, "! Comment vas-tu ?")

first_person = Personne('Simon', 'LARNE', 25, 'un homme')
second_person = Personne('Audrey', 'OVI', 40, 'une femme')
third_person = Personne("Romain", "DURAND", 34, "un homme")

def main():
    Personne.vieillir(first_person)
    Personne.presenter(first_person)
    Personne.presenter(second_person)
    Personne.saluer(first_person)
    Personne.presenter(third_person)
    Personne.vieillir(third_person)
    Personne.presenter(third_person)
    Personne.saluer(second_person)

main()