import numpy as np
import matplotlib.pyplot as plt

T0 , L = 1,1
x = np.linspace (0,L,101)
u = T0*np.ones(101)
u[0] ,u[100] = 0,0

for time in range (100):
    u[1:-1] += 0.25*(u[2:] - 2*u[1:-1] + u[:-2])

t = 1.0/300
f = lambda m : 2.0/(2*m-1)*2*T0/np.pi*np.exp(-((2*m-1)*np.pi/L)**2*t)*np.sin((2*m-1)*np.pi/L*x)
exact = sum ([f(m) for m in range (1,20)])

plt.plot (x,u,'o',x,exact,lw='3')
plt.show ()
