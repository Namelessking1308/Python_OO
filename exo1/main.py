from models import Elephant, Enclos, Soigneur

def main():
    elephant1 = Elephant()
    enclos1 = Enclos()
    soigneur1 = Soigneur()

    elephant1.caractéristiques_elephant("Roger", 50, 100, True, "Pierre") 
    soigneur1.personnage("Pierre", "13-08-2000", "5 ans", "Roger")
    enclos1.Caracteristique_enclos("Enclos à éléphant", 5, "10 km", "Roger")
    print(elephant1.manger())
    print(soigneur1.nourir(elephant1))
    print(elephant1.manger())
    print(soigneur1.entretenir(elephant1))
    print(enclos1.enleve_animal(elephant1))
    print(enclos1.afficher_animal(elephant1))
    
if __name__ == "__main__":
    main()