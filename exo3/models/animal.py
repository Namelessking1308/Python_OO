class Animal:
    
	#region Attributs

	def definir(self, nom, appetit=50, satisfaction=50, en_vie=True, soigneur=None):
		self.__nom = nom
		self.__appetit = max(0, min(100, appetit))
		self.__satisfaction = max(0, min(100, satisfaction))
		self.__en_vie = en_vie
		self.__soigneur = soigneur

	#endregion

	#region Prop's

	@property
	def nom(self):
		return self.__nom

	@nom.setter
	def nom(self, value):
		if not isinstance(value, str):
			raise TypeError("Le mot doit être une chaine")
		self.__nom = value

	@property
	def appetit(self):
		return self.__appetit
	
	@appetit.setter
	def appetit(self, value):
		self.__appetit = value

	@property
	def satisfaction(self):
		return self.__satisfaction
	
	@satisfaction.setter
	def satisfaction(self, value):
		self.__satisfaction = value

	@property
	def en_vie(self):
		return self.__en_vie

	@property
	def soigneur(self):
		return self.__soigneur

	@soigneur.setter
	def soigneur(self, value):
		self.__soigneur = value

	#endregion

	# Region Méthodes

	def afficher_etat(self):
		if not hasattr(self, 'nom'):
			return "[Erreur] Animal non défini..."
		etat = "Vivant" if self.en_vie else "Mort"
		soigneur_nom = self.soigneur.nom if self.soigneur else "Aucun"

		return (f" {self.nom}\n"
				f"    Appétit 		 : {self.appetit}/100\n"
				f"    Satisfaction   : {self.satisfaction}/100\n"
				f"    État   		 : {etat}\n"
				f"    Soigneur  	 : {soigneur_nom}")
	
	def laver(self, soigneur=None):
		if not hasattr(self, 'satisfaction') or not self.en_vie:
			return "[Erreur] Éléphant non défini ou mort..."

		if soigneur:
			self.satisfaction = min(100, self.satisfaction + 30)
			return (f"💧 {self.nom} est lavé par {soigneur.nom} \n"
                    f"    Satisfaction   : {self.satisfaction}/100")
		else:
			self.satisfaction = min(100, self.satisfaction + 15)
			return (f"💦 {self.nom} se lave \n"
                    f"    Satisfaction   : {self.satisfaction}/100")

	#endregion