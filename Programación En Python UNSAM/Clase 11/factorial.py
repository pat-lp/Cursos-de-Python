'''
------------------------------------------------------------------------------
Factorial
------------------------------------------------------------------------------
'''

def factorial(n):
    '''Calcula el factorial de un número positivo.'''
    if n == 1:
        return 1
    return n * factorial(n - 1)



n = 3
print(factorial(n))