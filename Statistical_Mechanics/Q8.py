# There might be some approximation used to make the calculation easy
import numpy as np
import matplotlib.pyplot as plt


def energy():
    T = 300  # We take temp=300K
    k = 1  # to fit within computation range, we have taken Boltzmann Constant=1
    b = 1 / (k * T)
    eps = np.linspace(0, 4, 1000)  # epsilon

    # Avg energy

    E = eps * ((np.exp(-b * eps) + 2 * np.exp(-2 * b * eps)) / (1 + np.exp(-b * eps) + np.exp(-2 * b * eps)))
    plt.xlabel('ε')
    plt.ylabel('Avg. Energy')
    plt.title('plot for the avarage energy as function of particle energy')
    plt.plot(eps, E)
    plt.show()


def spheat():
    T = np.linspace(0.1, 4, 1000)
    k = 1  # to fit within computation range, we have taken Boltzmann Constant=1
    b = 1 / (k * T)
    eps = 2
    Cv = (eps ** 2) * (np.exp(-b * eps) + 4 * np.exp(-2 * b * eps) + np.exp(-3 * b * eps)) / (
                k * T ** 2 * (1 + np.exp(-b * eps) + np.exp(-2 * b * eps)) ** 2)
    plt.xlabel('Temp (K)')
    plt.ylabel('Specific Heat')
    plt.title('plot for the specific heat as a function of temperature')
    plt.plot(T, Cv)
    plt.show()

energy()
spheat()