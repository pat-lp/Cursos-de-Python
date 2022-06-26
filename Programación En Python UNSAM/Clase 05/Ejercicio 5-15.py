'''
-------------------------------------------------------------------------------
Ejercicio 5.15: 
-------------------------------------------------------------------------------
Escribí una función llamada experimento_figus(n_repeticiones, figus_total) 
que simule el llenado de n_repeticiones álbums de figus_total figuritas y 
devuelva el número estimado de figuritas que hay que comprar, en promedio, 
para completar el álbum.

Para esto, una posibilidad es que la función experimento_figus() llame a la 
función cuantas_figus() tantas veces como lo indica el parámetro n_repeticiones 
y guarde los resultados parciales en una lista, a partir de la cual luego 
realice el promedio.

Guardá todo lo que hiciste hasta aquí sobre figuritas en un archivo figuritas.py para el cierre de la clase. Lo que sigue profundiza un poco más en el asunto.

¿Cuánto te da para 100 repeticiones en un álbum de 670 figuritas?
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
    album[random.randint(1, figus_total)-1]=1
    return np.where(album==1)[0][0]

def cuantas_figus(figus_total):
    cantidad=0
    resultado=True
    album=crear_album(figus_total)
    while resultado == True:
        cantidad+=1
        nro=random.randint(1, figus_total)-1
        if album[nro]==0:
            album[nro]=1
        else:
            album[nro]+=1
        if album_incompleto(album)==False:
            resultado=False
    return cantidad
    
def experimento_figus(n_repeticiones, figus_total):
    promedio= np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)]) #devuelve el promedio de la lista l.
    return promedio


n_repeticiones=100
figus_total=670
promedio= experimento_figus(n_repeticiones, figus_total)

print(f"Se estimá que se necesitan comprar para completar un álbum de {figus_total} figuritas en {n_repeticiones} repeticiones, un promedio de {promedio:.1f} figuritas.")
    