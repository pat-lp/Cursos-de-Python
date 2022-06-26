'''
------------------------------------------------------------------------------
Ejercicio 6-02: Propagar como el auto fantástico
------------------------------------------------------------------------------
'''
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#%% MODIFICACION DEL CODIGO

print("--------------------------------------------------------------")
print("Código modificado")
print("--------------------------------------------------------------")

def propagar_a_derecha_(l):
    copiaLista=l.copy()
    n = len(copiaLista)
    for i,e in enumerate(copiaLista):
        if e==1 and i<n-1:
            if copiaLista[i+1]==0:
                copiaLista[i+1] = 1
    return copiaLista
#%
def propagar_a_izquierda_(l):
    return propagar_a_derecha_(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha_(l)
    lp=propagar_a_izquierda_(ld)
    return lp

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
propagar([1,0,0,0,0,0,0,0,1])
#%% PREGUNTAS:
    
'''
1-¿Por qué se modificó la lista original?
Rta: 
    Se modificó la lista original porque no se trabajó con una copia sino que 
    se trabajo sobre la misma lista.
    
2-¿Por qué no quedó igual al estado propagado?
Rta:
    La lista se modifica en la primer función que es propagar_a_derecha, luego 
    en propagar se develve el resultado de la modificación pero se asigna a 
    otra variable que es ld con la cual se termina de hacer la propagación 

3-Corregí el código para que no cambie la lista de entrada.

4-¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n?
Rta:
    La cantidad de operaciones que hace propagar_a_derecha en una lista de 
    largo n son n+1 comparaciones.


5-Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de 
operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo 
propagar en una lista de largo n?
Rta:
    Hace como n comparaciones, es un algoritmo lineal.(ver bien)


'''