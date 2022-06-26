'''
------------------------------------------------------------------------------
Ejercicio 12.7
------------------------------------------------------------------------------
Modificá la función merge_sort para que también devuelva la cantidad de 
comparaciones hechas. Rehacé el último ejercicio de la sección anterior 
(Ejercicio 12.5) incorporando el merge sort a la comparación y al gráfico. 
Describí con tus palabras qué observas.
------------------------------------------------------------------------------
'''


import random 
import numpy as np
import matplotlib.pyplot as plt



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


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    compara = 0
    for i in range(len(lista) - 1):
        compara += 1
        if lista[i + 1] < lista[i]:
            compara += reubicar(lista, i + 1)
    return compara

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    compara = 0
    while j > 0 and v < lista[j - 1]:
        compara += 1
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return compara
    
    
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

#Modificado según lo explicado en clase de Youtube
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        compara=0
    else:
        medio = len(lista) // 2
        izq, compara_izq = merge_sort(lista[:medio])
        der, compara_der = merge_sort(lista[medio:])
        lista_nueva, comp= merge(izq, der)
        compara = compara_izq + compara_der + comp
    return lista_nueva, compara

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    compara = 0
    while(i < len(lista1) and j < len(lista2)):
        compara += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado = resultado + lista1[i:]
    resultado = resultado + lista2[j:] 
    return resultado, compara



def lista_aleatoria(N):
    '''
    Genera listas de largo y contenido aleatorio, de largo entre
    1 y 256 y contenido con números enteros entre 1 y 1000.
    '''
    return [random.randint(1, 1000) for i in range(N)]


def grafico_comparaciones(vector_burbujeo, vector_insercion, vector_seleccion, vector_merge_sort, Nmax):
    '''
    Genera un gráfico con las comparaciones de tres ordenamientos.
    Pre: Recibe cuatro vectores.
    Pos: Devuelve un gráfico.
    '''
    plt.figure(figsize=(12,6))
    x = np.arange(1,Nmax+1, 1)
    plt.plot(x, vector_burbujeo, color='green', linestyle='--', linewidth= 8, label='Ord. Burbujeo')
    plt.plot(x, vector_insercion,  color='crimson', linestyle='--',linewidth= 6, label='Ord. Inserción', alpha=0.5)
    plt.plot(x, vector_seleccion,  color = 'black', linewidth= 3, linestyle='-',label = 'Ord. Selección')
    plt.plot(x, vector_merge_sort, color = 'blue', linestyle='-', linewidth=2.5, label = 'Ord. Merge Sort',alpha=0.5)
    plt.title('Cantidad de comparaciones por tipo de ordenamiento')
    plt.grid('y')
    plt.xlabel('longitud lista')
    plt.ylabel('cantidad comparaciones')
    plt.ylim(0,30000)
    plt.xlim(0, 270)
    plt.legend(loc='upper left')
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
    comparaciones_merge_sort = np.empty(Nmax, dtype="int")
    
    for N in range(1, Nmax): 
        lista = lista_aleatoria(N)
        num = ord_burbujeo(lista)[0]
        comparaciones_burbujeo[N] = num
        comparaciones_insercion[N] = ord_insercion(lista)
        comparaciones_seleccion[N] = ord_seleccion(lista)
        comparaciones_merge_sort[N] = merge_sort(lista)[1]
    grafico_comparaciones(comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion,comparaciones_merge_sort, Nmax)
    return  comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion, comparaciones_merge_sort


def f_principal():
    Nmax = 256
    print(experimento_vectores(Nmax))
    
if __name__ == '__main__':
    f_principal()


