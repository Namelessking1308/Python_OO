from models import Voiture, Garage

def main():
	voiture_1 = Voiture()
	voiture_2 = Voiture()

	voiture_1.definir_voiture("Honda", "Civic", "Noir", 2006, 86452)
	voiture_2.definir_voiture("Porsche", "Carerra", "Jaune", 2006, 26748)

	print("Getter")
	print(f"Couleur 	: {voiture_1.couleur}")		# Appelle le getter

	print("Setter")
	voiture_1.couleur = "rouge"
	print(f"Nouvelle couleur : {voiture_1.couleur}")
	try:
		voiture_1.couleur = 123
	except TypeError as e:
		print(f"[Erreur] {e}")


	# test des erreurs

if __name__ == "__main__":
	main()