#compteurDeLigne
import sys
import os

#teste sur le nombre d'argument

if len(sys.argv) !=2:
	sys.exit(" Error: il faut exactement deux arguments")
nom_fichier =sys.argv[1]

#test si le fichier existe

if os.path.exists(nom_fichier):
	print(" le fichier existe  donc le script continu ")
else :
	sys.exit(" le fichier n'existe pas dans l'ordinateur ")

taille = 0

with open(nom_fichier , "r") as f_in:
	taille = len(f_in.readlines())
print(" {} contient {} lignes. ".format(nom_fichier , taille))
