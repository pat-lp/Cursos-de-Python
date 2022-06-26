'''
-------------------------------------------------------------------------------
Ejercicio 4.03: Búesquedas de un elemento
-------------------------------------------------------------------------------
En este primer ejercicio tenés que escribir una función buscar_u_elemento() que 
reciba una lista y un elemento y devuelva la posición de la última aparición de 
ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
-------------------------------------------------------------------------------
'''

def buscar_u_elemento(lista,e):
    i =  0
    pos =  -1
    while i < len(lista):
        if lista[i] == e:
            pos= i
        i+= 1
    return pos

def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de veces que aparece el 
    elemento en la lista'''
    i =  0
    cont=0
    while i < len(lista):
        if lista[i] == e:
            cont+=1
        i+= 1
    return cont
    

print("--------------------------------------------------------")
print("{:^55}".format('BUSCAR U ELEMENTOS'))
print("{:^55}".format('[1,2,3,2,3,4]'))
print("--------------------------------------------------------")
print("El elemento '{}' se encuentra en las pos: {} (-1 si no está)".format(1,buscar_u_elemento([1,2,3,2,3,4],1)))
print("El elemento '{}' se encuentra en las pos: {} (-1 si no está)".format(2,buscar_u_elemento([1,2,3,2,3,4],2)))
print("El elemento '{}' se encuentra en las pos: {} (-1 si no está)".format(3,buscar_u_elemento([1,2,3,2,3,4],3)))
print("El elemento '{}' se encuentra en las pos: {} (-1 si no está)".format(5,buscar_u_elemento([1,2,3,2,3,4],5)))

print("--------------------------------------------------------")
print("{:^55}".format('BUSCAR N ELEMENTOS'))
print("{:^55}".format('[1,2,3,2,3,4]'))
print("--------------------------------------------------------")
print("El elemento '{}' se encuentra repetido: {} número de veces".format(1,buscar_n_elemento([1,2,3,2,3,4],1)))
print("El elemento '{}' se encuentra repetido: {} número de veces".format(2,buscar_n_elemento([1,2,3,2,3,4],2)))
print("El elemento '{}' se encuentra repetido: {} número de veces".format(3,buscar_n_elemento([1,2,3,2,3,4],3)))
print("El elemento '{}' se encuentra repetido: {} número de veces".format(5,buscar_n_elemento([1,2,3,2,3,4],5)))