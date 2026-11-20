import numpy as np

A = np.array([[4, 1], [2, 3]])
B = np.array([9, 13])

x = np.zeros(2)

for i in range(10):
    x_new = (B - (A @ x - np.diag(A) * x)) / np.diag(A)
    x = x_new

print("Solution:", x)