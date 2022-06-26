'''
-------------------------------------------------------------------------------
Ejercicio "costo_camion"-Clase 07
-------------------------------------------------------------------------------
'''

from informe_final import leer_camion

def costo_camion(nombre_archivo):
    costoTotal = 0
    for i in leer_camion(nombre_archivo):
         try:
            costoTotal += int(i['cajones']) * float(i['precio'])
         except ValueError:
            print("Error")
    return costoTotal


def f_principal(archivo_camion):
    '''
    Función main() utiliza además el modulo informe
    para imprimir leer_camion
    '''
    costoTotal = costo_camion(archivo_camion)
    print("------------------------------------------------------------")
    print("El costo total por los cajones cargados es de: ", costoTotal) #47671.15
    print("------------------------------------------------------------")
    

if __name__=="__main__":
    f_principal('../Data/camion.csv')