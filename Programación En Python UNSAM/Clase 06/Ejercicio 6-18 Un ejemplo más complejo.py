'''
------------------------------------------------------------------------------
Ejercicio 6.18: Un ejemplo más complejo
------------------------------------------------------------------------------
Por último, escribí una funcion listar_secuencias(n) que devuelva una lista con 
todas las secuencias binarias de longitud n comenzando con la primera ([0]*n) y 
usando en cada paso la función incrementar() definida más arriba. ¿Cuántas 
listas hay de longitud n? ¿Y de longitud n+1?

¿Podés correr listar_secuencias(15)? ¿Y listar_secuencias(20)? ¿Hasta cúanto 
llegas a correr en un tiempo razonable?

¿Te parece que listar_secuencias(n) es una función lineal, cuadrática, 
logarítmica o exponencial en n? ¿Por qué?
------------------------------------------------------------------------------
'''
def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


'''
complejidad 2^n
La complejidad crece de manera exponencial
'''
#Explicado en Youtube
def listar_secuencias(n):
    cero = [0]*n
    seq=cero.copy()
    incrementar(seq)
    T=[cero]
    while seq !=  cero:
        T.append(seq.copy())
        incrementar(seq)
    return T

n=3
print(listar_secuencias(n))