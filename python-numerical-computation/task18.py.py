import random

inside = 0
total = 10000

for i in range(total):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        inside += 1

pi = 4 * inside / total

print("Estimated Pi =", pi)