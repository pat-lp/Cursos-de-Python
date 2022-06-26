# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:53:49 2021

@author: Patricia
"""

'''
------------------------------------------------------------------------------
Ejercicio 2.11: Tuplas
------------------------------------------------------------------------------
>>> import csv
>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> next(filas)
['nombre', 'cajones', 'precio']
>>> fila = next(filas)
>>> fila
['Lima', '100', '32.2']
>>>

En el intérprete interactivo, creá la siguiente tupla que representa la fila de antes, pero con las columnas numéricas pasadas a formatos adecuados:

>>> t = (fila[0], int(fila[1]), float(fila[2]))
>>> t
('Lima', 100, 32.2)
>>>
A partir de esta tupla, ahora podés calcular el costo total multiplicando cajones por precio:

>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
¿Qué pasó? ¿Qué hace ese 5 al final?

Este error no es un problema de Python, sino de la forma en la que la máquina representa los números de punto flotante. Así como en base 10 no podemos escribir un tercio de manera exacta, en base 2 escribir un quinto requiere infinitos dígitos. Al usar una representación finita (una cantidad acotada de dígitos) la máquina redondea los números. La aritmética de punto flotante no es exacta.

Esto pasa en todos los lenguajes de programación que usan punto flotante, pero en muchos casos estos pequeños errores quedan ocultos al imprimir. Por ejemplo:

>>> print(f'{cost:0.2f}')
3220.00
>>>
Las tuplas son de sólo lectura. Verificalo tratando de cambiar el número de cajones a 75.

>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
Aunque no podés cambiar al tupla, sí podés reemplazar la tupla por una nueva.

>>> t = (t[0], 75, t[2])
>>> t
('Lima', 75, 32.2)
>>>
Siempre que reasignes una variable como recién lo hiciste con t, el valor anterior de la variable se pierde. Aunque la asignación de arriba pueda parecer como que estás modificando la tupla, en realidad estás creando una nueva tupla y tirando la vieja.

Las tuplas muchas veces se usan para empaquetar y desempaquetar valores dentro de variables. Probá esto:

>>> nombre, cajones, precio = t
>>> nombre
'Lima'
>>> cajones
75
>>> precio
32.2
>>>
Tomá las variables de arriba y empaquetalas en una tupla.

>>> t = (nombre, 2*cajones, precio)
>>> t
('Lima', 150, 32.2)
>>>
------------------------------------------------------------------------------
'''