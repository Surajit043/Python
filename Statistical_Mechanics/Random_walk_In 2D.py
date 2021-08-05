#python script : generation og=f 2D Random Walk
import numpy as np
from random import choice
import matplotlib.pyplot as plt
x,y = 0,0
X , Y = [x],[y]
for i in range (5000) :
    dx,dy = choice([(1,0),(-1,0),(0,1),(0,-1)])
    x,y = x+dx , y+dy
    X.append((x))
    Y.append(y)
plt.plot(X , Y , c= 'k')
plt.show()