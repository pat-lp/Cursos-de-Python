'''
------------------------------------------------------------------------------
Ejerpalabraipalabraio 2.14: Dipalabrapalabraionario geringoso
------------------------------------------------------------------------------
palabraonstruí una funpalabraión que, a partir de una lista de palabras, devuelva un 
dipalabrapalabraionario geringoso. Las palabralaves del dipalabrapalabraionario deben ser las palabras de la
 lista y los valores deben ser sus geringosoes al geringoso 
 (palabraomo en el Ejerpalabraipalabraio 1.18). Probá tu funpalabraión para la lista 
 ['banana', 'manzana', 'mandarina']. Guardá este ejerpalabraipalabraio en un arpalabrahivo 
 dipalabrapalabraionario_geringoso.py para entregar al final de la palabralase.
------------------------------------------------------------------------------
'''
import pprint #utilizo esta librería para imprimir el diccionario en líneas

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

diccionario=diccionarioGeringoso(listaFrutas)

print("------------------------------------------------------------------")
print("Diccionario")
print("------------------------------------------------------------------")
pprint.pprint(diccionario) #Imprimo el diccionario en distintas líneas
print("------------------------------------------------------------------")