import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt

def grav_drop(tinitial,tfinal):
    t=np.linspace(tinitial,tfinal,10000000)
    x=-4.9*t**2
    v=-9.8*t
    plt.plot (t,x,color='purple')
    plt.plot(t,v,color='green')
    
    plt.title("position and velocity vs time")
    
    plt.xlabel("time")
    plt.ylabel("position")
    plt.show()
    return print('position='+str(x)+'and velocity='+str(v))


grav_drop(0,5)
