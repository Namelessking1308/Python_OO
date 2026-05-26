from .animal import Animal

class Elephant(Animal):

	def __init__(self, longueur_defense, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
		super().__init__(nom, appetit, satisfaction, en_vie, soigneur)
		self.__longueur_defense = longueur_defense

	@property
	def longueur_defense(self):
		return self.__longueur_defense
	
	@longueur_defense.setter
	def longueur_defense(self, value):
		if not isinstance(value, int):
			raise TypeError("LA valeur doit être un entier.")
		self.__longueur_defense = value
	
	def prendre_bain_de_boue(self):
		if not hasattr(self, 'nom'):
			return "[ERROR] Animal non défini ou MORT ! 😵"
		self.satisfaction += 30
		print(f"🛀 {self.nom} prend un bainde boue. \n"
				f"satisfaction : {self.satisfaction}")
	
	def aspire_eau(self):
		if not hasattr(self, 'nom'):
			return "[ERROR] Animal non défini ou MORT ! 😵"
		self.satisfaction += 10
		return (f"🍹 {self.nom} aspire de l'eau \n"
				f"satisfaction : {self.satisfaction}")

	def observer_environnement(self):
		return "Observe son environnement à travers ses defenses. 🐘"
	
	def faire_bruit(self):
		return f"{self.nom} Hurle avec sa trompe !!!!"

	def probabilite_deces(self):
		return (100 - self.appetit) / (max(1,self.longueur_defense / 100))