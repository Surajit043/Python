#PDE for diffusion in 1D
import numpy as np
import matplotlib.pyplot as plt
L=1
x=np.linspace(0,L,101)
u=np.zeros(101)
u[0]=0
u[100]=0
u[50]=1
for time in range(100):
	for i in range(1,100):
		u[i] +=(u[i+1]-2*u[i]+u[i-1])/4

	plt.cla()
	plt.plot(x,u,c='b',lw=2)
	plt.pause(0.001)

