'''
-------------------------------------------------------------------------------
Ejercicio 9.9: Mejor salida para objetos
-------------------------------------------------------------------------------
Modificá el objeto Lote que definiste en lote.py (del Ejercicio 9.2) de modo 
que el método __repr__() genere una salida más agradable. 
-------------------------------------------------------------------------------
'''

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        return self.cajones * self.precio
        
    def vender(self, cantidad):
        self.cajones -= cantidad
        
        
    def __str__(self):
        return f'{self.nombre}, {self.cajones}, {self.precio}'
        
    def __repr__(self):
        return f'Lote({object.__str__(self.nombre)}, {self.cajones}, {self.precio})'


def f_principal():
    peras = Lote('Pera', 100, 490.1)
    print(repr(peras))
    
if __name__ == "__main__":
    f_principal()