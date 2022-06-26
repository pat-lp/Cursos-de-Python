'''
-------------------------------------------------------------------------------
Ejercicio 4.14: Fijando ideas
-------------------------------------------------------------------------------
'''

import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

print(headers)

print(row)

types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func,val in zip(types, row)]

record = dict(zip(headers,converted))

print(record)

print(record['name'])

print(record['price'])

#%%  Modificar la fecha(date) en una tupla como(6,11,2007)


types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func,val in zip(types, row)]

record = dict(zip(headers,converted))

print(record)

print("fecha a tupla")
print(','.join(tuple(record['date'].split('/'))))

tup=tuple(record['date'].split("/"))
print(tup)


#res = tuple(map(int, test_str.split(', ')))
  

