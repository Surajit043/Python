# RandomWalk In 1D : Python script for animation view
import numpy as np
import matplotlib.pyplot as plt

x = 0
y = [x]
for t in range (10000):
    step=2*np.random.randint(2)-1       # +1 or -1
    x= x+step
    y.append(x)

    plt.cla()   #for dynamic ploting animation
    plt.plot(y)
    plt.pause(0.001)