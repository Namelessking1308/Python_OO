from .animal import Animal

class Girafe(Animal):

	def __init__(self, longueur_cou,  nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
		super().__init__(nom, appetit, satisfaction, en_vie, soigneur)
		self.__longueur_cou = longueur_cou

		
	@property
	def longueur_cou(self):
		return self.__longueur_cou
	
	@longueur_cou.setter
	def longueur_cou(self, value):
		if not isinstance(value, int):
			raise TypeError("La longueur du cou doit être un nombre.")
		if value < 1:
			raise ValueError("La valeur doit être de minimum 1.")
		self.__longueur_cou = value 

	def manger_feuilles(self):
		if not hasattr(self, 'nom'):
			return "[ERROR] Animal non défini ou MORT ! 😵"
		self.appetit += 10
		self.satisfaction += 10
		return(f"🌿 {self.nom} mange des feuilles \n"
			f"Appetit : {self.appetit} \n"
			f"Satifaction : {self.satisfaction}")
	
	def boire_eau(self):
		if not hasattr(self, 'nom'):
			return "[ERROR] Animal non défini ou MORT ! 😵"
		self.satisfaction += 5
		return(f"🚰 {self.nom} boit de l'eau \n"
			f"Satisfaction : {self.satisfaction}")

	def observer_environnement(self):
		return "Observe son environnement de trèèèèèèèès haut ! 🏢"
	
	def faire_bruit(self):
		return f"{self.nom} Hurle avec son cou !!!!"