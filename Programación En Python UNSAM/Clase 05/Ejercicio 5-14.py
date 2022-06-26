'''
-------------------------------------------------------------------------------
Ejercicio 5.14: 
-------------------------------------------------------------------------------
Ejecutá n_repeticiones = 1000 veces la función anterior utilizando 
figus_total = 6 y guardá en una lista los resultados obtenidos en cada 
repetición. Con los resultados obtenidos estimá cuántas figuritas hay que 
comprar, en promedio, para completar el álbum de seis figuritas.
Ayuda: El comando np.mean(l) devuelve el promedio de la lista l.

¿Podés crear esta lista usando una comprensión de listas?
------------------------------------------------------------------------------
'''
import random
import numpy as np

def crear_album(figus_total):
    #Devuelve vector vacio
    return np.zeros(figus_total,dtype=int)

def album_incompleto(A):
    #Devuelve True si no está completo y False si está completo
    return np.any(A==0)


def comprar_figu(figus_total):
    album=crear_album(figus_total)
    album[random.randint(0, figus_total-1)]=1
    return np.where(album==1)[0][0]

def cuantas_figus(figus_total):
    cantidad=0
    resultado=True
    album=crear_album(figus_total)
    while resultado == True:
        cantidad+=1
        nro=random.randint(0, figus_total-1)
        if album[nro]==0:
            album[nro]=1
        else:
            album[nro]+=1
        if album_incompleto(album)==False:
            resultado=False
    return cantidad
    

n_repeticiones = 1000 
figus_total = 6 

promedio= np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)]) #devuelve el promedio de la lista l.
print(f"Se estimá que se necesitan comprar para completar un álbum de {figus_total} figuritas en {n_repeticiones} repeticiones, un promedio de {promedio:.2f} figuritas.")