'''
-------------------------------------------------------------------------------
Ejercicio "documentacion"
-------------------------------------------------------------------------------
Pensá cuál es el contrato de la función.
Agregale la documentación adecuada.
Comentá el código si te parece que aporta.
Detectá si hay invariantes de ciclo y comentalo al final de la función
-------------------------------------------------------------------------------
'''

def valor_absoluto(n):
    '''
    Valor absoluto de un número.
    Precondición: Recibe un número 
    Poscondición: Devuelve un número positivo si es mayor que cero y realiza el
    valor absoluto si el número es negativo.
    '''
    if n >= 0:
        return n
    else:
        return abs(-n) #Se agregó abs para poder devolver el valor absoluto del nro.



def suma_pares(l):
    '''
    Suma los números pares de una lista.
    Precondición: Recibe un lista de números enteros.
    Poscondición: Devuelve la suma de todos los números enteros de la lista l, o devuelve 
    cero si no se realizó ninguna suma.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res #INVARIANTE DE CICLO = res


def veces(a, b):
    '''
    Suma a la cantidad de b veces
    Precondición: a es un número entero y b tiene que ser un número positivo.
    Poscondición: Devuelve la suma de b veces el valor de a.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res #INVARIANTE DE CICLO=res


def collatz(n):
    res = 1
    '''
    Conjetura del Dr. Lothar
    Precondición: Recibe un número entero positivo
    Poscondición: Devuelve la cantidad de iteraciones que realizó hasta llegar a 1.
    '''
    while n!=1:
        if n % 2 == 0: #Si el número es par lo divide por 2
            n = n//2
        else:
            n = 3 * n + 1 #Si el número es impar lo múltiplica por 3 y le suma 1
        res += 1
    return res #INVARIANTE DE CICLO = res


def f_principal():
    '''Imprime por pantalla las pruebas de lo realizado.'''
    nro_absoluto=-1
    print(f"Valor absoluto del número {nro_absoluto} es: ",valor_absoluto(nro_absoluto))
    #l=[1,2,3,4,5,6,8]
    #l=[1,3,5]
    l=[-2,-4,-6]
    print(f"La suma de los números pares de la lista{l} es: ",suma_pares(l))
    a=3
    b=2
    print(f"Suma el número {a} la cantidad de {b} veces resultando: ",veces(a, b))
    n=6
    print(f"La cantidad de iteraciones para el número {n} según la conjetura del Dr. Lothar es:",collatz(n))



if __name__ == "__main__" :
    f_principal()
    
