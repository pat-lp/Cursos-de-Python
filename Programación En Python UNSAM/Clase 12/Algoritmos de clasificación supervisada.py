'''
------------------------------------------------------------------------------
Algoritmos de clasificación supervisada
------------------------------------------------------------------------------
'''

from sklearn.datasets import load_iris

iris_dataset = load_iris()

print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())

#Las flores se clasifican en tres:
print("Target names:", iris_dataset['target_names'])

#Y los atributos son cuatro por cada flor:
print("Feature names:\n", iris_dataset['feature_names'])

#Son 150 flores etiquetadas, con cuatro atributos cada una, en un array de numpy. Las etiquetas son 0, 1 y 2 y se guardan también en un array:
    
print("Type of data:", type(iris_dataset['data']))
print("Shape of data:", iris_dataset['data'].shape)
print("First five rows of data:\n", iris_dataset['data'][:5])
print("Type of target:", type(iris_dataset['target']))
print("Shape of target:", iris_dataset['target'].shape)
print("Target:\n", iris_dataset['target'])

#%% VISUALIZACION DE DATOS

import pandas as pd
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)