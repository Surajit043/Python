'''
evaluate the gamma function
calculate gamma(1\2)

'''
import numpy as np
from scipy.integrate import quad
from numpy import sqrt , pi
y = sqrt(pi)
def f(z) :
	return z**(-0.5)*np.exp(-z)
ans,err = quad(f,0,np.inf)
result =(ans,err)/y

print (result)
