# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 20:23:06 2021

@author: Patricia
"""

'''
------------------------------------------------------------------------------
Ejercicio Búsqueda binaria vs. búsqueda secuencial
------------------------------------------------------------------------------
'''

import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_binaria(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve la cantidad de comparaciones que hace la función.
    '''
    
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps=0
    while izq <= der:
        comps+=1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,comps

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    '''
    Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''
     Devuelve un elemento aleatorio entre 0 y m-1.
    '''
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    '''
    Da la cantidad de comparaciones promedio en k experimentos elementales,
    en un experimento de búsqueda secuencial.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    '''
    Da la cantidad de comparaciones promedio en k experimentos elementales,
    en un experimento de búsqueda binaria.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]
    comps_prom = comps_tot / k
    return comps_prom

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)


plt.plot(largos,comps_promedio_binario, label ='Búsqueda Binaria')
plt.plot(largos, comps_promedio_secuencial, label ='Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.ylim(0,100)
plt.xscale("log")
plt.legend(loc ="upper left")
plt.show()