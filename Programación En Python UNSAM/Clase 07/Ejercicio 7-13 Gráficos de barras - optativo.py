# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
Ejercicio 7.13: Gráficos de barras
-------------------------------------------------------------------------------
Modificá el siguiente código para generar un gráfico similar al que se muestra: 
tenés que agregar etiquetas para las barras rojas cuidando la alineación del 
texto.
-------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

n = 12 
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va='bottom')
plt.ylim(-1.25, +1.25)

#%% SOLUCION PAGINA

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va= 'bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='right', va= 'top')

plt.xlim(-.5, n)
plt.xticks([])
plt.ylim(-1.25, 1.25)
plt.yticks([])

plt.show()