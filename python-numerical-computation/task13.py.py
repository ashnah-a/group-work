import numpy as np
from scipy.linalg import lu

A = np.array([[2, 1], [4, 3]])

P, L, U = lu(A)

print("Lower matrix:")
print(L)

print("Upper matrix:")
print(U)