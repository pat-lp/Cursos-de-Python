'''
------------------------------------------------------------------------------
Ejercicio 10.3: Un iterador adecuado
------------------------------------------------------------------------------
'''

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    
    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, i):
        return self.lotes[i]
    
    def precio_total(self):
        return sum([l.costo() for l in self.lotes])
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
print('Naranja' in camion)#True
print('Manzana' in camion)#False

print(len(camion))#7
print(camion[0])#Lote('Lima', 100, 32.2)
print(camion[1])#Lote('Naranja', 50, 91.1)
print(camion[0:3])#[Lote('Lima', 100, 32.2), Lote('Naranja', 50, 91.1), Lote('Caqui', 150, 103.44)]
print()

#%%
print(camion)