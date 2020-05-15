#doublons_list
def doublons_list(ma_list):
	t_mp=[]
	for i in ma_list:
	 	if i not in t_mp:
	 		t_mp.append(i)
	 		t_mp.sort()
	return t_mp

#programme principale 
l=[5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
lm=doublons_list(l)
print(lm)