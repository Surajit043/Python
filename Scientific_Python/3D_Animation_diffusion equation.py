import numpy as np

x=np.linspace(0,1,101)
t=np.linspace(0,100,101)
u = np.zeros([101,101])
u[0][50] = 1

for j in range(1,100):
	u[j] = u[j-1]
	for i in range(1,100):
		u[j,i] +=(u[j,i+1]-2*u[j,i]+u[j,i-1])/4

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
X,T=np.meshgrid(x,t)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,T,u,cmap=cm.coolwarm)
plt.show()
