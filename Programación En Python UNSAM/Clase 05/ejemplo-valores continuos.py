# -*- coding: utf-8 -*-

import random



def generar_punto():
    x=random.random()
    y=random.random()
    return x,y

N=10000
M=0
for i in range(N):
    x,y=generar_punto()
    if x**2+y**2 <1:
        M+=1
        
print(f"pi ~ {4*M/N:.5f}")

#%%

import matplotlib.pyplot as plt

N=1000
M=0
Xi =[]
Yi =[]
Xo =[]
Yo =[]

for i in range(N):
    x,y = generar_punto()
    if x**2+y**2 <1:
        Xi.append(x)
        Yi.append(y)
        M+=1
    else:
        Xo.append(x)
        Yo.append(y)
        
print(f"pi ~ {4*M/N:.5f}")

#%%

plt.clf()
plt.scatter(Xi,Yi,s=1)
plt.scatter(Xo,Yo,s=1)

#parámetros s,c y alpha