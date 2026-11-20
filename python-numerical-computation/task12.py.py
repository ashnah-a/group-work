import numpy as np

A = np.array([[2, 1], [1, 1]], dtype=float)
B = np.array([5, 3], dtype=float)

n = len(B)

for i in range(n):
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]
        B[j] = B[j] - factor * B[i]

x = np.zeros(n)
x[-1] = B[-1] / A[-1, -1]

for i in range(n - 2, -1, -1):
    x[i] = (B[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

print("Solution:", x)