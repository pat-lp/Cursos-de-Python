'''
-------------------------------------------------------------------------------
Ejercicio 4.04: Búsqueda de máximo y mínimo
-------------------------------------------------------------------------------
Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque el 
valor máximo de una lista de números positivos. Python tiene el comando max que 
ya hace esto, pero como práctica te proponemos que completes el siguiente 
código:
-------------------------------------------------------------------------------
'''

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

print("\n--------------------------------------------------------")
print("{:^55}".format('MÁXIMO'))
print("--------------------------------------------------------")
print("El elemento 'máximo' en la lista[1,2,7,2,3,4] es: {}".format(maximo([1,2,7,2,3,4]))) #7
print("El elemento 'máximo' en la lista[1,2,3,4] es:     {}".format(maximo([1,2,3,4]))) #4
print("El elemento 'máximo' en la lista[-5,4] es:        {}".format(maximo([-5,4]))) #4
print("El elemento 'máximo' en la lista[-5,-4] es:      {}".format(maximo([-5,-4]))) #-4
print("El elemento 'máximo' en la lista[] es:        {}".format(maximo([]))) #Lista Vacía
print("--------------------------------------------------------")
print("\n\n")
print("--------------------------------------------------------")
print("{:^55}".format('MÍNIMO'))
print("--------------------------------------------------------")
print("El elemento 'mínimo' en la lista[1,2,7,2,3,4] es: {}".format(minimo([1,2,7,2,3,4]))) #1
print("El elemento 'mínimo' en la lista[0,1,2,3,4] es:   {}".format(minimo([0,1,2,3,4]))) #0
print("El elemento 'mínimo' en la lista[-5,4] es:       {}".format(minimo([-5,4]))) #-5
print("El elemento 'mínimo' en la lista[-5,-4] es:      {}".format(minimo([-5,-4]))) #-5
print("El elemento 'mínimo' en la lista[] es:        {}".format(minimo([]))) #Lista Vacía
print("--------------------------------------------------------")