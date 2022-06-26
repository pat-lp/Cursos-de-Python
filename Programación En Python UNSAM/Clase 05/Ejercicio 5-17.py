'''
-------------------------------------------------------------------------------
Ejercicio 5.17: Ejercicios con paquetes
-------------------------------------------------------------------------------
Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
-------------------------------------------------------------------------------
'''

import random
import numpy as np

def crear_paquete(figus_total):
    paquete=np.linspace(random.randint(1,figus_total)-1,random.randint(1,figus_total)-1,num=5,dtype=np.int64)
    return paquete
    
def comprar_paquete(figus_total,figus_paquete):
    return [random.randint(1,figus_total)-1 for i in range(figus_paquete)]


figus_total=670 #tamaño del album
figus_paquete=5 #cantidad de figuritas por paquete
print("----------------------------------------------")
print("Paquete--> ",comprar_paquete(figus_total, figus_paquete))
print("----------------------------------------------")