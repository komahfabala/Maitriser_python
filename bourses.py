def filtrer(src, dst):
    """Fonction de traitement.
 
    Lit et traite ligne par ligne le fichier source (src).
    Le résultat est écrit au fur et à mesure dans le
    fichier destination (dst). 
    """
    # Lit l'en-tête, élimine la fin de ligne, et extrait les 
    # champs séparés par une virgule
    entete = src.readline().rstrip('\n\r').split(",")
    print(entete)
    # Détermine l'index des différents champs qui nous sont utiles
    dateidx = entete.index("Date")
    advcloseidx = entete.index("Adj Close")
    closeidx = entete.index("Close")
    openidx = entete.index("Open")
 
    # Ecrit l'en-tête
    dst.write("Date,Adj Close,Direction\n")
 
    # Puis les données
    for ligne in src:
        # Extraction des données de la ligne séparées par une virgule
        donnees = ligne.rstrip('\n\r').split(",")
 
        if donnees[closeidx] > donnees[openidx]:
            direction = 1
        elif  donnees[closeidx] < donnees[openidx]:
            direction = -1
        else:
            direction = 0
 
        # Ecriture des données dans le fichier destination
        dst.write("%s,%s,%s\n" % (donnees[dateidx], donnees[advcloseidx], direction))
#----------------- methode main-------------------------------------------------------------------------------------
def main() :
    # Ouverture du fichier source
    source = open("bourse.csv", "r")
    
    # Ouverture du fichier destination
    destination = open("result_bourse.txt", "w")
    
    try:
        # Appeler la fonction de traitement
        filtrer(source, destination)
    finally:
        # Fermeture du fichier destination
        destination.close()
    
        # Fermerture du fichier source
        source.close()
if __name__ == "__main__":
    main()