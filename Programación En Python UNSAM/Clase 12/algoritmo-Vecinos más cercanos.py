'''
------------------------------------------------------------------------------
Algoritmo vecinos más cercanos
------------------------------------------------------------------------------

------------------------------------------------------------------------------
'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt


iris_dataset = load_iris()


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)


#Creamos una instancia de la clase KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)

#Y la entrenamos con los datos de entrenamiento

knn.fit(X_train, y_train)


X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)


plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))