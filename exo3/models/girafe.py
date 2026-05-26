from .animal import Animal
from .elephant import Elephant

    # Region Attributs

class Girafe(Animal):
    
    def definir(self, nom, appetit, satisfaction, en_vie, soigneur, longueur_cou):
        super().definir(nom , appetit, satisfaction, en_vie , soigneur)
        self.__longueur_cou = longueur_cou

        return f"Girafe {self.nom} créé qui a une longueur de cou de {self.longueur_cou} m"
    
    # Endregion

    # Region Prop's
    @property
    def longueur_cou(self):
        return self.__longueur_cou
    
    @longueur_cou.setter
    def longueur_cou(self, value):
        self.__longueur_cou = value

    # Endregion

    # Region Méthodes

    def manger_feuilles(self):
        Elephant.manger()

    def boire_eau(self):
        Elephant.manger()

    def observer_environnement(self):
        return f"{self.nom} observe son environnement..."
    # Endregion