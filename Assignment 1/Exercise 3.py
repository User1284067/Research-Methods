import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt

v=4.8
h=1.2
r=2.5
theta=np.linspace(0,90,1000)
def R (theta):
    return v*np.cos(theta)/9.8 * (v*np.sin(theta) + np.sqrt(v**2*np.sin(theta)**2 + 2*9.8*h))


def F(theta):
    return R(theta)-r

plt.plot(theta, F(theta))

plt.show()