from models import Voiture, Garage

def main():
	voiture_1 = Voiture()
	voiture_2 = Voiture()

	voiture_1.definir_voiture("Honda", "Civic", "Noir", 2006, 86452)
	voiture_2.definir_voiture("Porsche", "Carerra", "Jaune", 2006, 26748)
	
	garage = Garage()

	garage.ajouter_voiture(voiture_1)
	garage.ajouter_voiture(voiture_2)

	print(garage.afficher_toutes_voitures())

	# print(voiture_1.demarrer())
	# print(voiture_2.demarrer())
	# print(voiture_1.demarrer())

if __name__ == "__main__":
	main()