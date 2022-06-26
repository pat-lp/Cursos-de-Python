# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:55:29 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio 3.12: Formato de números
-------------------------------------------------------------------------------
Imprimir números decimales
-------------------------------------------------------------------------------
'''

value= 42863.1
print(value)

print(f'{value:0.4f}') #flotante con 4 decimales

print(f'{value:> 16.2f}') #flotante alineado a la derecha

print(f'{value:<16.2f}')#flotante alineado a la izq.

print(f'{value:*>16.2f}') #flotante alineado der. acompañado de asteriscos