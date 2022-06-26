'''
-------------------------------------------------------------------------------
Ejercicio 3.01 al 3.05: Errores
-------------------------------------------------------------------------------
'''

# Ejercicio 3.1: Semántica
# Error SINTÁCTICO y estaba ubicado en la impresión de la función.
#    Lo corregí cambiando agregando print antes de imprimir la función

# Código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
#%%

# Ejercicio 3.2: Sintaxis
# Error SINTÁCTICO y estaba ubicado en la impresión de la función.
    # Lo corregí cambiando agregando ":" después de (expresion)
# Error SINTÁCTICO ubicado en el while
    # Lo corregí agregando ":"
# Error SINTACTICO ubicado en el if
    # Lo corregí agregando un "=" antes de la "a" que que no estaba realizando comparación sino asignación.
    # Además agregué ":" al termino del if
# Error SINTÁCTICO y estaba ubicado al finalizar la función
    # Lo corregí cambiando Falso por False ya que se trata de una variable de tipo booleano
# Error SINTÁCTICO cuando se llama a la función
    # Lo corregí agregando print antes de llamar a la función


# Código corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n: 
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%%

#Ejercicio 3.3: Tipos

# Error SINTÁCTICO y estaba ubicado cuando se llama a la función y se pasa por parámetro (1984)
    # Lo corregí colocando comillas a ('1984') 
    #ya que dentro de la función se utiliza la longitud de la cadena que se ingresa por parámetro
# Error SINTÁCTICO cuando se llama a la función
    # Lo corregí agregando print antes de llamar a la función


#Código corregido
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))


#%%

#Ejercicio 3.4: Alcances

# Error SINTÁCTICO dentro de la función
    # Lo corregí agregando "return c" al finalizar la función, ya que en este caso necesito me devuelva el valor de la suma


#Código corregido:
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%

# Ejercicio 3.5: Pisando memoria
# Se agrego registro={} dentro del for
# Siempre actualiza el mismo diccionario dentro del for, por ende se declaro 
# el diccionario dentro del ciclo para que vaya generando otra variable diccionario en cada iteración

import csv
from pprint import pprint

# Código corregido
def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)