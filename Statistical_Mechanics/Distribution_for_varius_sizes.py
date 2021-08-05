# Python script: Distributions for vartious system sizes
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

# Function to create list of head's
f = lambda n: [sum(randint(2, size=n)) for i in range(trial)]

markers = ['o', '^', 'p']
n, trial = 10, 10000

for i in range(3):
    x, y = np.unique(f(n), return_counts=True)
    x = x / n
    y = y / np.max(y)

    plt.plot(x, y, marker=markers[i])
    n = n * 10

plt.legend(['n = 10', 'n = 100', 'n = 1000'])
plt.show()