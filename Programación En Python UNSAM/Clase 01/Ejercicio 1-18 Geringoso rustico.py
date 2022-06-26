'''
-------------------------------------------------------------------------------
Ejercicio 1.18: Geringoso rústico
-------------------------------------------------------------------------------
Usá una iteración sobre el string cadena para agregar la sílaba 
'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

>>> cadena = 'Geringoso'
>>> capadepenapa = ''
>>> for c in cadena:
        ?
>>> capadepenapa
Geperipingoposopo
Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.
-------------------------------------------------------------------------------
'''

cadena = "Geringoso"
cadenaGeringoso=""
vocales ="aeiou"
print("\n---------------------------------------------------")
print("\t\t\t\t Resultado")
print("---------------------------------------------------")
for c in cadena:
    if c in vocales:
        cadenaGeringoso+=c+"p"+c
    else:
        cadenaGeringoso+=c
print(cadenaGeringoso)
print("\n---------------------------------------------------")