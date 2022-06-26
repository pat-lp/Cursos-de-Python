'''
------------------------------------------------------------------------------
Ejercicio 10.4: Un generador simple
------------------------------------------------------------------------------
Este generador que busca un archivo y entrega las líneas que incluyen cierto substring.
------------------------------------------------------------------------------
'''

def filematch(filename, substr):
    with open(filename, 'r')as f:
        for line in f:
            if substr in line:
                yield line
                
for line in open('../Data/camion.csv'):
    print(line, end='')
    
print()

for line in filematch('../Data/camion.csv', 'Naranja'):
    print(line, end='')