# Random Walk in 1D : To compute configaration avarage value
import numpy as np
import matplotlib.pyplot as plt
# N = Ensemble Number , T = Total time attemps
N , T = 10000 , 1000
t = range(1,T+1)        # Time Scale
# 2D array: Time Axis along row , each row is one configaration
walks = 2*np.random.randint(2,size = (N,T))-1
# Compute Config Avarage
position = np.cumsum(walks , axis=1)
pos_sq = position**2
mean_pos_sq = np.mean(pos_sq,axis=0)
rms = np.sqrt(mean_pos_sq)      #root mean square distance

# alues in log Scale
t = np.log (t)
rms = np.log (rms)
# to fit log values in linear scale
import numpy.polynomial.polynomial as poly
coeffs = poly.polyfit(t,rms ,1)
rmsfit = poly.polyval(t,coeffs)
print (coeffs)
# to plot data along with fitted curve
plt.plot(t[: : 50],rms[: : 50], 'o' , t, rmsfit, '-')
plt.xlabel('log(time)' , fontsize = 18)
plt.ylabel('log($R_{rms}$)' , fontsize = 18)
plt.title ('Random Walk In 1D' , fontsize = 20)
plt.show()
