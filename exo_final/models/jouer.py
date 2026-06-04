from abc import ABC, abstractmethod

class Jouable(ABC):

    #region ABC
    @abstractmethod
    def jouer(self):
        pass

    #endregion