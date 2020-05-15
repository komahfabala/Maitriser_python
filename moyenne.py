#moyenne avec affichage a deux chiffres pres

moyenne = [14,9,6,8,12]
valeur = 0
for x in moyenne:
	valeur +=x 
moy = valeur/len(moyenne)
print(" la moyenne {:.2f} ".format(moy))