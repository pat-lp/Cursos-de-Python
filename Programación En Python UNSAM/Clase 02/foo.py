# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:18:30 2021

@author: Patricia
"""

'''
Atrapar excepciones
Ctrl+C genera una excepción de tipo KeyboardInterrupt que no es atrapada
'''

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')



#%%
'''
Al presionar las teclas Ctrl+C la excepción KeyboardInterrupt sí es atrapada y
 no se termina el ciclo hasta no ingresar un número entero.
'''

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

#%%

raise RuntimeError('¡Qué moco!')