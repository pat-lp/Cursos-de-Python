'''
------------------------------------------------------------------------------
Potencia
------------------------------------------------------------------------------
'''

def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b
    

print(potencia(2, 10))#1024
print(potencia(3, 3))#27
print(potencia(5, 0))#1


#%% ITERATIVO CON PILA

def potencia(b, n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2

    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b

    return p

print(potencia(2, 10))#1024
print(potencia(3, 3))#27
print(potencia(5, 0))#1