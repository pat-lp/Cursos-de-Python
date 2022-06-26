'''
-------------------------------------------------------------------------------
Ejercicio 7.15: Setear el color de un scatter plot
-------------------------------------------------------------------------------
Modificá el código que sigue para generar un gráfico similar al que se muestra, 
prestando atención a los límites, el tamaño de las marcas, el color, y la 
transparencia de los trazos.
-------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)

#%% SOLUCION PAGINA

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])

plt.show()