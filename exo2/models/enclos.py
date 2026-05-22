class Enclos:

    # Region Attributs

    def definir(self, nom, capacite_max, taille):
        self._nom = nom
        self._capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = []
        return f"Enclos {nom} créé"
    
    # Endregion

    # Region Prop's

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom

    @property
    def capacite_max(self):
        return self._capacite_max
    
    @capacite_max.setter
    def capacite_max(self, nouvelle_capacite_max):
        self._capacite_max = nouvelle_capacite_max

    @property
    def taille(self):
        return self._taille
    
    @property
    def liste_animaux(self):
        return self._liste_animaux
    
    # Endregion

    # Region Méthodes
    
    def ajouter_animal(self, animal):
        if not hasattr(self, '_liste_animaux'):
            self._liste_animaux = []

        if len(self._liste_animaux) >= self._capacite_max:
            return f"Capacité max atteinte ({self._capacite_max})"
        
        self._liste_animaux.append(animal)
        return f"{animal.nom} ajouté à {self.nom}"

    def enleve_animal(self, animal):
        if animal in self._liste_animaux:
            self._liste_animaux.remove(animal)
            return f"{animal.nom} retiré de l'enclos"
        return "Animal non présent"

    def afficher_animal(self):
        if not hasattr(self, '_liste_animaux') or not self._liste_animaux:
            return f"L'enclos {self._nom} est vide"
        
        resultat = f"Enclos {self._nom}({len(self._liste_animaux)}/{self._capacite_max})\n"
        resultat += "=" * 50 + "\n"
        for animal in self._liste_animaux:
            resultat += animal.afficher_etat() + "\n\n"
        return resultat

    def passer_jour(self):
        """
        Simuler le passage d'une journée
        """
        if not hasattr(self, '_liste_animaux') or not self._liste_animaux:
            return f"L'enclos {self.nom} est vide"

        resultat = f"\nPassage d'une journée dans {self.nom}\n"
        resultat += "-" * 42 + "\n"

        for animal in self._liste_animaux:
            if animal._en_vie:
                animal._appetit = min(100, animal._appetit + 35)
                animal._satisfaction = max(0, animal._satisfaction - 25)

                resultat += f"{animal.nom} => Appétit = {animal._appetit}/100 | Satisfaction => {animal.satisfaction - 25}/100\n"

                if animal._appetit >= 95 or animal._satisfaction <= 5:
                    animal._en_vie = False
                    resultat += f"{animal.nom} est tombé malade ou est mort..."
            else:
                resultat += f"{animal.nom} est déjà mort\n"

        resultat += "-" * 42 + "\n"
        return resultat

    # Endregion