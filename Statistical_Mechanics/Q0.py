import numpy as np
from random import randint
from matplotlib import pyplot as plt

num = 4
result = [ ]
for i in range (100000):
    throw = [randint(1,6) for r in range(num)]
    s = sum([j for j in throw])
    result.append(s)

arr = np.array(result)
print ("Total number appearing in 4 dice =" ,arr)
plt.hist(arr)
plt.title('Histogram For Relative Frequency')
plt.xlabel('simulations for 4 outcome')
plt.ylabel('Frequency of simulation')
plt.show()