import random


#Simular la tirada de un dado
dado = random.randint(1,6)
print(dado)

#%% LA GENERALA

import random

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6))
    
print(tirada)

#%% SIN REPOSICION

from pprint import pprint
import random

palos=['oro','copa','espada','basto']
valores =[1,2,3,4,5,6,7,10,11,12]

naipes = [ (valor,palo) for valor in valores for palo in palos]
pprint(naipes)

random.sample(naipes,k=3) #muestra sin reposicion,k=3 naipes

#%% SHUFFLE

#orden aleatorio
print(random.shuffle(naipes))

#%% SEMILLAS

import random

random.seed(31415)

tirada=[]

for i in range(5):
    tirada.append(random.randint(1, 6))
    
print(tirada)
    
#%% SHUFFLE

palos=['oro','copa','espada','basto']
valores =[1,2,3,4,5,6,7,10,11,12]

naipes = [ (valor,palo) for valor in valores for palo in palos]

random.shuffle(naipes)
print(naipes)

print(naipes[-3:]) #Consultar las 3 cartas que quedaron al final

n1= naipes.pop()
n2= naipes.pop()
n3= naipes.pop()

print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')
