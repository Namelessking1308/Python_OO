class Soigneur:

    # Region Attributs

    def definir(self, nom, date_naissance, experience, nombre_animaux_responsable = 0):
        self._nom = nom
        self._date_naissance = date_naissance
        self._experience = experience
        self._nombre_animaux_responsable = nombre_animaux_responsable
        return f"Le soigneur {nom} créé"
    
    # Endregion

    # Region Prop's

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def date_naissance(self):
        return self._date_naissance
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def nombre_animaux_responsable(self):
        return self._nombre_animaux_responsable
    
    # Endregion

    # Region Méthodes

    def nourir(self, animal):
        """
        Nourrit seulement si on est le soigneur de l'animal
        """
        if not hasattr(self, '_nom') or not hasattr(animal, '_soigneur'):
            return "Erreur soigneur ou animal non défini..."
        
        if self != animal._soigneur:
            return f"{self._nom} n'est pas le soigneur de {animal._nom}"
        
        animal._appetit = max(0, animal._appetit - 40)
        animal._satisfaction = min(100, animal._satisfaction + 10)
        return f"{self._nom} a nourri {animal._nom} !\nAppétit maintenant : {animal._appetit}/100"
    
    def entretenir(self, animal):
        """
        Entretient seulement si responsable
        """
        if not hasattr(self, '_nom') or not hasattr(animal, '_soigneur'):
            return "Erreur soigneur ou animal non défini..."
                
        if self != animal._soigneur:
            return f"{self._nom} n'est pas le soigneur de {animal._nom}"
        
        animal._satisfaction = min(100, animal._satisfaction + 35)
        
        return f"{self._nom} a entretenu {animal._nom} !\nSatisfaction maintenant : {animal._satisfaction}/100"
    
    # Endregion