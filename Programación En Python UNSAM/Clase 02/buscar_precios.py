'''
------------------------------------------------------------------------------
Ejercicio 2.7: Buscar precios
------------------------------------------------------------------------------
Escribir una función buscar_precio(fruta) que busque en archivo 
../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en 
pantalla. Si la fruta no figura en el listado de precios, debe imprimir un 
mensaje que lo indique.
------------------------------------------------------------------------------
'''
def buscar_precio(fruta):
    encontrado=False
    f = open('Data/precios.csv','rt')
    next(f) 
    for line in f:
        row=line.split(",")
        if row[0] == fruta:
            print("El precio de un cajón de {} es: {}".format(fruta,row[1]))
            encontrado=True
    if not encontrado:
        print("{} no figura en el listado de precios.".format(fruta))
    f.close()

print("\n-----------------------------------------------\n")
buscar_precio('Kale')
buscar_precio('Frambuesa')
print("-----------------------------------------------")
