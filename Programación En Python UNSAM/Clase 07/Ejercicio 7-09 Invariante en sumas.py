'''
-------------------------------------------------------------------------------
Ejercicio 7.9: Invariante en sumas
-------------------------------------------------------------------------------
'''

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    
    
    EL INVARIANTE DE CICLO ES suma.
    
    '''
    suma=0
    for i in range(desde, hasta+1):
        suma+=i
    return suma



desde=1
hasta=4
suma=sumar_enteros(desde, hasta)
print(f"La suma de los números desde {desde} hasta {hasta} es un total de {suma} ")