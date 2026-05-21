from models import Elephant

class Enclos:

    def Caracteristique_enclos(self, nom, capacite_max, taille, liste_animaux):
        self.nom = nom
        self.capacite_max = capacite_max
        self.taille = taille
        self.liste_animaux = liste_animaux

    def ajouter_animal(self, animal : Elephant):
        if not hasattr(self, 'animal'):
            self.animaux = []
            self.animaux.append(animal.nom)
            return f"{animal.nom} ajouter à l'enclos."
        
    def enleve_animal(self, animal : Elephant):
        if animal.en_vie is not True:
            animal.pop
            return f"{animal.nom} est mort..."
        else:
            return f"{animal.nom} est encore en vie !"

    def afficher_animal(self, animal : Elephant):
        print(f"Il y a {animal.nom} dans l'enclos")