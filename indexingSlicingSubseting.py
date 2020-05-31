import numpy as np
import random
random.seed(2)

suduku = np.ones((9,9))
suduku[0:3,0:3] = 10
suduku[0:6,3:6] = 4
suduku[0:3,6:9] =3
suduku[3:6,0:3] =0
suduku[3:6,6:9] =8
suduku[3:6,3:6] = 9
suduku[6:9,0:3] = 7
suduku[6:9,6:9] = 2
print(suduku)