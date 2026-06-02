from enum import Enum

class Genre(Enum):
    POP = "pop"
    RAP = "rap"
    ROCK = "rock"
    JAZZ = "jazz"

class Chanson():

    def __init__(self, titre, artiste, duree, genre : Genre):
        self.titre = titre
        self.artiste = artiste
        self.duree = duree
        self.__genre = genre

    @property
    def genre(self):
        return self.genre

    @genre.setter
    def genre(self, value):
        if not isinstance(value, self.genre):
            raise ValueError("Le genre doit être un choix valide.")
        self.__genre = value

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
        
        
        
