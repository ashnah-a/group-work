from scipy.optimize import minimize_scalar

def f(x):
    return -((x-2)**2) + 10

result = minimize_scalar(
    lambda x: -f(x),
    bounds=(0, 4),
    method='bounded'
)

print("Maximum x =", result.x)
print("Maximum value =", f(result.x))