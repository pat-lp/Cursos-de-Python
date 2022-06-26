'''
-------------------------------------------------------------------------------
Ejercicio 5.04: Envido
-------------------------------------------------------------------------------
Explicado en clase de Youtube.
-------------------------------------------------------------------------------
'''
import random
from tqdm import tqdm

def dar_mano():
    return random.sample(naipes,3) #sin repetición

def tengo_31(mano):
    tengo=False
    for palo in palos:
        if (4,palo) in mano and (7,palo) in mano:
            tengo=True
        if (5,palo) in mano and (6,palo) in mano:
            tengo=True
    return tengo


def tengo_32(mano):
    tengo=False
    for palo in palos:
        if(5, palo) in mano and (7,palo) in mano:
            tengo=True
    return tengo

def tengo_33(mano):
    tengo=False
    for palo in palos:
        if (6,palo) in mano and (7,palo) in mano:
            tengo=True
    return tengo
        
valores =[1,2,3,4,5,6,7,10,11,12]
palos =['oro', 'copa','espada','basto']
naipes =[(valor,palo) for valor in valores for palo in palos]

N=100000
G31=0
G32=0
G33=0
'''
for i in range(N):
    if i%10000 ==0:
        print(".", end='')#para tener una idea del progreso
    mano=dar_mano()
    if tengo_31(mano):
         G31+=1
    elif tengo_32(mano):
         G32+=1
    elif tengo_33(mano):
         G33+=1'''


for i in tqdm(range(N)): #'tqdm' para incrementar la cantidad de iteraciones
     mano=dar_mano()
     if tengo_33(mano):
         G33+=1
     elif tengo_32(mano):
         G32+=1
     elif tengo_31(mano):
         G31+=1

print(f"Repartí {N} veces de las cuales {G31} saqué envido, {G32} saqué 32 de envido y {G33} saqué 33 de envido.")
print(f"Podemos estimar la probabilidad de tener 31: {G31/N:.6f}, 32: {G32/N:.6f} y 33: {G33/N:.6f}.")