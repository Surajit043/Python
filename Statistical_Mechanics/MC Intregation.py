# MC integration
import numpy as np
f = lambda x: np.sin(x)

def MCI ():
    x = np.random.uniform(a, b, N)
    return (b - a)*np.mean(f(x))
N = 10000
a, b = 0, np.pi
MCI ()
x = [MCI () for i in range(10000)]
import matplotlib.pyplot as plt
with plt.xkcd():
    plt.hist(x, bins = 40, color = 'k', ec = 'k')
    plt.show()