from models import Soigneur, Elephant, Enclos, Girafe

def main():
	print("=" * 15)
	print("Correctif Exo_2")
	print("=" * 15 + "\n")

	# Création du soigneur
	soigneur = Soigneur()
	soigneur2 = Soigneur()
	
	print(soigneur.definir("Dr House","14/3/1975", 12))
	print(soigneur2.definir("Valentine","13/08/2000", 5))

	# Création des éléphants + lien avec les soigneur 
	babar = Elephant()
	print(babar.definir("Babar", appetit=40, satisfaction=80, soigneur=soigneur))

	dumbo = Elephant()
	print(dumbo.definir("Dumbo", appetit=70, satisfaction=50, soigneur=soigneur, ))

	sophie = Girafe()
	print(sophie.definir("Sophie",appetit= 50,satisfaction= 40, en_vie= True, soigneur= soigneur2, longueur_cou= 20))

	print()

	# Création de l'enclos + ajout des animaux
	savane = Enclos()
	print(savane.definir("Savane", 5, "Grand"))
	print(savane.ajouter_animal(dumbo))
	print(savane.ajouter_animal(babar))
	print()
	foret = Enclos()
	print(foret.definir("Foret", 20, "Géante"))
	print(foret.ajouter_animal(sophie))
	print()

	# Affichage
	print(savane.aficher_animaux())
	print(foret.aficher_animaux())

	# actions soigneur
	print(soigneur.nourrir(dumbo))
	print()
	print(soigneur.entretenir(babar))
	print()
	print(soigneur2.entretenir(sophie))
	print()

	print(f"Age soigneur : {soigneur.age}")
	print(f"Age soigneur : {soigneur2.age}")

	# L'éléphant mange tout seul
	print(dumbo.manger())
	print()

	# Bonus...
	print(savane.passer_jour())
	print(foret.passer_jour())
	print(savane.passer_jour())
	print(foret.passer_jour())
	print(savane.passer_jour())
	print(foret.passer_jour())
	print(savane.passer_jour())
	print(foret.passer_jour())


	# Affichage Final 👿

if __name__ == "__main__":
	main()