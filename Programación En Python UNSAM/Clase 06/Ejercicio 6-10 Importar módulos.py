'''
-------------------------------------------------------------------------------
Ejercicio 6.10: Importar módulos
-------------------------------------------------------------------------------
'''

import rebotes

import hipoteca

import informe_funciones

import fileparse

help(fileparse)

dir(fileparse)

print("---------------------------------------------------------------------------")
print("Camion")
print("---------------------------------------------------------------------------")
camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
print(camion)
print("---------------------------------------------------------------------------")
print("Tuplas de precios")
print("---------------------------------------------------------------------------")
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
print(lista_precios)
print("---------------------------------------------------------------------------")
print("Precios")
print("---------------------------------------------------------------------------")
precios = dict(lista_precios)
print(precios)
print("---------------------------------------------------------------------------")
print("Precio Naranja: ",precios['Naranja'])
print("---------------------------------------------------------------------------")

#%%

from fileparse import parse_csv

print("---------------------------------------------------------------------------")
print("Camion")
print("---------------------------------------------------------------------------")
camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
print(camion)
print("---------------------------------------------------------------------------")
print("Tuplas de precios")
print("---------------------------------------------------------------------------")
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
print(lista_precios)
print("---------------------------------------------------------------------------")
print("Precios")
print("---------------------------------------------------------------------------")
precios = dict(lista_precios)
print(precios)