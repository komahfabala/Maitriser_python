#admisRecale

with open("notes.txt", "r") as fichier1 , open("admisRecale.txt", "w") as fichier2 :
	for lignes in fichier1:
		if float(lignes) < 10:
			fichier2.write( "racalé "+ lignes )
		elif float(lignes) >= 10 :
			fichier2.write("admis" + lignes)

with open("admisRecale.txt", "r") as filin :
	for lignes in filin:
		print(" {} \n".format(lignes))