'''
ARCHIVO DADO POR LA CATEDRA
'''
import informe_final
import lote

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    camion = [lote.Lote(d.nombre, d.cajones, d.precio) for d in camion]
    return sum([c.costo() for c in camion])

def f_principal(archivo):
    costo = costo_camion(archivo) 
    print(f'Costo total: {costo}')
#%%    
if __name__ == '__main__':
    f_principal('../Data/camion.csv')
    






















