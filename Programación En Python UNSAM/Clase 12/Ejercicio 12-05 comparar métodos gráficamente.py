'''
------------------------------------------------------------------------------
Ejercicio 12.5: comparar métodos gráficamente
------------------------------------------------------------------------------
Vamos a tratar de comparar visualmente la cantidad de comparaciones que hacen 
estos algoritmos para diferentes largos de listas. Hacé un programa 
comparaciones_ordenamiento.py que para N entre 1 y 256 genere una lista de largo 
N con números enteros del 1 al 1000 en orden aleatorio, calcule la cantidad de 
comparaciones realizadas por cada método de ordenamiento y guarde estos 
resultados en tres vectores de largo 256: comparaciones_seleccion, 
comparaciones_insercion y comparaciones_burbujeo.

Graficá estos tres vectores. Si las curvas se superponen, graficá una de ellas 
con línea punteada para poder verlas bien. ¿Cómo dirías que crece la complejidad 
de estos métodos? ¿Para cuáles depende de la lista a ordenar y para cuáles 
solamente depende del largo de la lista?
------------------------------------------------------------------------------
'''


import random 
import numpy as np
import matplotlib.pyplot as plt


#ordenar por selección una lista de tamaño N insume tiempo del orden de N^2
def ord_seleccion(lista):
    '''Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    n = len(lista) - 1
    compara = 0
    while n > 0:
        compara += n
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return compara

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

#Ordenar por inserción una lista de tamaño N puede insumir (en el peor caso) tiempo del orden de N^2
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    compara = 0
    for i in range(len(lista) - 1):
        compara += 1
        if lista[i + 1] < lista[i]:
            reubica=reubicar(lista, i + 1)
            compara += reubica
    return compara

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    comparacion = 0
    while j > 0 and v < lista[j - 1]:
        comparacion += 1
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return comparacion
    
def ord_burbujeo(lista):
    '''
    Ordenamiento Burbujeo.
    Pre: Recibe una lista.
    Pos: Devuelve una lista ordenada.
    '''
    compara = 0
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            compara +=1
            if (lista[j] > lista[j+1]):
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return compara, lista

def lista_aleatoria(N):
    '''
    Genera listas de largo y contenido aleatorio, de largo entre
    1 y 256 y contenido con números enteros entre 1 y 1000.
    '''
    return [random.randint(1, 1000) for i in range(N)]


def grafico_comparaciones(vector_burbujeo, vector_insercion, vector_seleccion):
    '''
    Genera un gráfico con las comparaciones de tres ordenamientos.
    Pre: Recibe cuatro vectores.
    Pos: Devuelve un gráfico.
    '''
    plt.figure(figsize=(10,6))
    x = np.arange(1, Nmax+1, 1)
    plt.plot(x, vector_burbujeo,color='green', linestyle='--', linewidth= 6, label='Ord. Burbujeo')
    plt.plot(x, vector_insercion, color='black', linestyle='-',linewidth= 3, label='Ord. Inserción')
    plt.plot(x, vector_seleccion, color = 'cyan', linewidth= 1, linestyle='-',label = 'Ord. Selección')
    plt.title('Cantidad de comparaciones por tipo de ordenamiento')
    plt.grid('y')
    plt.xlabel('longitud lista')
    plt.ylabel('cantidad comparaciones')
    plt.legend(loc='lower right')
    plt.show()


def experimento_vectores(Nmax):
    '''
    Compara la cantidad de comparaciones de tres ordenamientos(Burbujeo, Inserción y Selección)
    Pre: genera listas de distintos largos entre 1 y Nmax, y calcula la 
        cantidad de comparaciones.
    Pos: Guarda los resultados en tres vectores de largo Nmax.
    '''
    
    comparaciones_seleccion = np.empty(Nmax, dtype="int")
    comparaciones_insercion = np.empty(Nmax, dtype="int")
    comparaciones_burbujeo = np.empty(Nmax, dtype="int")
    
    for N in range(1, Nmax): 
        lista = lista_aleatoria(N)
        num = ord_burbujeo(lista)[0]
        comparaciones_burbujeo[N] = num
        comparaciones_insercion[N] = ord_insercion(lista)
        comparaciones_seleccion[N] = ord_seleccion(lista)
    grafico_comparaciones(comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion)
    return  comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion

Nmax = 256
print(experimento_vectores(Nmax))



