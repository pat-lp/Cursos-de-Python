'''
-------------------------------------------------------------------------------
Ejercicio 9.1: Objetos como estructura de datos.
-------------------------------------------------------------------------------
Otra forma de representar los datos con los que estás trabajando es definir una
clase. Creá un archivo llamado lote.py y adentro definí una clase llamada Lote
que represente un lote de cajones de una misma fruta. Definila de modo que cada 
instancia de la clase Lote (es decir, cada objeto lote) tenga los atributos 
nombre, cajones, y precio. Éste es un ejemplo del comportamiento buscado:
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
        #return f'{self.nombre}, {self.cajones}, {self.precio}'
        return f'Lote de {self.cajones} cajones de {object.__str__(self.nombre)}, pagados a ${self.precio} cada uno.'
        
    def __repr__(self):
        return f'Lote({object.__str__(self.nombre)}, {self.cajones}, {self.precio})'


def f_principal():
    peras = Lote('Pera', 100, 490.1)
    print(repr(peras))
    
if __name__ == "__main__":
    f_principal()