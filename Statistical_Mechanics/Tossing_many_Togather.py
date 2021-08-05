# Python scripts: Tossing of many coins together
import numpy as np
from numpy.random import randint

n, trial = 100, 100000
f = [sum(randint(2, size = n)) for i in range(trial)]

x, y = np.unique(f, return_counts = True )
y = y/np.max(y)

# For plotting
import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.show()