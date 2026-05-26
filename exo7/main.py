from models import Soigneur, Elephant, Enclos, Girafe, Animal, Outils

def declancher_bruit(animal):
	print(animal.faire_bruit())

def main():
	print("=" * 15)
	print("Correctif Exo_4")
	print("=" * 15 + "\n")

	# Création du soigneur
	soigneur = Soigneur("Dr House", "14/3/1975", 12)

	# Création des éléphants + lien avec les soigneur 
	babar = Elephant(25, "Babar", appetit=40, satisfaction=80, soigneur=soigneur)

	dumbo = Elephant(30, "Dumbo", appetit=70, satisfaction=50, soigneur=soigneur)

	print()

	sophie = Girafe(150, "Soph", appetit=50, satisfaction=80, soigneur=soigneur)

	print()

	print(dumbo.aspire_eau())

	print(dumbo.faire_bruit())

	print(sophie.manger_feuilles())

	print(sophie.faire_bruit())

	print(babar.observer_environnement())

	Outils.pauses(3)

	# Création de l'enclos + ajout des animaux
	savane = Enclos("Savane", 5, "Grand")
	print(savane)
	print(savane.ajouter_animal(dumbo))
	print(savane.ajouter_animal(babar))
	print()

	# Affichage
	print(savane.aficher_animaux())

	# actions soigneur
	print(soigneur.nourrir(dumbo))
	print()
	print(soigneur.entretenir(babar))
	print()

	print(f"Age soigneur : {soigneur.age}")

	# L'éléphant mange tout seul
	print(dumbo.manger())
	print()

	# Bonus...
	print(savane.passer_jour())
	print(savane.passer_jour())
	print(savane.passer_jour())
	print(savane.passer_jour())

	# Affichage Final 👿

	# print(dumbo.declancher_bruit())

	Outils.clear_console()

if __name__ == "__main__":
	main()