import numpy as np
def MCI () :
	x=np.random.uniform(a,b,N)
	return (b-a)*np.mean(f(x))
f=lambda x:x*x
N=10000
a,b=0,2
print (MCI())
X=[MCI() for i in range (10000)]
import matplotlib.pyplot as plt
with plt.xkcd() :
	plt.hist (X, bins = 40, color = 'k', ec = 'w')
	plt.show()