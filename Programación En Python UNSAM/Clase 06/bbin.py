'''
------------------------------------------------------------------------------
Ejercicio "bbin"
------------------------------------------------------------------------------
'''
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

def insertar(lista, x):
    '''
     Recibe una lista ordenada y un elemento. Si el elemento se encuentra en 
     la lista solamente devuelve su posición; si no se encuentra en la lista, 
     lo inserta en la posición correcta para mantener el orden, también debe 
     devolver su posición.
     '''
    pos=donde_insertar(lista, x)
    if x not in lista:
        lista.insert(pos, x)
    return pos


def main():
    '''
    Función main() creada para probar lo realizado.
    '''
    print("-------------------------------------------------")
    print("{:^50s}".format('LISTA, ELEMENTO Y POSICIÓN'))
    print("-------------------------------------------------")
    lista=[1,3,5]
    print(f"Lista {lista} elemento 0,  en posición: ",insertar(lista, 0))
    print(f"Lista {lista} elemento 1,  en posición: ",insertar(lista, 1))
    print(f"Lista {lista} elemento 2,  en posición: ",insertar(lista, 2))
    print(f"Lista {lista} elemento 3,  en posición: ",insertar(lista, 3))
    print(f"Lista {lista} elemento 5,  en posición: ",insertar(lista, 5))
    print(f"Lista {lista} elemento 4,  en posición: ",insertar(lista, 4))
    lista2=[1]
    print(f"Lista {lista2} elemento 1,  en posición: ",insertar(lista2, 1))
    print(f"Lista {lista2} elemento 3,  en posición: ",insertar(lista2, 3))
    lista3=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    print(f"Lista {lista3} elemento 18,  en posición: ", insertar(lista3,18))
    return "Fin de la función main()"

#print(main())