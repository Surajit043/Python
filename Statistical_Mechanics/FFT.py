import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Number of sample points
n=500
# Sample Spacing
t = 1.0/400.0
x=np.linspace(0.0,n*t,n)
# The function
y = 2*np.sin(2.0*np.pi*x)+5*np.sin(5.0*np.pi*x)
# FFT
yf = fft(y)
freq = np.linspace(0.0,1.0/(2*t), n//2)
# for ploting
plt.plot(freq , 2.0/n*np.abs(yf[:n//2]), color = 'black')
plt.title('FFT', size='20')
plt.grid()
plt.show()