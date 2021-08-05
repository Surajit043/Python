import random as r
import matplotlib.pyplot as plt

n=1000
t=range (1,n)
h=[ ]
head = 0

for i in t :
    frac = float(head)/i
    if r.random() <= 0.5 :
        head += 1
        frac = float(head)/i
    h.append(frac)

# for ploting
plt.plot(t,h , c = "k" , lw = 2)
plt.xlim(1,n)
plt.ylim(0.4,0.6)
plt.axhline(0.5 ,c ="k")
plt.title ("Fraction of Head" , size = '20')
plt.show()