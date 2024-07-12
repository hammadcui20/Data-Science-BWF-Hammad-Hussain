import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

print("Array + 2:", array + 2)
print("Array * 3:", array * 3)

matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

print("Matrix Transpose:\n", matrix.T)
print("Matrix Determinant:", np.linalg.det(matrix))
