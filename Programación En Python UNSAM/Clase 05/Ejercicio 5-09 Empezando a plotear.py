'''
-------------------------------------------------------------------------------
Ejercicio 5.09: Empezando a plotear
-------------------------------------------------------------------------------
Escribí una función plotear_temperaturas() en un archivo plotear_temperaturas.py 
que lea el archivo de datos temperaturas.npy (debería tener las 999 mediciones 
simuladas que creaste recién) y haga un histograma de las temperaturas simuladas.
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