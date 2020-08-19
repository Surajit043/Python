'''
one dimentional heta flow 
d(u)/dt = c^2* d**2(u)/d*x**2

'''


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace (0,1,101)
theta = np.zeros (101)

v = np.exp(-(x - 0)**2/0.001)
plt.plot(x,v,'--', label = 'Initial' , c='y',lw = 1.5)

for time in range(100):
    for i in range(1, 100):
        v[i] += (v[i+1] - 2*v[i] + v[i-1])/4. #concider c^2 is equal to 4

# for 2D plot
plt.plot(x,v, label='Latter' ,lw = 1.5 , c= 'b')
plt.title (' 1D Heat Flow ' ,size ='20')
plt.xlabel ('Time ----->',size = '14')
plt.ylabel('Heat Flow ----->', size ='14')
plt.legend()
plt.show()
