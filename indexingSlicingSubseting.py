import numpy as np
import random
random.seed(2)

suduku = np.random.randint(0,10,[9,9])
suduku[0:3,0:3] = 10
suduku[0:6,3:6] = 4
suduku[0:3,6:9] =3
suduku[3:6,0:3] =0
suduku[3:6,6:9] =8
suduku[3:6,3:6] = 9
suduku[6:9,0:3] = 7
suduku[6:9,6:9] = 2
print(suduku)
carre1=suduku[0:3,0:3] 
print(carre1)
valeurs , counts = np.unique(suduku,return_counts=True) #compte le nombre de repetition
for i,j in zip(valeurs[counts.argsort()],counts[counts.argsort()]): #tri du tableau des en fonction des occurences
    print("valeurs {} apparrait {}".format(i,j) )

