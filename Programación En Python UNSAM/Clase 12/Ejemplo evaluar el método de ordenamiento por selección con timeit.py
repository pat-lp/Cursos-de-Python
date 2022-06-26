'''
------------------------------------------------------------------------------
Ejemplo: evaluar el método de ordenamiento por selección con timeit
------------------------------------------------------------------------------
'''
import matplotlib.pyplot as plt
import numpy as np
import random
import timeit as tt



def ord_seleccion(lista):
    '''Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


def generar_lista(N):
    '''
    Genera listas de largo y contenido aleatorio, de largo entre
    1 y 256 y contenido con números enteros entre 1 y 1000.
    '''
    return [random.randint(1, 1000) for i in range(N)]

    
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []

    global lista
    
    listas =[generar_lista(N) for N in range(1, 256)]
    
    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)

    return tiempos_seleccion



listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
    

tiempos_seleccion = experimento_timeit_seleccion(listas, 100)


plt.plot(tiempos_seleccion)
plt.show()