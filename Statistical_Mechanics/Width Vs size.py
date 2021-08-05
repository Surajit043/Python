# Python script: Width vs. system size
import numpy as np
from numpy.random import randint

f = lambda n: [sum(randint(2, size=n)) for i in range(trial)]

n, trial = 10, 10000
N, Y = [], []

for i in range(10):
    x, y = np.unique(f(n), return_counts=True)
    x = x / n  # Normalized by width
    p = y / trial  # Probability
    d = np.sqrt(sum(x * x * p) - (sum(x * p)) ** 2)  # Width
    Y.append(d)
    N.append(n)
    n = n * 2

# For plotting
import matplotlib.pyplot as plt

fit = np.array(N) ** (-0.5)
plt.loglog(N, Y, 'o', N, fit, '-', lw=2)
plt.ylabel('Width', size=20)
plt.xlabel('system size', size=20)
plt.show()