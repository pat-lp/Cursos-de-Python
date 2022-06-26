'''
ARCHIVO DADO POR LA CATEDRA
'''
import informe_final


def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()

def f_principal(archivo):
    costo = costo_camion(archivo) 
    print(f'Costo total: {costo}')
    
#%%    
if __name__ == '__main__':
    f_principal('../Data/camion.csv')
    

















