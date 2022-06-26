'''
-------------------------------------------------------------------------------
Ejercicio 5.13: Cantidad de compras
-------------------------------------------------------------------------------
Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum 
(figus_total), genere un álbum nuevo, simule su llenado y devuelva la cantidad 
de figuritas que se debieron comprar para completarlo.
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
    

figus_total=6
cantidad=cuantas_figus(figus_total)

print(f"Se necesitaron para llenar un album de {figus_total} figuritas una cantidad de {cantidad} figuritas para completarlo")
