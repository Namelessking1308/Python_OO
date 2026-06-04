from .jouer import Jouable

class Podcast(Jouable):
    #region Attributs

    def __init__(self, titre, animateur, duree):
        self.__titre = titre
        self.__animateur = animateur
        self.__duree = duree

    #endregion
    
    #region Prop's

    @property
    def titre(self):
        return self.__titre
    
    @property
    def animateur(self):
        return self.__animateur
    
    @property
    def duree(self):
        return self.__duree

    #endregion

    #region Méthodes

    def jouer(self):
        sent = 0
        while sent == 0:
            valeur_saisie = input(
                "Souhaitez-vous jouer le Podcast ? OUI/NON\n"
            ).lower().strip()
            if valeur_saisie == "oui":
                print(
                    f"{self.__titre} est en cours de lecture... "
                    f"Animateur: {self.__animateur} "
                    f"{self.__duree} minute(s)\n"
                )
                sent += 1
            elif valeur_saisie == "non":
                print("Aucun podcast n'est en cours de lecture...")
                sent += 1
            else:
                print("Veuillez répondre par OUI ou NON.")

    #endregion
        