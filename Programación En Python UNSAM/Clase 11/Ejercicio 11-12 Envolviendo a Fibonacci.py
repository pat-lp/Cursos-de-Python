'''
------------------------------------------------------------------------------
Ejercicio 11.12: Envolviendo a Fibonacci
------------------------------------------------------------------------------
Escribí una función fibonacci(n) que calcule el n-ésimo número de Fibonacci de 
forma recursiva pero que utilice un diccionario para almacenar los valores ya 
computados y no computarlos más de una vez.

Observación: Será necesario implementar una función wrapper (es decir, una 
función que envuelva a otra) para cumplir con la firma de la función pedida. 
Podés trabajar en un script en blanco o completar el siguiente código.
------------------------------------------------------------------------------
'''

def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            ?? # completar
        return ?? # completar
    
    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 