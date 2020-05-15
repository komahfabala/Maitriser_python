#produit de nombres consecutif

liste_elts = list(range(2,20,2))
print(liste_elts)
#la liste vide pour le produit 

liste_produit =[]

for x in range(len(liste_elts)):
	k=liste_elts[x]
	liste_produit.append(k*(liste_elts[x]+2))
	print(liste_produit)