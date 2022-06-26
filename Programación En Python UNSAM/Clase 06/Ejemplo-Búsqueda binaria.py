
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
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


busqueda_binaria([1, 3, 5], 0, verbose = True)
print()
busqueda_binaria([1, 3, 5], 1, verbose = True)
print()
busqueda_binaria([1, 3, 5], 2, verbose = True)
print()
busqueda_binaria([1, 3, 5], 3, verbose = True)
print()
busqueda_binaria([1, 3, 5], 5, verbose = True)
print()
busqueda_binaria([1, 3, 5], 6, verbose = True)
print()
busqueda_binaria([1], 1, verbose = True)
print()
busqueda_binaria([1], 3, verbose = True)
print()
busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True)