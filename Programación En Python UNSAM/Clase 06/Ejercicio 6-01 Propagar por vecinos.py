'''
------------------------------------------------------------------------------
Ejercicio 6-01: Propagar por vecinos
------------------------------------------------------------------------------
'''
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):  #O(n)
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l): #O(n^2)
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m

propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
propagar([0,0,0,0,0,0,0,0,1])

#%% PREGUNTAS

'''
1-¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no 
causan un IndexError en los bordes de la lista?
Rta: 
    Porque Python evalúa las condiciones del primer and y si no se cumple no 
    sigue comprobando el resto(lazy evaluation).

2-¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas 
perfectamente simétricas, no generan la misma cantidad de repeticiones de 
llamadas a la función propagar_al_vecino?
Rta:
    Porque propagar([1,0,0,0,0]) comienza con 1 que es la opción que evaluúa 
    el condicional de propagar_al_vecino, en cambio con propagar([0,0,0,0,1])
    tiene que recorrer todo el vector antes de encontrar el 1 y comenzar a 
    propagar.

3-Sobre la complejidad. Si te sale, calculá:
3.1-¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de 
largo n?
Rta: 
    Se puede repetir el ciclo while n veces el largo de la lista.

3.2-¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
Rta:
    Hace O(n) operaciones.

3.3-Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar en una 
lista de largo n? ¿Es un algoritmo de complejidad lineal o cuadrática?
Rta:
    Es un algoritmo cuadrático, con complejidad O(n^2)

'''