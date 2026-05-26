class Voiture:
	"""
	Classe Voiture
	"""
	nombre_voitures = 0 		# Attribut de classe
	
	def definir_voiture(self, marque, modele, couleur, annee, kilometrage):
		"""
		Méthode pour initialiser les attributs (remplace le constructeur)
		"""
		self.marque = marque
		self.modele = modele
		self.couleur = couleur
		self.annee = annee
		self.kilometrage = kilometrage
		self.est_demarre = False

		Voiture.nombre_voitures += 1

		print("nombre voiture(s) :", Voiture.nombre_voitures)

	def demarrer(self):
		if not hasattr(self, 'est_demarre'):
			return "[Erreur] Veuillez d'abord définir la voiture avec définir_voiture()"
		if not self.est_demarre:
			self.est_demarre = True
			return f"[Succès] {self.marque} {self.modele} à démarré !"
		return f"[Succès] {self.marque} {self.modele} est déjà démarré !"

	def arreter(self):
		pass

	def rouler(self):
		pass

	def afficher_info(self):
		if not hasattr(self, 'marque'):
			return "voiture non définie."
		return f"🏎️  {self.marque} {self.modele}"

	def __str__(self):
		if hasattr(self, 'marque'):
			return f"{self.marque}"
		return "Voiture (non définie)"