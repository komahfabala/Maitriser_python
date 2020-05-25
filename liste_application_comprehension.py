import time

valeur_debut = time.time()

liste_test = [i**2 for i in range(10) ] #liste comprehension
nestead_liste = [[i+2 for i in range(20)] for j in range(5)] #des listes qui contiennent d'autre liste

valeur_fin = time.time()
print(liste_test)
print(nestead_liste)
print(valeur_debut - valeur_fin)

