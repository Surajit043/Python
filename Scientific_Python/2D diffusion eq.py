import numpy as np
import matplotlib.pyplot as plt

x = np. linspace (0,1,101)
y = np.linspace (0,1,101)
u = np.zeros ((101,101))
u[50,50] = 1

for time in range (200) :
    for i in range (1,100) :
        for j in range (1,100):
            u[i,j] += (u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i,j-1] -4*u[i,j])/4

plt.plot(x,u, color='b')
plt.plot (y,u, color='r')
plt.show()
plt.show()
