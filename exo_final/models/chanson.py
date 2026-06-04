from enum import Enum
from .jouer import Jouable

class Genre(Enum):
    #region Enum

    POP = "pop"
    RAP = "rap"
    ROCK = "rock"
    JAZZ = "jazz"

    #endregion 

class Chanson(Jouable):
    #region Attributs

    def __init__(self, titre, artiste, duree, genre : Genre):
        self.__titre = titre
        self.__artiste = artiste
        self.__duree = duree
        self.__genre = genre

    #endregion

    #region Prop's

    @property
    def titre(self):
        return self.__titre
    
    @property
    def artiste(self):
        return self.__artiste
    
    @property
    def duree(self):
        return self.__duree

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if not isinstance(value, self.__genre):
            raise ValueError("Le genre doit être un choix valide.")
        self.__genre = value

    #endregion
    
    #region Méthodes
    def jouer(self):
        sent = 0
        while sent == 0:
            valeur_saisie = input(
                "Souhaitez-vous jouer une musique ? OUI/NON\n"
            ).lower().strip()
            if valeur_saisie == "oui":
                print(
                    f"{self.__titre} est en cours de lecture... "
                    f"{self.__duree} minute(s)\n"
                    f"Genre: {self.__genre} Artiste: {self.__artiste}"
                )
                sent += 1
            elif valeur_saisie == "non":
                print("Aucune musique n'est en cours de lecture...")
                sent += 1
            else:
                print("Veuillez répondre par OUI ou NON.")

            #endregion