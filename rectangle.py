class Rectangle:
    """Ceci est la classe Rectangle."""

    def __init__(self, long=0.0, larg=0.0, coul="blanc"):
        """Initialisation d'un objet.

        Définition des attributs avec des valeurs par défaut.
        """
        self.longueur = long
        self.largeur = larg
        self.couleur = coul

    def calcule_surface(self):
        """Méthode qui calcule la surface."""
        return self.longueur * self.largeur

    def change_carre(self, cote):
        """Méthode qui transforme un rectangle en carré."""
        self.longueur = cote
        self.largeur = cote

    def calcul_perimetre(self):
        """ Méthode sui calcule le perimetre """
        return 2*(self.longueur+self.largeur)

if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe Rectangle.
    rectangle = Rectangle(30,50,"rouge")
    surface = rectangle.calcule_surface()
    print(" la largeur {} , la longueur {} d'une surface de {} et la couleur {} "\
        .format(rectangle.largeur , rectangle.longueur , surface , rectangle.couleur))
    rectangle.change_carre(30)
    surface1 = rectangle.calcule_surface()
    pourtour = rectangle.calcul_perimetre()
    print(" la largeur {} , la longueur {} d'une surface de {} qui a un perimetre de {} et la couleur est {} "\
        .format(rectangle.largeur , rectangle.largeur , surface1 , pourtour , rectangle.couleur))
    


