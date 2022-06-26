'''
-------------------------------------------------------------------------------
Ejercicio 9.2: Agregá algunos métodos
-------------------------------------------------------------------------------
Agregá los métodos costo() y vender() a tu objeto Lote. 
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
        