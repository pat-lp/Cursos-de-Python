'''
-------------------------------------------------------------------------------
Ejercicio formato tabla
-------------------------------------------------------------------------------
'''


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        return NotImplementedError()
    
    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        return NotImplementedError()
    
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end = ' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV.
    '''
    def encabezado(self, headers):
        print(','.join(headers))
        
    def fila(self, data_fila):
        print(','.join(data_fila))
        

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')
    
    def fila(self, data_fila):
        print('<tr>', end = '')
        for d in data_fila:
            print(f'<td>{d}</td>', end = '')
        print('</tr>')

def crear_formateador(fmt):
    ''''
    Elige el formato según elección del usuario
    '''
    if fmt == 'txt':
        return FormatoTablaTXT()
    elif fmt == 'csv':
        return FormatoTablaCSV()
    elif fmt == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
        

def imprimir_tabla(camion, columnas, formateador):
    formateador.encabezado(columnas)
    for lote in camion:
        colname = [f'{getattr(lote, colname)}' for colname in columnas]
        formateador.fila(colname)
        
        
'''
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        p = '$'+str(precio)
        rowdata = [nombre, str(cajones), f'{p}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
'''