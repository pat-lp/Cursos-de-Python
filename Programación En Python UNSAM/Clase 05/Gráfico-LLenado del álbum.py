

import random
import numpy as np
import matplotlib.pyplot as plt

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


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
