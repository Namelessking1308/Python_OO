class Elephant:

    def caractéristiques_elephant(self, nom, appetit, satisfaction, en_vie, soigneur):
        self.nom = nom
        self.appetit = appetit
        self.satisfaction = satisfaction
        self.en_vie = True
        self.soigneur = soigneur

        print(f"--L'animal {self.nom}--\n{self.appetit}/100 d'appétit\n{self.satisfaction} de satisfaction\n{self.en_vie} en vie\nSon soigneur est {self.soigneur}")

    def manger(self):
        if self.appetit <= 50:
            return f"{self.nom} à faim... il lui reste {self.appetit} d'appétit"
        return f"{self.nom} n'a plus faim !"