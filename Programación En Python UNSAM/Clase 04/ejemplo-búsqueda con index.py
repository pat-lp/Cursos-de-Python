'''
-------------------------------------------------------------------------------
Ejercicio 4.01: Debugger
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''

def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.
    Si e está en lista devuelve el índice, de lo 
    contrario devuelve -1.'''
    if e in lista:
        pos= lista.index(e)
    else:
        pos= -1
    return pos


lista=[1,4,54,3,0,-1]


print(busqueda_con_index(lista, 1)) #0
print(busqueda_con_index(lista, -1)) #5
print(busqueda_con_index(lista, 3)) #3
print(busqueda_con_index(lista, 44)) #-1
print(busqueda_con_index([], 0)) #-1