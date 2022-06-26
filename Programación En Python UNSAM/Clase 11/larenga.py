'''
-------------------------------------------------------------------------------
Ejercicio 11.9: Pascal
-------------------------------------------------------------------------------
El triángulo de Pascal es un arreglo triangular de números que se define de la 
siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los 
valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los 
valores que se encuentran en los bordes del triángulo son todos unos. Cualquier 
otro valor se calcula sumando los dos valores contiguos de la fila de arriba.
Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra 
en la fila n y la columna k. 
-------------------------------------------------------------------------------
'''

def pascal(n, k):
    '''
    Calcula el valor que se encuentra 
    en la fila(n) y la columna(k), en un arreglo triangular.
    Pre: n y k son números positivos.
    Pos: Devuelve el valor en la columna y fila indicados.
    '''
    if (n== k or k==0): #Caso base
        return 1
    else:
        pascal1 = pascal(n - 1, k-1)
        pascal2 = pascal(n - 1, k)
        return pascal1 + pascal2


def f_principal():
    print(pascal(3, 1))#3
    print(pascal(5, 2))#10
    
if __name__== '__main__':
    f_principal()

