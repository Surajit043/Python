import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

n=10000
mu=1
std_dev=0.5

x=normal(mu,std_dev,size=n)
x_av=np.mean(x)

def c(k):
	return np.mean([(x[i]-x_av)*(x[i+k]-x_av) for i in range (n-k)])

def r(k): return c(k)/c(0)
corr =[r(k) for k in range(1000)]
plt.plot(corr[1:])
plt.axhline( )
plt.show( )