#lectureSequence
import sys
import os

def lit_fasta() :
	if len(sys.argv) != 2 :
		sys.exit(" error : il faut exactement deux arguments pour lancer le script ")
	nom_fichier = sys.argv[1]
	if os.path.exists(nom_fichier):
		print(" {} !!!".format(nom_fichier))
	else :
		sys.exit(" le fichier n'existe pas dans l'ordinateur ")
	
	v=0
	with open(nom_fichier, "r") as lec_in :
		lg = lec_in.readline()
		while lg :
			lg = lec_in.readline()
			taille = len(lg)
			l_base = ["A","C","G","T"]
			for i in l_base:
				base = lg.count(i)
				v+=1
			print("la sequence contient {} bases ".format(v))
			print(" la longuer est {}".format(taille))	
			v=0
				
			
			

#programme principal

lit_fasta()