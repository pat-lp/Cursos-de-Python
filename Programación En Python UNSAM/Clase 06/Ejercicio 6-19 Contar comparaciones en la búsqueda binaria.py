'''
------------------------------------------------------------------------------
Ejercicio 6.19: Contar comparaciones en la búsqueda binaria
------------------------------------------------------------------------------
Modificá el código de búsqueda binaria (busqueda_binaria(lista, x)) introducido 
en la Sección 6.5, de forma que devuelva (además de la posición del elemento 
en la lista) la cantidad de comparaciones que realizó el algoritmo para 
encontrarlo o decidir que no está.
------------------------------------------------------------------------------
'''

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


print("Posición de un elemento en la lista y cantidad de comparaciones")
print("-----------------------------------------------------------------")

lista=[1,3,5]
x=0
print(f"Lista {lista} elemento {x}--> posisión:{busqueda_binaria(lista, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista, x)[1]}")
x=5
print(f"Lista {lista} elemento {x}--> posisión:{busqueda_binaria(lista, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista, x)[1]}")
x=4
print(f"Lista {lista} elemento {x}--> posisión:{busqueda_binaria(lista, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista, x)[1]}")
x=1
print(f"Lista {lista} elemento {x}--> posisión:{busqueda_binaria(lista, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista, x)[1]}")

lista2=[1]
x=1
print(f"Lista {lista2} elemento {x}--> posisión:{busqueda_binaria(lista2, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista2, x)[1]}")
x=3
print(f"Lista {lista2} elemento {x}--> posisión:{busqueda_binaria(lista2, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista2, x)[1]}")

lista3=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
x=18
print(f"Lista {lista3} elemento {x}--> posisión:{busqueda_binaria(lista3, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista3, x)[1]}")

lista4= [0,2,4,6] 
x=3
print(f"Lista {lista4} elemento {x}--> posisión:{busqueda_binaria(lista4, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista4, x)[1]}")
x=4
print(f"Lista {lista4} elemento {x}--> posisión:{busqueda_binaria(lista4, x)[0]} - cantidad de comparaciones:{busqueda_binaria(lista4, x)[1]}")

