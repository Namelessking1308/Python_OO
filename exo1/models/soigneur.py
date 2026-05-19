from .elephant import Elephant

class Soigneur:

    def personnage(self, nom, date_naissance, experience, nombre_animaux_responsable):
        self.nom = nom
        self.date_naissance = date_naissance
        self.experience = experience
        self.nombre_animaux_responsable = nombre_animaux_responsable

        

    def nourir(self, elephant : Elephant):
        if elephant.appetit <= 50 and not elephant.appetit >= 100:
            elephant.appetit += 10
            return f"{elephant.nom} a manger, {elephant.appetit}/100"
        else:
            return f"{elephant.nom} n'a pas besoin de manger"

    def entretenir(self, elephant : Elephant):
        if elephant.satisfaction <= 50 and not elephant.satisfaction >= 100:
            elephant.satisfaction += 10
            return f"{elephant.nom} est satisfait {elephant.satisfaction}/100"
        else:
            return f"{elephant.nom} n'a pas besoin d'être nettoyé"