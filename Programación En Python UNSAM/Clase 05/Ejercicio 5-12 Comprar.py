'''
-------------------------------------------------------------------------------
Ejercicio 5.12: Comprar
-------------------------------------------------------------------------------
Alguna de las funciones que introdujimos en la Sección 5.2 sirve para devolver 
un número entero aleatorio dentro de un rango (¿cuál era?). Implementá una 
función comprar_figu(figus_total) que reciba el número total de figuritas que 
tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero 
aleatorio que representa la figurita que nos tocó.
------------------------------------------------------------------------------
'''

import random
import numpy as np

def crear_album(figus_total):
    #Devuelve vector vacio
    return np.zeros(figus_total,dtype=int)

def comprar_figu(figus_total):
    #Devuelve el número de figurita que nos tocó
    album=crear_album(figus_total)
    album[random.randint(0, figus_total-1)]=1
    return np.where(album==1)[0][0]


figus_total=670
print("Figurita en el album: ",comprar_figu(figus_total))


