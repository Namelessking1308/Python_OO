from models import Voiture, Garage

def main():
    voiture_1 = Voiture()
    garage = Garage()
    voiture_1.definir_voiture("Ford", "Mustang", "Noir", 2025, 15000)
    garage.ajouter_voiture(voiture_1)
    print(garage.afficher_toutes_voitures())

    print(voiture_1.demarrer())

if __name__ == "__main__":
    main()