#compositionAcideAnime compte le nombre d'occurence de chaque acide amine
import sys
def  compositionAcideAnime(ma_ch):
	if len(sys.argv) != 2:
		print(" Usage : il faut exactement deux arguments <nomProgramme > < chaine_de_caractere> " )
	mon_dict = dict()
	occur =0
	for x in range(len(ma_ch)):
		occur = ma_ch.count(ma_ch[x]) 
		mon_dict[ma_ch[x]] = occur
	return mon_dict


def  affiche_mon_dict(mon_dict1):
	for key in mon_dict1:
		print(key, mon_dict1[key])

#programme principale

val = sys.argv[1]
mD= compositionAcideAnime(val)
affiche_mon_dict(mD)