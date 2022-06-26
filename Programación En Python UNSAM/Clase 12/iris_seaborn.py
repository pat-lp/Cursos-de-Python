'''
------------------------------------------------------------------------------
Ejercicio 12.10: Seaborn
------------------------------------------------------------------------------
Repetí el gráfico anterior pero usando seaborn en lugar de pandas para graficar, 
y guardá el código correspondiente en un archivo iris_seaborn.py para entregarlo.

Sugerencia: Usando iris_dataframe['target'] = iris_dataset['target'], agregá 
al DataFrame el atributo target de cada flor para poder hacer un sns.pairplot() 
seteando hue sobre las especies de iris.
------------------------------------------------------------------------------
'''


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris_dataset = load_iris()

iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
iris_dataframe['target'] = iris_dataset['target']

sns.set_style('darkgrid')
sns.pairplot(data= iris_dataframe, hue='target', palette='Dark2', diag_kind='hist', markers=['o','s','D'], height=3, aspect=1)
plt.show()

