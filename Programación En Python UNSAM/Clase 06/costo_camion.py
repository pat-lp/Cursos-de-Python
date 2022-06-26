'''
-------------------------------------------------------------------------------
Ejercicio "costo_camion"
-------------------------------------------------------------------------------
'''

from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    costoTotal=0
    for i in leer_camion(nombre_archivo):
         try:
            costoTotal+=int(i['cajones'])*float(i['precio'])
         except ValueError:
            print("Error")
    return costoTotal


def main():
    '''
    Función main() creada para probar lo realizado.
    '''
    costoTotal=costo_camion('../Data/camion.csv')
    print("------------------------------------------------------------")
    print("El costo total por los cajones cargados es de: ",costoTotal) #47671.15
    print("------------------------------------------------------------")
    return "\nFin función main()"

#print(main())