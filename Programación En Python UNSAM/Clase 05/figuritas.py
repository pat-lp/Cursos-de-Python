'''
-------------------------------------------------------------------------------
Ejercicio "figuritas"
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
    
def experimento_figus(n_repeticiones, figus_total):
    promedio= np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return promedio

#Función para probar lo realizado
def main():
    n_repeticiones=100
    figus_total=670
    promedio= experimento_figus(n_repeticiones, figus_total)
    return(f"Se estimá que se necesitan comprar para completar un álbum de {figus_total} figuritas en {n_repeticiones} repeticiones, un promedio de {promedio:.1f} figuritas.")
    
#print(main())