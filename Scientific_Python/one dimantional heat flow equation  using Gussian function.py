'''
one dimentional heta flow on insulated rod
d(theta)/dt = h* d**2(theta)/d*x**2

'''


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace (0,1,101)
theta = np.zeros (101)

u = np.exp(-(x - 0)**2/0.001)
plt.plot(x,u,'--', label = 'Initial' , c='y',lw = 1.5)

for time in range(100):
    for i in range(1, 100):
        u[i] += (u[i+1] - 2*u[i] + u[i-1])/4.

# for 2D plot
plt.plot(x,u, label='Latter' ,lw = 1.5 , c= 'b')
plt.title (' 1D Heat Flow On a Insulated Metal Bar ' ,size ='17')
plt.xlabel ('Time ----->',size = '14')
plt.ylabel('Heat Flow ----->', size ='14')
plt.legend()
plt.show()

# for 3D plot
from matplotlib import cm
from mpl_toolkits import mplot3d
X,T = np.meshgrid (x,theta)
ax = plt.axis(projection='3d')
ax.plot_surface (X,T,theta,camp=cm.coolwarm)
plt.show ( )
