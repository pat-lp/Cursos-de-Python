'''
-------------------------------------------------------------------------------
Ejercicio 5.18: Ejercicios con paquetes
-------------------------------------------------------------------------------
Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el 
tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, 
simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
-------------------------------------------------------------------------------
'''

import random
import numpy as np

def crear_album(figus_total):
    #Devuelve vector vacio
    return np.zeros(figus_total,dtype=int)

def album_incompleto(A):
    #Devuelve True si no está completo y False si está completo
    return np.any(A==0)



def crear_paquete(figus_total):
    paquete=np.linspace(random.randint(1,figus_total)-1,random.randint(1,figus_total)-1,num=5,dtype=np.int64)
    return paquete
    
def comprar_paquete(figus_total,figus_paquete):
    return [random.randint(1,figus_total)-1 for i in range(figus_paquete)]


def cuantos_paquetes(figus_total,figus_paquete):
    cantidad=0
    resultado=True
    album=crear_album(figus_total)
    while resultado == True:
        cantidad+=1
        paquete=comprar_paquete(figus_total, figus_paquete)
        for i,x in enumerate(paquete):
            if np.where(album==x) and album[i]==1:
                album[x-1]+=1
            else:
                album[x-1]=1
        if album_incompleto(album)==False:
            resultado=False
    return cantidad

figus_total=670 #tamaño del album
figus_paquete=5 #cantidad de figuritas por paquete

print(f"Cantidad de paquetes con '{figus_paquete}' figuritas necesarios para completar un album de '{figus_total}'--> ",cuantos_paquetes(figus_total, figus_paquete))
