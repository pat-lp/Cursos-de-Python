'''
-------------------------------------------------------------------------------
Ejercicio 1.1: Python como calculadora
-------------------------------------------------------------------------------
En tu máquina, iniciá Python y usalo como calculadora para resolver 
el siguiente problema:

¿Cuántas horas son 105 minutos?
¿Cuántos kilómetros son 20 millas? (un kilómetro corresponde a 0,6214 millas)
-------------------------------------------------------------------------------
'''

print("\n-----------------------------------------\n")
# 1
print("¿Cuántas horas son 105 minutos?")
horas= 105/60
print("La cantidad de horas que son 105 minutos es", horas)
print("\n-----------------------------------------\n")

# 2
print("¿Cuántos kilómetros son 20 millas?")
km = 20/0.6214
print("La cantidad de kilómetros que son 20 millas es un total de: {:.3f}".format(km))
print("\n-----------------------------------------\n")

# 3
print("Si alguien corre una carrera de 20 millas en 105 minutos, ¿cuál fue tu velocidad promedio en km/h?")
kmh= km/1.75
print("La velocidad en km/h es de: {:.3f}".format(kmh))
print("\n-----------------------------------------\n")

