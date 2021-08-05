# Python Script: Monte carlo Integration
import numpy as np
f = lambda x: (3)/(np.pi*(9+x**2)) # def function
def MonteCarloInt(a, b, f):
    N = 100000
    x = np.linspace(a, b, 1000)
    y_min = 0
    y_max = np.max(f(x)) + 1
    A = (b - a) * (y_max - y_min)

    x = np.random.uniform(a, b, N)
    y = np.random.uniform(y_min, y_max, N)
    n = np.sum([abs(y) < abs(f(x))])

    return A * n / N
print(MonteCarloInt(0, 1 , f))