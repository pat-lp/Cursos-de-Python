'''
------------------------------------------------------------------------------
Ejercicio 10.14: Expresiones generadoras como argumentos en funciones
------------------------------------------------------------------------------
'''

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes) #expresión generadora
    
    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, item):
        return self.lotes[item]
    
    def precio_total(self):
        return sum(l.costo() for l in self.lotes) #expresión generadora
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

    def __str__(self):
        t = [f'Camion con {self.lotes.__len__()} lotes:\n']
        for obj in self.lotes:
            s = str(obj.__str__())
            t.append(s)
        return ''.join(t)
    
    def __repr__(self):
        return f'Camion({self.lotes})'