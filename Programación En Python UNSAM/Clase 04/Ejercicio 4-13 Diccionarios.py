'''
-------------------------------------------------------------------------------
Ejercicio 4.13: Diccionarios
-------------------------------------------------------------------------------
'''

import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

#select = ['nombre', 'cajones','precio']
#indices = [headers.index(ncolumna) for ncolumna in select]
#print(indices)#[0,1,2]

types = [str, int, float]

r = list(zip(types, row))
print("zip\n",r)

converted =[]

for func,val in zip(types, row):
    converted.append(func(val))
    
    
print("Converted:",converted)

print("Multiplicación:",converted[1] * converted[2])

converted = [func(val) for func,val in zip(types,row)]

print("Converted:",converted)

#%%

print(headers)#['nombre', 'cajones', 'precio']

print(converted)#['Lima', 100, 32.2]

print(dict(zip(headers,converted)))

#{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}

print({ name: func(val) for name,func,val in zip(headers,types,row)  })