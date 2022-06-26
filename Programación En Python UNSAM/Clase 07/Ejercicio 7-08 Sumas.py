'''
-------------------------------------------------------------------------------
Ejercicio 7.8: Sumas
-------------------------------------------------------------------------------
Realizar dos implementaciones correspondientes a la función sumar_enteros 
definida recién.
- En la primera implementación te pedimos que uses un ciclo.
- En la segunda te pedimos que lo hagas sin ciclos: implementá la función de 
manera que trabaje en tiempo constante (es decir, usando una cantidad de 
operaciones que no depende de las entradas a la función.
Ayuda: Estas sumas se pueden escribir como diferencia de dos números 
triangulares.
-------------------------------------------------------------------------------
'''

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0

    '''
    suma=0
    for i in range(desde, hasta+1):
        suma+=i
    return suma



desde=1
hasta=4
suma=sumar_enteros(desde, hasta)
print(f"La suma de los números desde {desde} hasta {hasta} es un total de {suma} ")

#%%

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