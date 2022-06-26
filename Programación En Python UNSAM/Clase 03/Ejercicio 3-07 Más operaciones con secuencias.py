# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:22:48 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio 3.07: Más operaciones con secuencias
-------------------------------------------------------------------------------
Algunas operaciones de reducción de secuencias.
-------------------------------------------------------------------------------
'''

data = [4, 9, 1, 25, 16, 100, 49]
min(data)

#%%

max(data)

#%%

sum(data)

#%%

for x in data:
        print(x)
        
#%%

for n, x in enumerate(data):
        print(n, x)
        
#%%
data = [4, 9, 1, 25, 16, 100, 49]
for n in range(len(data)):
        print(data[n])