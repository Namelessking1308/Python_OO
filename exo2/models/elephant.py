class Elephant:

    # Region Attributs

    def definir(self, nom, appetit = 50, satisfaction = 50, en_vie = True, soigneur = None):
        self._nom = nom
        self._appetit = max(0, min(100, appetit))
        self._satisfaction = max(0, min(100,satisfaction))
        self._en_vie = en_vie
        self._soigneur = soigneur
        return f"Élephant {nom} créé"

    # Endregion

    # Region Prop's

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom
    
    @property
    def appetit(self):
        return self._appetit
    
    @property
    def satisfaction(self):
        return self._satisfaction
    
    @property
    def en_vie(self):
        return self._en_vie
    
    @property
    def soigneur(self):
        return self._soigneur
    
    @soigneur.setter
    def soigneur(self, nouveau_soigneur):
        self._soigneur= nouveau_soigneur

    # Endregion

    # Region Méthodes

    def manger(self):
        if not hasattr(self, '_nom') or not self._en_vie:
            return "Erreur, Élephant non défini ou mort..."
        
        self._appetit = max(0, self._appetit - 25)
        self._satisfaction = min(100, self._satisfaction + 15)

        return(f"L'élephant {self._nom} a manger !\nAppétit : {self._appetit}/100\nSatisfaction : {self._satisfaction}/100")
    
    def afficher_etat(self):
        if not hasattr(self, '_nom'):
            return "Erreur, Élephant non défini..."
        etat = "Vivant" if self._en_vie else "Mort"
        soigneur_nom = self._soigneur.nom if self._soigneur else "Aucun"

        return(f"L'élephant {self._nom}\nAppétit : {self._appetit}/100\nSatisfaction : {self._satisfaction}/100\nÉtat : {etat}\nSoigneur : {soigneur_nom}")
    
    #Endregion