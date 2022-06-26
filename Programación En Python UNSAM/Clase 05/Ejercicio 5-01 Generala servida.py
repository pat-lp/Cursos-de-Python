'''
-------------------------------------------------------------------------------
Ejercicio 5.01: Generala servida
-------------------------------------------------------------------------------
Queremos estimar la probabilidad de obtener una generala servida (cinco dados iguales) en una tirada de dados. Podemos hacer la cuenta usando un poco de teoría de probabilidades, o podemos simular que tiramos los dados muchas veces y ver cuántas de esas veces obtuvimos cinco dados iguales. En este ejercicio vamos a usar el segundo camino.

Escribí una función tirar() que devuelva una lista con cinco dados generados aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve True si y sólo si los cinco dados de la lista tirada son iguales.
-------------------------------------------------------------------------------
'''
import random

def tirar():
    tirada=[random.randint(1,6) for dado in range(5)]
    return tirada


def es_generala(tirada):
    generala=True
    conjunto=set(tirada)
    if len(conjunto)!= 1:
        generala=False
    return generala

print(tirar())

N = 100000
G= sum([es_generala(tirar()) for i in range(N)])

prob =G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#Cómo saber la precisión de los resultados obtenidos.
#Cuál es la probabilidad real? si yo tiro un dado, no importa el valor del primero pero si de los siguientes.
prob=1/6**4
print("Probabilidad real: ",prob)

#%% SUMA DE 5 DADOS
import matplotlib.pyplot as plt

N=100#00
sumas =[sum(tirar()) for i in range(N)]


plt.hist(sumas,bins=26)#,density=True)
