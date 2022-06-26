'''
-------------------------------------------------------------------------------
Ejercicio 3.10: Invertir un diccionario
-------------------------------------------------------------------------------
VER BIEN!!!!!!!!! A ENTREGAR
-------------------------------------------------------------------------------
'''

precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
print("-----------------------------------------------------------")

# Con el método items(), obtenés pares (clave,valor):
print(precios.items())

print("-----------------------------------------------------------")
# Para obtener pares (valor, clave), usá zip().
lista_precios = list(zip(precios.values(),precios.keys()))
print("Lista con (valor,clave)\n",lista_precios)
print("-----------------------------------------------------------")
print("Mínimo: ",min(lista_precios))

print("Máximo: ", max(lista_precios))

print("Ordenado: ",sorted(lista_precios))

print("-----------------------------------------------------------")

# zip() No esta limitado a pares
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]

print("Ejemplo zip() con tres listas\n",list(zip(a, b, c)))

print("-----------------------------------------------------------")
print("La función zip() corta cuando una de las entradas es más corta")
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))