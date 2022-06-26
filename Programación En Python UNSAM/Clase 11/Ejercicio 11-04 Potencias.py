# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:25:21 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio 11.4: Potencias
-------------------------------------------------------------------------------
Escribí una función recursiva es_potencia(n, b) que reciba 2 enteros, n y b, y 
devuelva True si n es potencia de b y False en caso contrario.
Ejemplos:

es_potencia(8, 2) -> True
es_potencia(64, 4) -> True
es_potencia(70, 10) -> False
es_potencia(1, 2) -> True
-------------------------------------------------------------------------------
'''

def es_potencia(n, b):
    resultado = False
    for i in range(0, n):
        pot = b **i
        print(pot)
        if pot== n:
            resultado=True
            break
    return resultado


b=10
n=70
print(es_potencia(n, b))