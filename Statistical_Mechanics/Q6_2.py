import numpy as np
import matplotlib.pyplot as plt
N=1000 #number of walks
T=200 #total no of time steps
t=range(1,T+1)
walks=2*np.random.randint(2,size=(N,T))-1
plt.plot(np.cumsum(walks))
plt.xlabel('Time', fontsize = 18)
plt.ylabel('Cumalative Position (x) ' , fontsize = 18)
plt. title ('Random Walk in ID', fontsize = 20)
plt.show()

