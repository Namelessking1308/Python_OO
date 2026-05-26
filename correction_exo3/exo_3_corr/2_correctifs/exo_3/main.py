from models import Soigneur, Elephant, Enclos, Girafe, Animal

def main():
	print("=" * 15)
	print("Correctif Exo_2")
	print("=" * 15 + "\n")

	# Création du soigneur
	soigneur = Soigneur()
	
	print(soigneur.definir("Dr House","14/3/1975", 12))

	# Création des éléphants + lien avec les soigneur 
	babar = Elephant()
	print(babar.definir(25, "Babar", appetit=40, satisfaction=80, soigneur=soigneur))

	dumbo = Elephant()
	print(dumbo.definir( 30, "Dumbo", appetit=70, satisfaction=50, soigneur=soigneur))

	print()

	sophie = Girafe()
	print(sophie.definir(150, "Soph", appetit=50, satisfaction=80, soigneur=soigneur))

	print()

	print(dumbo.aspire_eau())

	print(sophie.manger_feuilles())

	print(babar.observer_environnement())

	# Création de l'enclos + ajout des animaux
	savane = Enclos()
	print(savane.definir("Savane", 5, "Grand"))
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

if __name__ == "__main__":
	main()