'''
-------------------------------------------------------------------------------
Ejemplo: el modelo de cuadrados mínimos
-------------------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])

minx = min(x)
maxx = max(x)

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = x, y = y, color='blue')
plt.plot(grilla_x, grilla_y, color =  'green')
plt.title('scatterplot de los datos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


