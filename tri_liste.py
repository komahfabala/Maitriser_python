#tri_liste

def tri_function(ma_list):
	tmp = []
	k=0
	while  len(ma_list)>0:
		val1 = min(ma_list)
		ma_list.remove(val1)
		tmp.append(val1)
		
	return tmp
#programme principal

k = [8, 3, 12.5, 45, 25.5, 52, 1]
res = tri_function(k)
print (" la liste triée ", res)