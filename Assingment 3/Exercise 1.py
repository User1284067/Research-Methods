import numpy as np
import scipy as sp
from scipy import optimize
import random as rd
import matplotlib.pyplot as plt
import os as os
import re as re

A=2
B=3
x=np.linspace(0,1000,1000)

a,b,c,d,e,f=np.polyfit(x,A*np.sin(x)+B*np.cos(x),5)

plt.plot(x,A*np.sin(x)+B*np.cos(x))
plt.plot(x,a*x**5+b*x**4+c*x**3+d*x**2+e*x+f)
plt.show()




"""
HW:
    1. Use polyfit with 5th order approximation to fit f(x)=Asin(x)+Bcos(x)
    2. Use curve fit to fit the scalar maxwell botlzmann distribution: 
        f(x)=4pi(M/2piRT)^3/2 exp(-M/2RT)x^2, M=14, R=8.314,T=298.15    
    """

