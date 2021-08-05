# Estimate The Value Of Pi By Using Random Numbers
from numpy.random import uniform as u
n=1000              # no Of Trials
inside = sum(u(-1,1,n)**2 + u(-1,1,n)**2 <= 1)
pi = 4.0*inside / n
print ("Value Of Pi = " , pi)

