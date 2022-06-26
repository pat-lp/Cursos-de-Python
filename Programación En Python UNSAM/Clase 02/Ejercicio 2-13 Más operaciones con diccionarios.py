# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:56:26 2021

@author: Patricia
"""

'''
------------------------------------------------------------------------------
Ejercicio 2.13: Más operaciones con diccionarios
------------------------------------------------------------------------------
Si usás el comando for para iterar sobre el diccionario, obtenés las claves:

>>> for k in d:
        print('k =', k)

k = nombre
k = cajones
k = precio
k = fecha
k = cuenta
>>>
Probá esta variante:

>>> for k in d:
        print(k, '=', d[k])

nombre = 'Lima'
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
cuenta = 12345
>>>
Una manera más elegante de trabajar con claves y valores simultáneamente es usar el método items(). Esto te devuelve una lista de tuplas de la forma (clave,valor) sobre la que podés iterar.

>>> items = d.items()
>>> items
dict_items([('nombre', 'Lima'), ('cajones', 75), ('precio', 32.2), ('fecha', (14, 8, 2020))])
>>> for k, v in d.items():
        print(k, '=', v)

nombre = Lima
cajones = 75
precio = 32.2
fecha = (14, 8, 2020)
>>>
Si pasás un diccionario a una lista, obtenés sus claves.

>>> list(d)
['nombre', 'cajones', 'precio', 'fecha', 'cuenta']
>>>
También podés obtener todas las claves del diccionario usando el método keys():

>>> claves = d.keys()
>>> claves
dict_keys(['nombre', 'cajones', 'precio', 'fecha', 'cuenta'])
>>>
Si tenés tuplas como en items podés crear un diccionario usando la función dict(). Probá esto:

>>> nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> nuevos_items
[('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
>>> d = dict(nuevos_items)
>>> d
{'nombre': 'Manzanas', 'cajones': 100, 'precio': 490.1, 'fecha': (13, 8, 2020)}
------------------------------------------------------------------------------
'''