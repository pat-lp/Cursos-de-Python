'''
------------------------------------------------------------------------------
Ejercicio 10.13: Expresiones generadoras
------------------------------------------------------------------------------
'''

nums = [1,2,3,4,5]
cuadrados = (x*x for x in nums)
print(cuadrados)

for n in cuadrados:
    print(n)

'''
A diferencia de una definición por comprensión de listas, una expresión 
generadora sólo puede recorrerse una vez. Si intentás recorrerla de nuevo 
con otro for, no obtenés nada.'''
for n in cuadrados:
    print(n) #NO SE OBTIENE NADA