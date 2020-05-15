#frequenceAdn
import sys
def cal_composition(x) :
	l_base =["A","C","G","T"]
	l_res =[]
	for i in l_base:
		nb_re = str(x).count(i)
		l_res.append( float(nb_re))
	return l_res

#programme principal

valeur = sys.argv[1]
ma_list = cal_composition(valeur)
print(" la liste des frequences :" ,ma_list)