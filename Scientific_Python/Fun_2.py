import numpy as np
import matplotlib.pyplot as plt
import pylab
t=np.arange(0,2*np.pi,0.1)
x=16*np.sin(t)**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
fig,ax=plt.subplots()
plt.plot(x,y,lw=3,color='red')
pylab.fill_between(x,y,color='crimson')
ax.set_aspect('equal')
plt.title('You & me',fontsize='35',color='navy')
pylab.text(0,2,'I Love You',fontsize='40',fontweight='bold',color='navy',horizontalalignment='center')
plt.show()
