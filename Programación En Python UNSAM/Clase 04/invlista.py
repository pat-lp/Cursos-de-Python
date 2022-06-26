'''
-------------------------------------------------------------------------------
Ejercicio 4.05: Invertir una lista
-------------------------------------------------------------------------------
Escribí una función invertir_lista(lista) que dada una lista devuelva otra que 
tenga los mismos elementos pero en el orden inverso. Es decir, el que era el 
primer elemento de la lista de entrada deberá ser el último de la lista de 
salida y análogamente con los demás elementos.
-------------------------------------------------------------------------------
'''

def invertir_lista(lista):
    invertida = []
    for e in reversed(lista): # Recorro la lista
        invertida.append(e) #agrego el elemento e al principio de la lista invertida
    return invertida

#Función main con las pruebas realizadas de las funciones
def main():
    lista1= [1, 2, 3, 4, 5] 
    lista2= ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    
    print("\n--------------------------------------------------------")
    print("{:^55}".format('INVERTIR LISTA'))
    print("--------------------------------------------------------")
    print(f"Lista original:  {lista1}\nLista invertida: {invertir_lista(lista1)}\n")
    print(f"Lista original:  {lista2}\nLista invertida: {invertir_lista(lista2)}\n")
    return "Fin función main()"

#print(main())
