from models import Chanson, Jouable, Podcast, Publicite, Genre, Playliste

def main():
    
    chanson1 = Chanson("Hasta la vista", "PNL", 3, Genre.RAP.value)

    podcast1 = Podcast("Horreur dans la cuisine", "Mkskayz", 45)

    playliste1 = Playliste("Été")

    playliste1.ajouter_piste(chanson1)

    playliste1.lire_playliste()

    chanson1.jouer()
    print()
    podcast1.jouer()

if __name__ == "__main__":
    main()