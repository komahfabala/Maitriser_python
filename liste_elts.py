#boucle for et while 

lisete = ["vache" , " souris" , "levure" , " bactterie"]

for x in lisete:
	print(x)
print(" fin de la lisete avec for1 ") ;
#avec for en core en utilisant range

for x in range(4):
	print(lisete[x])
print(" deuxieme exemple for2") ;
#avec while
i = 1
while i < len(lisete):
			print(lisete[i]) ; i = i+1