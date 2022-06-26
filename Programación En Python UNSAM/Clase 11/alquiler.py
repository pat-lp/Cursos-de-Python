'''
-------------------------------------------------------------------------------
Ejercicio 11.14: precio_alquiler ~ superficie
-------------------------------------------------------------------------------
Usando la función que definimos antes, ajustá los datos con una recta.
Graficá los datos junto con la recta del ajuste.
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
Una forma de cuantificar cuán bien ajusta la recta es considerar el promedio de 
los errores cuadráticos, llamado error cuadrático medio.

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
Calculá el error cuadrático medio del ajuste que hiciste recién.
-------------------------------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

minx = min(superficie)
maxx = max(superficie)

a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

plt.scatter(x = superficie, y = alquiler, color ='green')
plt.plot(grilla_x, grilla_y, color =  'black')
plt.title('Precio alquiler mensual departamentos \nen el Bo. de Caballito(CABA), y sus superficies')
plt.xlabel('superficie(metros cuadrados)')
plt.ylabel('precio(miles de pesos)')
plt.show()

print()
print('Error cuadrático medio')
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
