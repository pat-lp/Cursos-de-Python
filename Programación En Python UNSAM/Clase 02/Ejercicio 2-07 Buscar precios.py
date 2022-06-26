'''
------------------------------------------------------------------------------
Ejercicio 2.7: Buscar precios
------------------------------------------------------------------------------
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función 
buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de 
determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura 
en el listado de precios, debe imprimir un mensaje que lo indique.

>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.
Guardá este código en un archivo buscar_precio.py para entregar al final de la clase.
------------------------------------------------------------------------------
'''
def buscar_precio(fruta):
    encontrado=False
    f = open('Data/precios.csv','rt') #abro archivo
    next(f) #salto el encabezado
    for line in f:
        row=line.split(",")
        if row[0] == fruta: #Busco línea por línea
            print("El precio de un cajón de {} es: {}".format(fruta,row[1]))
            encontrado=True
    if not encontrado:
        print("{} no figura en el listado de precios".format(fruta))
    f.close()

print("\n-----------------------------------------------\n")
buscar_precio('Kale')
buscar_precio('Frambuesa')
print("-----------------------------------------------")
