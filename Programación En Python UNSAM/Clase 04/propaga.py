'''
-------------------------------------------------------------------------------
Ejercicio 4.06: Propagación
-------------------------------------------------------------------------------
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos 
pueden estar en tres estados: nuevos, prendidos fuego o ya gastados 
(carbonizados). Representaremos esta situación con una lista L con un elemento 
por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 
(carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a 
cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se 
encienden nuevamente.

Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's 
y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0.
-------------------------------------------------------------------------------
'''

def propagar(vector):
    copiaVector= vector.copy()
    #Recorro la lista,si tengo 1 reemplazo los valores consecutivos de 0 con 1
    
    for indice,valor in enumerate(vector):
        if valor==0 and vector[indice-1]== 1 and vector[indice+1] !=-1:
            copiaVector[indice+1] =1
            copiaVector[indice] =1
        if valor ==-1 and vector[indice-1]==0 and vector[indice+1]==0:
            copiaVector[indice+1]=1
            copiaVector[indice-1]=1
    i=len(copiaVector)
    for indice2 in reversed(copiaVector):
        i-=1
        if indice2==1 and copiaVector[i-1]==0:
            copiaVector[i-1]=1
    return copiaVector


#Función para probar lo realizado
def main():
    print("--------------------------------------------------")
    p=propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
    print("ENTRADA: [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]")
    print("SALIDA: ",p) #SALIDA[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
    print("--------------------------------------------------")
    p2=propagar([ 0, 0, 0, 1, 0, 0])
    print("ENTRADA: [0, 0, 0, 1, 0, 0]")
    print("SALIDA: ",p2) #SALIDA:[ 1, 1, 1, 1, 1, 1]
    print("--------------------------------------------------")
    return "Fin función main()"

#print(main())