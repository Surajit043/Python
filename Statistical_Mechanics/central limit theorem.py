import numpy as np
import matplotlib.pyplot as plt

x = lambda n: np.mean(np.random.randint(1,7, size = n))
xx = [x(n) for i in range (10000)]
plt.hist(xx)
plt.show()