"""
Enunciado:
Utiliza NumPy para crear y manipular matrices. Implementa dos funciones, create_matrices() y manipulate_matrices().
La función create_matrices() debe crear una matriz de ceros de tamaño 3x3, una matriz de unos de tamaño 2x4, y una
matriz identidad de tamaño 4x4.
La función manipulate_matrices() debe modificar estas matrices:
En la matriz de ceros, cambia el valor del elemento en la fila 2, columna 2 al valor de 5; En la matriz de unos, cambia
toda la tercera columna a 3; y en la matriz identidad, cambia la diagonal secundaria a 2.

Parámetros:

    - La función create_matrices() no recibe parámetros y devuelve las tres matrices creadas.
    - manipulate_matrices(zeros_matrix: np.ndarray, ones_matrix: np.ndarray, identity_matrix: np.ndarray) recibe las
    tres matrices creadas y devuelve las tres matrices modificadas.

Nota: recomendamos anotar las dos funciones (como aprendimos en el B1). Los tipos correspondientes seran: 
para matrices de NumPy usaremos el objeto `np.ndarray` y para agrupar la salida de una función usaremos el objeto 
`typing.Tuple` para señalar que la salida de una función son más de una matriz. 

Ejemplo:
    def create_matrices() -> np.ndarray:
        ...

    def manipulate_matrices(
        zeros_matrix: np.ndarray, 
        ones_matrix: np.ndarray, 
        identity_matrix: np.ndarray
    ) -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
        ...

    Entrada:
    zeros_matrix, ones_matrix, identity_matrix = create_matrices()
    manipulate_matrices(zeros_matrix, ones_matrix, identity_matrix)

    Salida:
    [array([[0. 0. 0.]
            [0. 5. 0.]
            [0. 0. 0.]]),
     array([[1. 1. 3. 1.]
            [1. 1. 3. 1.]]),
     array([[1. 0. 0. 2.]
            [0. 1. 2. 0.]
            [0. 2. 1. 0.]
            [2. 0. 0. 1.]])]
"""
import numpy as np
import typing as t


def create_matrices() -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # np.zeros recibe una tupla con las dimensiones de la matriz (filas, columnas)
    zeros_matrix = np.zeros((3,3))
    # np.ones hace lo mismo pero la crea con 1 en lugar de 0.
    ones_matrix = np.ones((2,4))
    # np.eye crea una matriz cuadrada con unos en la diagonal y ceros en el resto
    identity_matrix = np.eye(4)
    return zeros_matrix, ones_matrix, identity_matrix


def manipulate_matrices(
    zeros_matrix: np.ndarray, ones_matrix: np.ndarray, identity_matrix: np.ndarray
) -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Para acceder a un elemento de la matriz usamos matriz[fila, columna]
    # OJO que python empieza a contar las filas y columnas desde 0.
    zeros_matrix[1, 1] = 5
    # Para seleccionar una columna se utiliza matriz[:,columna]
    ones_matrix[:,2] = 3
    # matriz.shape te permite calcualar el tamaño de la matriz: .shape[0] nº de filas, .shape [1] nº de columnas
    for fila in range(identity_matrix.shape[0]):
        # Para acceder a la diagonal secundaria: columna = tamaño_matriz - 1 - fila
        columna = identity_matrix.shape[0] - 1 - fila
        identity_matrix[fila, columna] = 2 
    return zeros_matrix, ones_matrix, identity_matrix


# Para probar el código:
zeros_matrix, ones_matrix, identity_matrix = create_matrices()
print("Matriz de ceros creada:\n", zeros_matrix)
print("Matriz de unos creada:\n", ones_matrix)
print("Matriz identidad creada:\n", identity_matrix)
print("*" * 50)
zeros_matrix_modif, ones_matrix_modif, identity_matrix_modif = manipulate_matrices(
    zeros_matrix,
    ones_matrix,
    identity_matrix
)
print("Matriz de ceros modificada:\n", zeros_matrix_modif)
print("Matriz de unos modificada:\n", ones_matrix_modif)
print("Matriz identidad modificada:\n", identity_matrix_modif)
