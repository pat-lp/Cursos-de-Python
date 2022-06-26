'''
------------------------------------------------------------------------------
Training y testing
------------------------------------------------------------------------------
X_train shape: (112, 4)
y_train shape: (112,)
X_test shape: (38, 4)
y_test shape: (38,)
------------------------------------------------------------------------------
'''

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)