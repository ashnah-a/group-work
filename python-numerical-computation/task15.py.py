import numpy as np

A = np.array([[4, 1], [2, 3]])
B = np.array([9, 13])

x = np.zeros(2)

for i in range(10):
    x[0] = (9 - x[1]) / 4
    x[1] = (13 - 2*x[0]) / 3

print("Solution:", x)