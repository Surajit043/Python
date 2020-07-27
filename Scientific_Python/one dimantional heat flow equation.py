'''
one dimentional heta flow on insulated rod
d(theta)/dt = h* d**2(theta)/d*x**2

'''


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (0,1,101)
theta = np.zeros (101)

theta[0] = 1
plt.plot(x,theta , '--' , label = 'Initial', lw= 1.5 ,c= 'y')

for time in range (100):
    for i in range (1,100):
        theta[i] += (theta[i+1] - 2*theta[i] + theta[i-1])/6

plt.plot(x,theta, label = 'Latter' , color = 'b',lw='2')
plt.title (' 1D Heat Flow On a Insulated Metal Bar ' ,size ='17')
plt.xlabel ('Time ----->' , size ='14')
plt.ylabel ('Heat Flow ----->' , size = '14')
plt.legend()
plt.show()
