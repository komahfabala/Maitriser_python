from numpy import random
import numpy as np
import matplotlib.pyplot as plt

dataSet = {f"experinece{i}" : random.randn(100) for i in range(5)} #nestead dict
liste_elmt = [list(random.randn(10)) for i in range(5)]
print(liste_elmt[1:3])

def graphique(dataSet_val) :
    plt.figure(figsize=(12,8))
    for k,i in zip(dataSet_val.keys(), range(1,len(dataSet_val)+1)):
        plt.subplot(len(dataSet_val),1,i)
        plt.plot(dataSet_val[k])
        plt.title(k)
    plt.show()

def main():
    graphique(dataSet)
if __name__ == "__main__":
    main()