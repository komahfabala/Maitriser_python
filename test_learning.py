import numpy as np

def initialisation(m,n) :
    """
        m nombre de colonne de la matrice
        n nombre de ligne de la matrice
        retourne une matrice aleatoire (m,n+1)
        #avec une colonne de biais(remplie de 1) tout a droite
    """
    mat_aleatoire= np.random.randn(m,n+1)
    mat_biais = np.ones((m,1))
    np.random.seed(0)
    mat_complet =np.concatenate((mat_aleatoire,mat_biais),axis=1)
    return mat_complet
if __name__ == "__main__":
    tes= initialisation(5,4)
    print(tes)