from .jouer import Jouable

class Playliste():
    
    #region Attributs

    def __init__(self, nom):
        self.__nom = nom
        self.__liste_jouable = []

    #endregion

    #region Prop's

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def liste_jouable(self):
        return self.__liste_jouable
    
    @liste_jouable.setter
    def liste_jouable(self, value):
        self.__liste_jouable = value


    #endregion

    #region Méthodes

    def ajouter_piste(self, piste):
        self.__liste_jouable.append(piste)
        return f"{piste} ajouter à la playliste {self.__nom}"

    def lire_playliste(self):
        for i in self.__liste_jouable:
            return f"La playliste {self.__nom} {Jouable.jouer(i)}"
    #endregion