'''
-------------------------------------------------------------------------------
Ejercicio 11.13: Hojas ISO y recursión
-------------------------------------------------------------------------------
Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor 
que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente 
a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. 
La función debe devolver el ancho y el largo -en ese orden- en una tupla.
-------------------------------------------------------------------------------
'''


def  medidas_hoja_A(N):
    '''
    Calcula las medidas de una hoja ISO
    Pre: Entrada N mayor que cero, usando la hoja A0 como caso base.
    Pos: Devuelve ancho y largo en una tupla.
    '''
    mm_ancho = 841
    mm_largo = 1189
    
    if N == 0:
        return mm_ancho, mm_largo
    mm_ancho, mm_largo = medidas_hoja_A(N-1)
    if N % 2 == 0:
        mm_ancho //= 2 
        mm_largo = mm_largo
    else:
        mm_ancho = mm_ancho
        mm_largo //= 2
    return mm_ancho, mm_largo



def f_principal():
    N = 1
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')#(841, 594)
    
    N = 2
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')# (420, 594)
    
    N = 5
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')# (210, 148)
    
    N = 6
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')#(105, 148)
    
    N = 8
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')# (52, 74)
    
    N = 9
    print(f'Hoja A{N}: {medidas_hoja_A(N)}')# (52, 37)

if __name__=='__main__':
    f_principal()
