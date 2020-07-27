# Python Script for Diffusion in 1D
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 101)
u = np.exp(-(x - 0.5)**2/0.001)

plt.plot(x,u,label= 'initial',c='b',lw='2')
#plt.show( )

for time in range(100):
    for i in range(1, 100):
        u[i] += (u[i+1] - 2*u[i] + u[i-1])/4.
plt.plot(x,u,label= 'after',c='r',lw='2')
plt.show()
