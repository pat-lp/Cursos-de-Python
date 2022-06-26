'''
------------------------------------------------------------------------------
Contar la cantidad de operaciones de un algoritmo
------------------------------------------------------------------------------
Esta modificación de la función cuenta (y devuelve) además cuántas 
comparaciones (z == x) hace la función. Observá que devuelve un par de datos.
Si querés acceder a la posición podés usar busqueda_secuencial_(lista, x)[0] 
y para acceder a la cantidad de comparaciones que hizo 
busqueda_secuencial_(lista, x)[1].
------------------------------------------------------------------------------
'''
def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

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


lista=[1,2,3,4]
print(f"Posición del elemento 2 en la lista {lista}: ",busqueda_secuencial_(lista, 2)[0])#posición elemento
print(f"La cantidad de comparaciones para buscar al elemento 2 en la lista {lista} es de:",busqueda_secuencial_(lista, 2)[1])#cantidad de comparaciones