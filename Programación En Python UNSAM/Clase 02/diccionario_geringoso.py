'''
------------------------------------------------------------------------------
Ejercicio 2.14: Diccionario geringoso
------------------------------------------------------------------------------
Construí una función que, a partir de una lista de palabras, devuelva un 
diccionario geringoso. Las claves del diccionario deben ser las palabras de la
lista y los valores deben ser sus traducciones al geringoso. Probá tu función
para la lista ['banana', 'manzana', 'mandarina']. 
------------------------------------------------------------------------------
'''
import pprint

def diccionarioGeringoso(listaPalabras):
    diccionario={}
    vocales="aeiou"
    
    for palabra in listaPalabras:
        geringoso=""
        for letra in palabra:
            geringoso += letra
            if letra in vocales:
                geringoso += "p"+letra
        diccionario[palabra]=geringoso
    return diccionario

listaFrutas =  ['banana', 'manzana', 'mandarina']

diccionario = diccionarioGeringoso(listaFrutas)

print("------------------------------------------------------------------")
print("Diccionario")
print("------------------------------------------------------------------")
pprint.pprint(diccionario)
print("------------------------------------------------------------------")