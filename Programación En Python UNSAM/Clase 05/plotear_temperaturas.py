'''
-------------------------------------------------------------------------------
Ejercicio "plotear_temperaturas"
-------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas=np.load("../Data/temperaturas.npy")
    plt.hist(temperaturas,bins=10,color='green',edgecolor = 'black')
    plt.title('"HISTOGRAMA DE TEMPERATURAS SIMULADAS"')
    plt.xlabel("temperatura(°C)")
    plt.ylabel("Cantidad")
    plt.show()
    
    
plotear_temperaturas()