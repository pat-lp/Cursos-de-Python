# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:18:18 2021

@author: Patricia
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

rta = tiene_a ('palabra')
print(rta)