'''
------------------------------------------------------------------------------
Ejercicio 2.3: Precio de la naranja
------------------------------------------------------------------------------
El archivo Data/precios.csv contiene una serie de líneas con precios de venta 
de cajones en el mercado al que va el camión. El archivo se ve así:
"Lima",40.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",53.72
...
Escribí un código que abra el archivo Data/precios.csv, busque el precio de la
naranja y lo imprima en pantalla.
>>> f = open('../Data/precios.csv', 'rt')
...
>>> f.close()

El precio de la naranja es:  106.28
------------------------------------------------------------------------------
'''


f = open('Data/precios.csv','rt') #abro archivo
next(f) #salto el encabezado
for line in f:
    if "Naranja" in line: #Busco línea por línea
        row=line.split(",") #fragmento la línea para obtener el precio
        print("El precio de la naranja es: ",row[1])
    
f.close()
