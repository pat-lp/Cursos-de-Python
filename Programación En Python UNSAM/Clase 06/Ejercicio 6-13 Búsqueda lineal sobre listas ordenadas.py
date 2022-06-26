'''
------------------------------------------------------------------------------
Ejercicio 6-13: Búsqueda lineal sobre listas ordenadas
------------------------------------------------------------------------------
Modificá la función busqueda_lineal(lista, e) de la Sección 4.2 para el caso de 
listas ordenadas, de forma que la función pare cuando encuentre un elemento mayor a e. 
Llamá a tu nueva función busqueda_lineal_lordenada(lista,e) y guardala en el archivo 
busqueda_en_listas.py.
------------------------------------------------------------------------------
'''

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos


def busqueda_lineal_lordenada(lista, e):
    '''Función que pare cuando encuentre un elemento mayor a e, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z > e:   # si encontramos a e
            pos = z  # guardamos su posición
            break    # y salimos del ciclo
    return pos


print("-----------------------------------------")
print("BÚSQUEDA BINARIA SOBRE LISTAS ORDENDADAS")
print("-----------------------------------------")
lista=[1, 4, 54, 3, 0, -1]
lista.sort()

print("Elemento de la lista mayor a 44 es: ",busqueda_lineal_lordenada(lista, 44))

print("Elemento de la lista mayor a 3 es: ",busqueda_lineal_lordenada(lista, 3))

print("Elemento de la lista mayor a 0 es: ",busqueda_lineal_lordenada(lista, 0))

print("Elemento de la lista mayor a 42 es: ",busqueda_lineal_lordenada([], 42))

#%% CLASE YOUTUBE

def busqueda_lineal_v1(lista,x, verbose=True):
    '''
    Búsqueda lineal ordenada
    Precondición:
    Poscondición:
        - devuelve p tal que lista[p]==x, si está en lista;
        - devuelve -1 si x no está en lista.
    '''
    if verbose:
        print(lista,x)
        
    pos=-1
    for idx, elem in enumerate(lista):
        if elem==x:
            pos=idx
            
        if verbose:
            print(lista,idx,pos)
            
    return pos

lista_ejemplo=[1,3,5,7,9,11,13,15,17,19,21,23]
lista_2=[0,2,4,6]

busqueda_lineal_v1(lista_ejemplo,19,True)


#%% CLASE YOUTUBE


def busqueda_lineal_v2(lista,x, verbose=True):
    '''
    Búsqueda lineal ordenada
    Precondición: La lista está ordenada
    Poscondición:
        - devuelve p tal que lista[p]==x, si está en lista;
        - devuelve -1 si x no está en lista.
    '''
    if verbose:
        print(lista,x)
        
    pos=-1
    for idx, elem in enumerate(lista):
        if elem==x:
            pos=idx
            
        if verbose:
            print(lista,idx,pos)
            
        if elem>=x: #Sale de la búsqueda si no encuentra el elemento ó si lo encontró
            break
        
    return pos

def donde_insertar_lineal(lista, x, verbose=True):
    '''
    Precondición: Lista ordenada
    Poscondición:
        - devuelve la posición donde insertar x para que lista siga ordenada.
        
    '''
    if verbose:
        print(lista,x)
        
    pos=-1
    for idx, elem in enumerate(lista):
            
        if verbose:
            print(lista,idx,pos)
            
        if elem>=x: #Sale de la búsqueda si no encuentra el elemento ó si lo encontró
            pos=idx   
            break
        
    return pos


lista_ejemplo=[1,3,5,7,9,11,13,15,17,19,21,23]
lista_2=[0,2,4,6]

busqueda_lineal_v2(lista_ejemplo,19,True)
donde_insertar_lineal(lista_ejemplo,2,True)