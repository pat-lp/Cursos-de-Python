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
print("\n---------------------------------------------------")
print("\t\t\t\t Resultado")
print("---------------------------------------------------")

# Se utiliza el ciclo for y se añade a la impresión la sílaba que corresponde 
# a la vocal, además se agrega end="" para hacer que imprima en una sola línea.
for c in cadena:
    if c=="a":
        print("a"+"pa", end="")
    elif c == "e":
        print("e"+"pe",end="")
    elif c == "i":
        print("i"+"pi",end="")
    elif c == "o":
        print("o"+"po",end="")
    elif c == "u":
        print("u"+"pu",end="")
    else:
        print(c,end="")
        
print("\n---------------------------------------------------")