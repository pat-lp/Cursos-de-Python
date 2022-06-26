'''
-------------------------------------------------------------------------------
Ejercicio 8.5: Recorrer el árbol de archivos
-------------------------------------------------------------------------------
Definí una función llamada archivos_png(directorio) que arme una lista de todos 
los archivos .png que se encuentren en algún subdirectorio directorio dado.

Probá tu función con distintos directorios. Por ejemplo:

>>> archivos_png('../Data/ordenar')
['good_code_20190621.png',
 'git_20190503.png',
 'correlation_20200924.png',
 'duty_calls_20180321.png',
 'pregnant_20200102.png',
 'ppx_20180917.png',
 'twitter_bot_20181225.png',
 'standards_20190421.png',
 'unicode_20200718.png',
 'sandwich_20201002.png',
 'python_20190812.png']
-------------------------------------------------------------------------------
'''

import os


def archivos_png(directorio):
    '''
    Genera una lista con los archivos .png de un directorio o subdirectorio.
    Pre: Recibe un directorio
    Pos: Devuelve una lista con todas las imágenes .png que se encuentran en el 
    directorio/subdirectorio dado.
    '''
    lista_imagenes = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if '.png' in name:
                lista_imagenes.append(name)
        for name in dirs:
            if '.png' in name:
                lista_imagenes.append(name)
    return lista_imagenes

def f_principal():
    imagenes_png = archivos_png('../Data/ordenar')
    print("\n\t\t\t Lista imágenes .png\n\n",imagenes_png)
    

if __name__ == "__main__":
    f_principal()
    
