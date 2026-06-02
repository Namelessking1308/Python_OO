from abc import ABC, abstractmethod
from .chanson import Chanson

class Jouable(ABC, Chanson):

    @abstractmethod
    def jouer(self):
        while True:
            valeur_saisie = input(
                "Souhaitez-vous jouer une musique ? OUI/NON\n"
            ).lower().strip()
            if valeur_saisie == "oui":
                print(
                    f"{self.titre} est en cours de lecture... "
                    f"{self.duree} minute(s)\n"
                    f"Genre: {self.__genre} Artiste: {self.artiste}"
                )
                return
            elif valeur_saisie == "non":
                print("Aucune musique n'est en cours de lecture...")
                return
            else:
                print("Veuillez répondre par OUI ou NON.")