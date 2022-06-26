'''
------------------------------------------------------------------------------
Ejercicio 11.2: Números triangulares
------------------------------------------------------------------------------
Escribí una función triangular(n) que calcule recursivamente el n-ésimo número 
triangular (es decir, el número 1 + 2 + 3 + ... + n).
Fijate que este ejercicio es un caso particular de la función 
sumar_enteros(desde, hasta) que implementaste en el Ejercicio 7.8. La 
implementación que hiciste en el primer inciso de ese ejercicio es una forma 
de reemplazar la recursión por un ciclo. La implementación que hiciste en el 
segundo inciso es mucho más eficiente.
------------------------------------------------------------------------------
'''

def sumar_enteros_v2(desde, hasta): 
    '''Calcula la sumatoria de los números triangulares entre 1 y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde vale 1 y hasta es número entero y triangular.
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0

    '''
    nro_triangular=0
    nro_triangular=(hasta*(hasta+desde))//2
    return nro_triangular



desde=1
hasta=4
suma=sumar_enteros_v2(desde, hasta)
print(f"La suma de los números desde {desde} hasta {hasta} es un total de {suma} ")