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