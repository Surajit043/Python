import numpy as np
n = 100000
N = range (1,100000)
X = np.random.choice ([0,1], size = n)
Y = [np.sum(X[:i])/i for i in N]

# plot to see
import matplotlib.pyplot as plt
plt.plot(N, Y)
plt.show ()
