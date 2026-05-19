class Voiture:
    """
    Classe Voiture
    """
    nombre_voiture = 0

    def definir_voiture(self, marque, modele, couleur, annee, kilometrage):
        """
        Méthode pour initialiser les attributs (remplace le constructeur)
        """
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.kilometrage = kilometrage
        self.est_demarrer = False

        Voiture.nombre_voiture += 1

        print(f"le nombre de voiture: {Voiture.nombre_voiture}")

    def demarrer(self):
        if not hasattr(self, 'est_demarrer'):
            return "*Erreur*\nVeuillez d'abord définir la voiture avec definir_voiture."
        
        if not self.est_demarrer:
            self.est_demarrer = True
            return f"*Succès*\n{self.marque} {self.modele} a démarré !"
        return f"*Succès*\n{self.marque} {self.modele} est déjà démarré !"
    
    def arreter(self):
        pass

    def rouler(self):
        pass

    def afficher_info(self):
        if not hasattr(self, 'marque'):
            return "Voiture non définie"
        return f"{self.marque} {self.modele}"

    def __str__(self):
        if hasattr(self, 'marque'):
            return f"{self.marque}"
        return "Voiture non définie."