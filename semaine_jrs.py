#les jours de la semaine

semaine = [" lundi " , " mardi " , " mercredi " , " jeudi " , " vendredi " , " samedi " , " dimanche "] 
#affichage 
for i in range(len(semaine)):
	print( " jour   {} est {} ".format(i , semaine[i])) ;

#affichange avec le while 
print( "les jours du week-end :" ) ;
v= 5
while v < 7:
	print(semaine[v]); v = v+1  

