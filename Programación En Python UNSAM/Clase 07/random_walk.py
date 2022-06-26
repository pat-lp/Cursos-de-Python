'''
-------------------------------------------------------------------------------
Ejercicio 7.12: "random walk"
-------------------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint (-1,2,largo)
    return pasos.cumsum()

N = 100000
maxi = -9999
mini = 100000
cantidad_trayectorias = 12
colores = ['royalblue','orange','grey','pink','tomato','aqua','brown','darkgreen','gold','purple','magenta','blue']


plt.subplot(2, 1, 1)
for i in range(cantidad_trayectorias):
    trayectorias = randomwalk(N)
    array = np.array(trayectorias)
    
    minimo = np.amin(array)
    if minimo < mini:
        mini = minimo
        caminata_menos_lejos = array
       
    maximo = np.amax(array)
    if maximo > maxi:
        maxi = maximo
        caminata_mas_lejos = array
  
    plt.plot(array, color = colores[i])

plt.title('12 caminatas al azar')
plt.ylabel('distancia al origen', fontsize=10)
plt.xlabel('tiempo', fontsize=10)
plt.xticks([]), plt.yticks([])
plt.yticks([-500.0, 0, +500.0])
plt.ylim(-1000.0, 1000.0)

#Espacio entre gráfico  de 12 caminatas y los otros subplots
plt.subplots_adjust(hspace=0.5)

#Espacio entre los subplots de caminata más lejos y menos lejos
plt.subplots_adjust(wspace=0.3)

plt.subplot(2, 2, 3)
plt.plot(caminata_mas_lejos, color='royalblue')
plt.xticks([]), plt.yticks([])
plt.yticks([-500.0, 0, +500.0])
plt.ylim(-1000.0, 1000.0)
plt.title('La caminata que más se aleja', fontsize=10)


plt.subplot(2, 2, 4)
plt.plot(caminata_menos_lejos, color='royalblue')
plt.xticks([]), plt.yticks([])
plt.yticks([-500.0, 0, +500.0])
plt.ylim(-1000.0, 1000.0)
plt.title('La caminata que menos se aleja', fontsize=10)

plt.show()
