import numpy as np
import random

liste_elmt = [list(i*j for i in range(5)) for j in range(5)]
arr1 = np.array([[1,2,4],[7,8,9],[8,9,4]])
arr2D = np.array([[1,2,3,4,5],[6, 7, 8, 9, 10],[96,45,23,12,1]])
print('indexing :',arr1[2,-1])
print(arr2D[:, 0])
"""
    Vérifiez si Array possède ses données
    Comme mentionné ci-dessus, les copies sont propriétaires des données, et les vues ne sont pas propriétaires des données 
    mais comment pouvons-nous le vérifier ?
    Chaque tableau NumPy a une base d'attributs qui renvoie None si le tableau possède les données.
    Sinon, l'attribut base fait référence à l'objet original. 
"""
arr3 = np.array([1, 2, 3, 4, 5])
x = arr3.copy() # copie le tableau et ensuite on peut modifier l'original
y = arr3.view() # copie , si on modifie le tableau d'original et la copie aussi est modifié 
print('verif du copie et view : \n',x.base)
print(y.base) 
#shape
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('utilisation du shape :',arr4.shape) 
#reshape
"""
        Convertissez le tableau 1-D suivant de 12 éléments en un tableau 3-D.
        La dimension la plus extérieure aura 2 tableaux qui contiennent 3 tableaux, chacun avec 2 éléments :
"""
arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr =arr5.reshape(2, 3, 2)
print('utilisation du reshape : \n',newarr)

"""
    mauvaise façon de faire 
"""
"""
arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr6:
  for y in x:
    for z in y:
      print(z) 

"""
"""
    mieux
   nditer() permet de parcourir un tableau a plusieur dimension sans ecrire plus de boucle 
"""
arr_test = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr_test):
  print(x) 

arr_enu = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr_enu): #affiche l'indice de chaque element du tableau numpy
  print(idx, x) 
print("****************")
arr7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr7[:, ::2]): # iterer avec un pas de 2 mais on ne peut pas faire d'operation sur l'element
     print(x)
gerate_rand = np.random.randint(100,size=(5,4)) 
print(gerate_rand[0:3,0:2])
print("******************************************")
mon_arr =  np.array([[["me","ta","mon","ma"],["ton","votre","notre","leur"]],[["mes","tes","ses","tes"],["le","la","lui","leurs"]]])
print(mon_arr[1:2,0:4])
print(mon_arr.shape)
nouv_arr = mon_arr.reshape(4,4) # il faut que le nombre de lignes soit divisible par le nombre d'element 16/4=4 d'ou => (4,4) 
print(" changement de dimension en matrice 4x4 \n",nouv_arr) 
nouv2_arr = mon_arr.reshape(2,2,4)
print("changement de dimension en un tableau en 2Dimension : \n", nouv2_arr)