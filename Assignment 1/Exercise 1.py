import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt


t=np.linspace(0,10*np.pi,10000000)
z=np.sin(t)*np.exp(-t/10)
plt.plot (t,z,color='purple')
#this made each of the data points purple
plt.title("displacement vs time")
#changed the name from cool beans to displacement vs time
plt.xlabel("time")
plt.ylabel("dispalcement")
plt.show()