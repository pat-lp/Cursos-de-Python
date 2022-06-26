'''
------------------------------------------------------------------------------
Ejercicio 6-14: Búsqueda binaria
------------------------------------------------------------------------------
Modificando la función busqueda_binaria(lista, x) adecuadamente, definí una 
función donde_insertar(lista, x) de forma que reciba una lista ordenada y un 
elemento y devuelva la posición de ese elemento en la lista (si se encuentra 
en la lista) o la posición donde se podría insertar el elemento para que la 
lista permanezca ordenada (si no está en la lista).
Por ejemplo: el elemento 3 podría insertarse en la posición 2 en la 
lista [0,2,4,6] para mantenerla ordenada. Por lo tanto, el llamado 
donde_insertar([0,2,4,6], 3) deberá devolver 2, al igual que el llamado 
donde_insertar([0,2,4,6], 4).
------------------------------------------------------------------------------
'''
#Complejidad logaritmo de cantidad de elementos
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada, recorre de izq a der
    Poscondición:
        - Devuelve -1 si x no está en lista;
        - Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista,x):
    '''
    Reciba una lista ordenada y un elemento y devuelva la posición de ese 
    elemento en la lista (si se encuentra en la lista) o la posición donde 
    se podría insertar el elemento para que la lista permanezca ordenada 
    (si no está en la lista).
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        if lista[medio] > x:
            pos= medio
        else: 
            pos= medio+1
    return pos


lista=[1,3,5]
print(f"Lista {lista} elemento 0,  en posición: ",donde_insertar(lista, 0))
print(f"Lista {lista} elemento 1,  en posición: ",donde_insertar(lista, 1))
print(f"Lista {lista} elemento 5,  en posición: ",donde_insertar(lista, 5))
print(f"Lista {lista} elemento 4,  en posición: ",donde_insertar(lista, 4))
lista2=[1]
print(f"Lista {lista2} elemento 5,  en posición: ",donde_insertar(lista2, 1))
print(f"Lista {lista2} elemento 5,  en posición: ",donde_insertar(lista2, 3))
lista3=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print(f"Lista {lista3} elemento 18,  en posición: ", donde_insertar(lista3,18))

lista4= [0,2,4,6] 
print(f"Lista {lista4} elemento 3,  en posición: ",donde_insertar(lista3, 3))
print(f"Lista {lista4} elemento 4,  en posición: ",donde_insertar(lista3, 4))

#%% CLASE YOUTUBE


def donde_insertar_binaria(lista,x,verbose=True):
    '''
    Insertar ordenada binaria
    Precondición: lista ordenada
    Poscondición:
        - devuelve la posición donde insertar x para que lista siga ordenada.
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break #corta el ciclo cuando lo encuentra
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if not(izq <= der):
        pos=izq
    return pos

lista=[1,3,5]
print(f"Lista {lista} elemento 0,  en posición: ",donde_insertar_binaria(lista, 0))
print(f"Lista {lista} elemento 1,  en posición: ",donde_insertar_binaria(lista, 1))
print(f"Lista {lista} elemento 5,  en posición: ",donde_insertar_binaria(lista, 5))
print(f"Lista {lista} elemento 4,  en posición: ",donde_insertar_binaria(lista, 4))
lista2=[1]
print(f"Lista {lista2} elemento 5,  en posición: ",donde_insertar_binaria(lista2, 1))
print(f"Lista {lista2} elemento 5,  en posición: ",donde_insertar_binaria(lista2, 3))
lista3=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print(f"Lista {lista3} elemento 18,  en posición: ", donde_insertar_binaria(lista3,18))

lista4= [0,2,4,6] 
print(f"Lista {lista4} elemento 3,  en posición: ",donde_insertar_binaria(lista3, 3))
print(f"Lista {lista4} elemento 4,  en posición: ",donde_insertar_binaria(lista3, 4))
