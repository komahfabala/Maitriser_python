a=1 ; b=1 ; x =a+b ; print(x) 
nom = " komah "
prenom = " Mohamed " 
#affichage
print(" {1} , {0} " .format(nom , prenom)) 
artiste = [" Arafatdj " ,  "supect95" , "mixpremier" , " magic-system" , " tchekoubou " , " beynaud " , " yode-siro" ]; print("artiste =" , artiste)
animaux = [" giraf" , " tigre " , " lyon " , " elephant " , " pantere" , " lievre " , " python " , " heron "] ; print("animaux =" , animaux[0:4])


def carre_nombre(nb) :
    va = nb **2
    return   va
if __name__ == "__main__":
    k=carre_nombre(8)
    print(k)