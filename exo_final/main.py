from models import Chanson, Jouable, Podcast, Publicite, Genre

def main():
    
    playliste1 = Chanson("Hasta la vista", "PNL", 3, Genre.RAP.value)

    playliste1.jouer()

if __name__ == "__main__":
    main()