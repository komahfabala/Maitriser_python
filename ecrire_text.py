Pur_sang = []

with open("./Data_set_pyton/Equides.csv", "r",encoding="iso-8859-1") as fichier1 , open("fichier1.txt", "w") as fichier2 :
    tab=[]
    for lignes in fichier1:
        tab=lignes.split(";")
        if len(tab) != 8:
            continue
        if "PUR SANG" in tab[0] :
            Pur_sang.append(tab[0])
            Pur_sang.append(tab[1])
            fichier2.write( str(Pur_sang)+ lignes )
with open("fichier1.txt", "r") as filin :
	for lignes in filin:
		print(" {} \n".format(lignes))

