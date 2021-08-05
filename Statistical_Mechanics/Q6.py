import numpy as np
import matplotlib.pyplot as plt
N=1000 #number of walks
T=200 #total no of time steps
t=range(1,T+1)
walks=2*np.random.randint(2,size=(N,T))-1
#for config average
pos=np.cumsum(walks,axis=1)
pos_sq=pos**2
mean_pos_sq=np.mean(pos_sq,axis=0)
rms=np.sqrt(mean_pos_sq)
#Value in log scale
t=np.log(t)
rms=np.log(rms)
#for data fitting
import numpy.polynomial.polynomial as poly
coeffs=poly.polyfit(t,rms,1)
rmsfit=poly.polyval(t,coeffs)
#plotting
plt.plot(t[::50],rms[::50],'o',t,rmsfit,'-')
plt.xlabel('log(time)',fontsize=18)
plt.ylabel('log($R_{rms}$)',fontsize=18)
plt.title('Random walk in 1D',fontsize=22,color='r')
plt.show( )