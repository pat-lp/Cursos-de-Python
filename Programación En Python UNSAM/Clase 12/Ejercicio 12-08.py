'''
------------------------------------------------------------------------------
Ejercicio 12.8
------------------------------------------------------------------------------
La idea de este ejercicio es, nuevamente, comparar los algoritmos de 
ordenamiento que vimos hasta ahora pero usando timeit() en lugar de contando a 
mano la cantidad de operaciones.
Juntá en el archivo time_ordenamiento.py los métodos de búsqueda del Ejercicio 
12.7.
Escribí un experimento que, tal como hiciste en el Ejercicio 12.5, para N 
entre 1 y 256 genere una lista de largo N con números enteros del 1 al 1000, 
calcule el tiempo que tarda cada método en ordenar la lista y guarde estos 
resultados en vectores de largo 256.
En este caso, vas a tener que generar y guardar todas las listas a ser 
utilizadas antes de correr el experimento, para poder usar las mismas repetidas 
veces al evaluar cada método. Definí para eso una función generar_listas(Nmax) 
que genere una lista de listas, una de cada longitud entre 1 y Nmax, con 
valores aleatorios entre 1 y 1000.
Asegurate de evaluar todos los métodos de ordenamiento con las mismas listas 
(siempre usá copias para no ordenar listas que ya están ordenadas) y guardar 
esta información para poder mostrarla o usarla.
Graficá los datos de tiempos de ejecución en función de las longitudes de las 
listas. ¿Coinciden las curvas con lo que habías predicho estimando el número 
de operaciones?
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



def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v


def ord_burbujeo(lista):
    '''
    Ordenamiento Burbujeo.
    Pre: Recibe una lista.
    Pos: Devuelve una lista ordenada.
    '''
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if (lista[j] > lista[j+1]):
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return lista



def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


def generar_lista(N):
    '''
    Genera listas de largo y contenido aleatorio, de largo entre
    1 y 256 y contenido con números enteros entre 1 y 1000.
    '''
    return [random.randint(1, 1000) for i in range(N)]


def experimento_timeit(Nmax):
    """
    Realiza un experimento usando timeit para evaluar los métodos
    de ordenamiento de listas con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'Nmax' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge_sort = []

    global lista
    
    listas =[generar_lista(N) for N in range(1, 256)]
    
    for lista in listas:

        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = Nmax, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = Nmax, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = Nmax, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = Nmax, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge_sort.append(tiempo_merge)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge_sort = np.array(tiempos_merge_sort)
    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge_sort

Nmax = 100
tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge_sort = experimento_timeit(Nmax)

plt.plot(tiempos_seleccion, color='black', label='Ord. Selección')
plt.plot(tiempos_insercion, color='crimson', label='Ord. Inserción')
plt.plot(tiempos_burbujeo, color='green', label='Ord. Burbujeo')
plt.plot(tiempos_merge_sort, color='blue', label='Ord. Merge Sort')
plt.title('Tiempo de ordenamiento: Selección, Inserción, Burbujeo y Merge Sort')
plt.xlabel('longitud listas')
plt.ylabel('tiempo de ejecución')
plt.show()
