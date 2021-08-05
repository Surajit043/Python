# Python Script: Simulation of coin tossing
import matplotlib.pyplot as plt
import numpy as np
# 1st part
n = 100000
N = range (1,100000)
X = np.random.choice ([0,1], size = n)
Y = [np.sum(X[:i])/i for i in N]
# plot to see
plt.plot(N, Y)
plt.show ()

# 2nd part

def coinFlip(size):
    flips = np.random.randint(0, 2, size=size)
    return flips.mean()
coinFlip = np.frompyfunc(coinFlip, 1, 1)

xmin, xmax, dx = 1, 10000, 1
x = np.arange(xmin, xmax, dx)
y = coinFlip(x)
plt.plot(x, y)
plt.show()