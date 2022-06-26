'''
-------------------------------------------------------------------------------
Ejercicio 5.02: Generala no necesariamente servida
-------------------------------------------------------------------------------
Si uno juega con las reglas originales (se puede volver a tirar algunos de los
cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo 
una estrategia que intente obtener generala (siempre guardar los dados que más 
se repiten y tirar nuevamente los demás) es más probable obtener una generala 
que si sólo consideramos la generala servida. Escribí un programa que estime la 
probabilidad de obtener una generala en las tres tiradas de una mano y guardalo 
en un archivo generala.py.
-------------------------------------------------------------------------------
'''

import random
from collections import Counter

def tirar():
    return [random.randint(1,6) for dado in range(5)]


def es_generala(tirada):
    generala=True
    conjunto=set(tirada)
    if len(conjunto)!= 1:
        generala=False
    return generala

def generala_no_servida(tirar):
    tirada=tirar.copy()
    resultado=False
    repetido=Counter(tirada).most_common(1)[0][0]#valor que se repite
    cont=0
    tirada.sort()
    while resultado!= True and cont<3:
        cont+=1
        for valor in tirada:
            if valor != repetido:
                tirada.remove(valor)
                tirada.append(random.randint(1,6))
        if es_generala(tirada)==True:
            resultado=True
    return resultado
    
def prob_generala(N):
    G=sum([generala_no_servida(tirar()) for i in range(N)])
    return G/N


N = 100
prob=prob_generala(N)

print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


