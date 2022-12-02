import numpy as np
from scipy.optimize import curve_fit
import random as rd
import matplotlib.pyplot as plt
import os as os
import re as re


M=0.02018
R=8.314
T=298.15 
x=np.linspace(0,1000,1000)

y=4*np.pi*(M/2*np.pi*R*T)**(3/2)*np.exp(-M/2*R*T)*x**2

def fit(x,r,t):
    4*np.pi*(M/2*np.pi*r*t)**(3/2)*np.exp(-M/2*r*t)*x**2


plt.plot(curve_fit(fit,x,y))
plt.show()










"""
HW:
    1. Use polyfit with 5th order approximation to fit f(x)=Asin(x)+Bcos(x)
    2. Use curve fit to fit the scalar maxwell botlzmann distribution: 
        f(x)=4pi(M/2piRT)^3/2 exp(-M/2RT)x^2, M=14, R=8.314,T=298.15    
    """


