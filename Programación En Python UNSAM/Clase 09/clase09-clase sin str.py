# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:57:38 2021

@author: Patricia
"""


s = "ejemplo de cadena"
s.upper() #un método de la clase cadena
c = "otro ejemplo"
c.upper()


lista = [0,1,2,3]
lista.index(2) #un método que no modifica el objeto
lista.append(4) #un método que sí modifica el objeto
#%%
##############
##  CLASES  ##
##############

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

#%% constructores
a = Punto(1,1)
a.x
a.y

b = Punto(3,4)
b.x
b.y

#%% más métodos
import numpy as np

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_origen(self):
        n = np.sqrt(self.x**2 + self.y**2)
        return n

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

#%%
#defino una instancia
a = Punto(1,1)
a.x
a.y
a.dist_origen()

#defino otra instancia
b = Punto(3,4)
b.dist_origen()

#%%
a.mover(1,1)
a.x
a.y
a.dist_origen()

#%%
b.x
print(b)
