# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:13:22 2021

@author: Patricia
"""

def busqueda_lineal(lista,e):
    '''Si e está en la lista devuelve su posición,
     de lo contrario devuelve -1.'''
    
    pos=-1 #comenzmos suponiendo que e no está
    i=0
    #recorremos los elementos de la lista
    for z in lista:
        if z== e: #si encontramos a e
            pos=i #guardamos su posición
            break #y salimos del ciclo
        i += 1
    return pos


print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44))#-1

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 3))#3

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 0))#4

print(busqueda_lineal([], 42))#-1

#%% VERSION CON ENUMERATE

def busqueda_lineal(lista,e):
     '''Si e está en la lista devuelve su posición,
     de lo contrario devuelve -1.'''
      #comenzamos suponeindo que e no está
     pos = -1  
     for i,z in enumerate(lista): #recorremos la lista
         if z==e:  # si encontramos a e
             pos=i #guardamos su posición
             break #y salimos del ciclo
     return pos
 
print(busqueda_lineal([1, 4, 54, 3, 0, -1], 44)) #-1

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 3))#3

print(busqueda_lineal([1, 4, 54, 3, 0, -1], 0))#4

print(busqueda_lineal([], 42))#-1