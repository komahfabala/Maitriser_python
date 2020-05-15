#nombreMystere
import sys
def  nombreMystere(ma_chaine):
	if len(sys.argv) != 2:
		print(" usage : il faut exactement deux arguments <nombreMystere> et <argument>")
	l_tmp = []
	nombreMystere =0
	trouver =0
	k=0
	if (len(ma_chaine) ==3) and (int(ma_chaine) < 300) and (int(ma_chaine)%2 ==0):
		for i in ma_chaine:
			l_tmp.append(int(i))
		for x in l_tmp:
			nombreMystere +=x
			if nombreMystere ==7 :
				if  l_tmp[0] ==  l_tmp[1] or l_tmp[0] == l_tmp[2] or l_tmp[1] == l_tmp[2]:
					trouver = ma_chaine ;
					print(" vous avez trouver bravo!!!!!!!")
	else:
		print(" vous n'avez pas trouver le nombre ")
	return trouver


#programme principal
chaine= sys.argv[1]
mystere =nombreMystere(chaine)
print(" le nombre mystere est {}".format(mystere))