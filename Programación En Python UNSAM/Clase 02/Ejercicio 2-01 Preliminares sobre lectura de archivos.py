'''
------------------------------------------------------------------------------
Ejercicio 2.1: Preliminares sobre lectura de archivos
------------------------------------------------------------------------------
Primero, tratá de leer el archivo entero de una en una larga cadena:
------------------------------------------------------------------------------
'''

with open('C:/Users/Patricia/Desktop/Programacion_en_Python_UNSAM/ejercicios_python/Clase02/Data/camion.csv', 'rt') as f:
    data = f.read()
print(data)


#Utilizando un FOR para leer línea por línea
with open('C:/Users/Patricia/Desktop/Programacion_en_Python_UNSAM/ejercicios_python/Clase02/Data/camion.csv', 'rt') as f:
    print("Imprime utilizando FOR")    
    for line in f:
            print(line, end = '')


f = open('C:/Users/Patricia/Desktop/Programacion_en_Python_UNSAM/ejercicios_python/Clase02/Data/camion.csv', 'rt')
headers = next(f)
headers

print("\nImprime saltando la primer línea")
for line in f:
        print(line, end = '')
f.close() #porque no se utilizó WITH

print("\n")
f = open('C:/Users/Patricia/Desktop/Programacion_en_Python_UNSAM/ejercicios_python/Clase02/Data/camion.csv', 'rt')
headers =next(f).split(",")
print(headers)#solo imprimió la primer línea
for line in f:
    row = line.split(",")
    print(row)
f.close()
