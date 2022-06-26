# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:31:44 2021

@author: Patricia
"""

'''
------------------------------------------------------------------------------
Ejercicio 6.17: Complejidad de incrementar()
------------------------------------------------------------------------------
Si tomamos n = len(s) podemos tratar de medir la complejidad de la función incrementar() en términos de la longitud n de la secuencia. ¿Te parece que incrementar() es una función lineal, cuadrática, logarítmica o exponencial? ¿Por qué?
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



print(incrementar([0,0,0,0,0]))#[0, 0, 0, 0, 1]
print(incrementar([0,0,1,1,0]))#[0, 0, 1, 1, 1]
print(incrementar([0,0,1,1,1]))#[0, 1, 0, 0, 0]
print(incrementar([1,1,1,1,1]))#[0, 0, 0, 0, 0]