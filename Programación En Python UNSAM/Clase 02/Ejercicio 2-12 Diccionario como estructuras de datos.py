# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:55:55 2021

@author: Patricia
"""

'''
------------------------------------------------------------------------------
Ejercicio 2.12: Diccionarios como estructuras de datos
------------------------------------------------------------------------------
Una alternativa a la tupla es un diccionario.

>>> d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
>>> d
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2 }
>>>
Calculá el costo total de este lote:

>>> cost = d['cajones'] * d['precio']
>>> cost
3220.0000000000005
>>>
Compará este ejemplo con el mismo cálculo hecho con tuplas más arriba. Cambiá el número de cajones a 75.

>>> d['cajones'] = 75
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio': 32.2 }
>>>
A diferencia de las tuplas, los diccionarios se pueden modificar libremente. Agregá algunos atributos:

>>> d['fecha'] = (14, 8, 2020)
>>> d['cuenta'] = 12345
>>> d
{'nombre': 'Lima', 'cajones': 75, 'precio':32.2, 'fecha': (14, 8, 2020), 'cuenta': 12345}
>>>
------------------------------------------------------------------------------
'''