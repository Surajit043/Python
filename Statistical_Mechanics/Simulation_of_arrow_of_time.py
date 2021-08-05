# Python Script: Simulation of arrow of time
import numpy as np
from numpy.random import uniform, randint
import matplotlib.pyplot as plt

N = 100  # Number of particles
L = np.full((N,), 1)  # All the particles are indexed 1

T = range(1000)
S = []

for t in T:
    i = randint(0, 100)
    p = sum(L) / N
    if uniform(0, 1) < p:
        if L[i] == 1: L[i] == 0
    else:
        if L[i] == 0: L[i] == 1

    S.append(sum(L))

# For plotting
plt.plot(T, S)
plt.xlabel('Time', size=16)
plt.ylabel('No. of particles on left', size=16)
plt.show()