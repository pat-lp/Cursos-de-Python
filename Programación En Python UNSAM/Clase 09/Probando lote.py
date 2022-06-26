# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:53:04 2021

@author: Patricia
"""


import lote

a = lote.Lote('Pera', 100, 490.10)

print(a.nombre)#'Pera'
print(a.cajones)#100
print(a.precio)#490.1


#Vamos a crear más objetos de tipo Lote para manipularlos. Por ejemplo:

b = lote.Lote('Manzana', 50, 122.34)
c = lote.Lote('Naranja', 75, 91.75)
b.cajones * b.precio#6117.0
c.cajones * c.precio#6881.25
lotes = [a, b, c]
print(lotes)#ERROR, IMPRIME DIRECCIONES DE MEMORIA
#[<lote.Lote object at 0x37d0b0>, <lote.Lote object at 0x37d110>, <lote.Lote object at 0x37d050>]
for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')


#%% SE AGREGAN METODOS COSTO Y VENDER A LOTE

s = lote.Lote('Pera', 100, 490.10)
print(s.costo())#49010.0
print(s.cajones)#100
print(s.vender(25))
print(s.cajones)#75
print(s.costo())#36757.5

#%% PROBANDO __repr__

s = lote.Lote('Pera', 100, 490.10)
print(repr(s))

peras = lote.Lote('Pera', 100, 490.1)
print(peras)