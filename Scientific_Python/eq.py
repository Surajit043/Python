import numpy as np
import matplotlib.pyplot as plt


x= np.linspace(0,1,360)
v = []
for t in range (0,360):
    u = lambda (x): ((np.cos(0.5*t)+np.sin (0.5*t))*np.exp ((1/4)**2*(0.5)**2*t))
    v.append(u)
    #return u
plt.plot(x,v)
plt.show()
