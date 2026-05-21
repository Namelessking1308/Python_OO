class Soigneur:

    def definir(self, nom, date_naissance, experience, nombre_animaux_responsable = 0):
        self.nom = nom
        self.date_naissance = date_naissance
        self.experience = experience
        self.nombre_animaux_responsable = nombre_animaux_responsable
        return f"Le soigneur {nom} créé"
    
    def nourir(self, animal):
        """
        Nourrit seulement si on est le soigneur de l'animal
        """
        if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
            return "Erreur soigneur ou animal non défini..."
        
        if self != animal.soigneur:
            return f"{self.nom} n'est pas le soigneur de {animal.nom}"
        
        animal.appetit = max(0, animal.appetit - 40)
        animal.satisfaction = min(100, animal.satisfaction + 10)
        return f"{self.nom} a nourri {animal.nom} !\nAppétit maintenant : {animal.appetit}/100"
    
    def entretenir(self, animal):
        """
        Entretient seulement si responsable
        """
        if not hasattr(self, 'nom') or not hasattr(animal, 'soigneur'):
            return "Erreur soigneur ou animal non défini..."
                
        if self != animal.soigneur:
            return f"{self.nom} n'est pas le soigneur de {animal.nom}"
        
        animal.satisfaction = min(100, animal.satisfaction + 35)
        
        return f"{self.nom} a entretenu {animal.nom} !\nSatisfaction maintenant : {animal.satisfaction}/100"
        
        