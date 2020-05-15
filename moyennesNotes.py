#moyennesNotes

liste = []
with open("notes.txt" , "r") as filin :
	for lignes in filin :
		liste.append(float(lignes))
		#print(" {} \n".format(liste))
print(liste)
somme = 0
for val in liste:
	somme += val

my = somme/len(liste)
print(" la moyenne de l'etudiant est : {:.2f}  ".format(my))