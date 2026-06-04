from .jouer import Jouable

class Publicite(Jouable):
    #region Attributs

    def __init__(self, marque, duree):
        self.__marque = marque
        self.__duree = duree

    #endregion

    #region Prop's

    @property
    def marque(self):
        return self.__marque
    
    @property
    def duree(self):
        return self.__duree

    #endregion
    
    #region Méthodes
    def jouer(self):
        return (f"--Publicité--"
                f"{self.marque}"
                f"{self.duree} minute(s)")
    #endregion