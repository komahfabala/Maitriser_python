#sequenceComplementaire
sequence = [" A "," C "," G "," T "," T "," A "," G "," C "," T "," A "," A "," C "," G "]
print(sequence)
print()
print(" sequence Complementaire")
for i in sequence :
	if i == " A ":
		print(" T ", end= '     ')
		continue
	elif i == " T " :
		print(" A " , end='     ')
		continue
	elif i == " C " :
		print(" G " , end='     ')
		continue
	elif i== " G " :
		print(" C " , end='     ')
		continue
	print(i , end = '     ')
print()