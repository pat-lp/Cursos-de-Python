'''
------------------------------------------------------------------------------
Ejercicio 12.2: burbujeo
------------------------------------------------------------------------------
COMPLEJIDAD: La idea básica del ordenamiento de la burbuja es recorrer el conjunto 
de elementos en forma secuencial varias veces. Cada paso compara un elemento del 
conjunto con su sucesor (x[i] con x[i+i]), e intercambia los dos elementos si 
no están en el orden adecuado.
Este algoritmo es poco eficiente puesto que existen n-1 pasos y n-i 
comprobaciones en cada paso, aunque es mejor que el algoritmo de ordenamiento 
por intercambio.
En el peor de los casos cuando los elementos están en el orden inverso, el 
número máximo de recorridos es n-1 y el número de intercambios o comparaciones 
está dado por (n-1) * (n-1) = n² - 2n + 1.En el mejor de los casos cuando los 
elementos están en su orden, el número de recorridos es mínimo 1 y el ciclo de 
comparaciones es n-1.
La complejidad del algoritmo de la burbuja es O(n²).
------------------------------------------------------------------------------
'''

def ord_burbujeo(lista):
    '''
    Ordenamiento Burbujeo.
    Pre: Recibe una lista.
    Pos: Devuelve una lista ordenada.
    '''
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            #comparamos el valor actual con el siguiente
            #Si el actual es mayor, entonces intercambios actual con el sigui
            if (lista[j] > lista[j+1]):
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return lista


def f_principal():
    lista_1 = [1, 2, -3, 8, 1, 5]
    lista_2 = [1, 2, 3, 4, 5]
    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    lista_4 = [10, 8, 6, 2, -2, -5]
    lista_5 = [2, 5, 1, 0]
    
    print(ord_burbujeo(lista_1))
    print(ord_burbujeo(lista_2))
    print(ord_burbujeo(lista_3))
    print(ord_burbujeo(lista_4))
    print(ord_burbujeo(lista_5))

if __name__=='__main__':
    f_principal()
