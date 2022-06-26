'''
-------------------------------------------------------------------------------
Ejercicio 4.03 y 4.04: Búsqueda de elementos y búsqueda de máximo y mínimo
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

def maximo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.'''
    # m guarda el máximo de los elementos a medida que recorro la lista.
     # Lo inicializo en 0
    m="Lista Vacía"
    if len(lista) > 0:
        m = -99999
        for e in lista:
            if e > m:
                m = e
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.'''
    # m guarda el máximo de los elementos a medida que recorro la lista.
     # Lo inicializo en 0
    m="Lista Vacía"
    if len(lista) > 0:
        m = 99999
        for e in lista:
            if e < m:
                m = e
    return m

#Función main con las pruebas realizadas de las funciones
def main():
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
    print("\n--------------------------------------------------------")
    print("\n\n")
    print("\n--------------------------------------------------------")
    print("{:^55}".format('MÁXIMO'))
    print("--------------------------------------------------------")
    print("El elemento 'máximo' en la lista[1,2,7,2,3,4] es: {}".format(maximo([1,2,7,2,3,4]))) #7
    print("El elemento 'máximo' en la lista[1,2,3,4] es:     {}".format(maximo([1,2,3,4]))) #4
    print("El elemento 'máximo' en la lista[-5,4] es:        {}".format(maximo([-5,4]))) #4
    print("El elemento 'máximo' en la lista[-5,-4] es:      {}".format(maximo([-5,-4]))) #-4
    print("El elemento 'máximo' en la lista[] es:        {}".format(maximo([]))) #Lista Vacía
    print("--------------------------------------------------------")
    print("\n")
    print("--------------------------------------------------------")
    print("{:^55}".format('MÍNIMO'))
    print("--------------------------------------------------------")
    print("El elemento 'mínimo' en la lista[1,2,7,2,3,4] es: {}".format(minimo([1,2,7,2,3,4]))) #1
    print("El elemento 'mínimo' en la lista[0,1,2,3,4] es:   {}".format(minimo([0,1,2,3,4]))) #0
    print("El elemento 'mínimo' en la lista[-5,4] es:       {}".format(minimo([-5,4]))) #-5
    print("El elemento 'mínimo' en la lista[-5,-4] es:      {}".format(minimo([-5,-4]))) #-5
    print("El elemento 'mínimo' en la lista[] es:        {}".format(minimo([]))) #Lista Vacía
    print("--------------------------------------------------------")
    return "Fin función main()"

#print(main())


