import random

total = 10000
sum_y = 0

for i in range(total):
    x = random.random()
    sum_y += x**2

result = sum_y / total

print("Estimated integral =", result)