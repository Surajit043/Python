# Python Script: Simulation of coin tossing
import numpy as np
n = 100000
N = range (1,100000)
X = np.random.choice ([0,1], size = n)
Y = [np.sum(X[:i])/i for i in N]
z = np.average(Y)
print(z)
# plot to see
import matplotlib.pyplot as plt
plt.plot(N, Y)
plt.show ()

# Estimate The Value Of Pi By Using Random Numbers
from numpy.random import uniform as u
n=1000              # no Of Trials
inside = sum(u(-1,1,n)**2 + u(-1,1,n)**2 <= 1)
pi = 4.0*inside / n
print ("Value Of Pi = " , pi)

