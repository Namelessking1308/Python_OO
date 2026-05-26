from .animal import Animal

	# region Attributs

class Elephant(Animal):

    def definir(self, nom, appetit, satisfaction, en_vie, soigneur):
        super().definir(nom , appetit, satisfaction, en_vie , soigneur)

        return f"Éléphant {nom} créé"

    # endregion

    # region Methodes

    def manger(self):
        if not hasattr(self, 'nom') or not self.en_vie:
            return "[Erreur] Éléphant non défini ou mort..."

        self.appetit = max(0, self.appetit - 25)
        self.satisfaction = min(100, self.satisfaction + 15)

        return (f"🍉 {self.nom} a mangé. \n"
                f"    Appétit 		 : {self.appetit}/100\n"
                f"    Satisfaction   : {self.satisfaction}/100")

    def passe_le_temps(self):
        self.appetit = max(0, self.appetit - 15)
        self.satisfaction = min(100, self.satisfaction - 25)

    def decede(self):
        self.en_vie = False
        return f"😵 {self.nom} est tombé malade ou est mort...\n"
    
    def prendre_bain_de_boue(self):
        return f"{self.nom} prend un bain de boue..."
    
    def aspirer_eau(self):
        return f"{self.nom} aspire de l'eau !"

    # endregion