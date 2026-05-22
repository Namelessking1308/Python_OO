from models import Elephant, Soigneur, Enclos

def main():
    print("=" * 15)
    print("Correctif Exo 1")
    print("=" * 15 + "\n")

    # Création du soigneur
    soigneur = Soigneur()

    print(soigneur.definir("Dr House", "14/03/1975", 12))

    # Création des éléphants + lien avec les soigneurs 
    babar = Elephant()
    print(babar.definir("Babar", appetit = 40, satisfaction = 80, soigneur = soigneur))

    dumbo = Elephant()
    print(dumbo.definir("Dumbo", appetit = 70, satisfaction = 50, soigneur = soigneur))

    print()

    # Création de l'enclos + ajout des animaux

    savane = Enclos()
    print(savane.definir("Savane", 5, "Grand"))
    print(savane.ajouter_animal(dumbo))
    print(savane.ajouter_animal(babar))
    print()

    # Affichage

    print(savane.afficher_animal())

    # Actions soigneur

    print(soigneur.nourir(dumbo))
    print()
    print(soigneur.entretenir(babar))
    print()

    # L'éléphant mange tout seul

    print(dumbo.manger())
    print()

    # Bonus...

    print(savane.passer_jour())
    print(savane.passer_jour())
    print(savane.passer_jour())
    print(savane.passer_jour())

    # Affichage Final

if __name__ == "__main__":
    main()