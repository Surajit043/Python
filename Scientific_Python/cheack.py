import numpy as np
from scipy.special import legendre
import matplotlib.pyplot as plt
a = np.arange(-1,1,0.01)
for i in range (1,10):
      pi = legendre(i)
      plt.plot(a,pi(a))

plt.show( )
