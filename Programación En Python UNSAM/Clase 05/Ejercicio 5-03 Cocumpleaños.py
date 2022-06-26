'''
-------------------------------------------------------------------------------
Ejercicio 5.03: Cocumpleaños
-------------------------------------------------------------------------------
Haciendo miles de experimentos numéricos, estimá la probabilidad de que en un 
grupo de 30 personas elegidas al azar, dos cumplan años el mismo día. Escribí 
un programita que permita calcular esa probabilidad asumiendo que el año tiene 
365 días.
-------------------------------------------------------------------------------
'''

#La paradoja del cumpleaños(paradoja es porque parece lo contrario a la intuición).
'''EXPLICACIÓN: Para calcular la probabilidad para cualquier número de personas
n<=365(con más de 365 la probabilidad es 1), la idea es calcular la probalidad de que no 
haya dos personas que cumplan años el mismo día(la llamaremos p). Después se 
calcula la probabilidad de que haya alguna realizando 1-p.

Tomamos una de las personas del grupo que cumplirá un cierto día, tomamos otra 
de las personas y la probabilidad de que esta persona no coincida en cumpleaños 
con la primera es de 364/365(casos favorables: todos los días excepto el del 
cumpleaños de la primera persona; casos posibles: todos los días del año).
'''
 
import math

#Formula utilizada: 1-( (365!) / 365^n * (365-n)!)

n=30

p=1-(math.factorial(365))/((365**n)*(math.factorial(365-n)))

print(f"La probabilidad de que dos personas cumplan el mismso día es de {p} poco más  de {round(p*100,2)}%")


