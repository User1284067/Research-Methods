import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt
import array as ar

g = 9.8 
dt = 0.1 
N = 100
vi = 50.0
xi = 25.0
t = 0
x = 1
v = 0
omega=1
time = [0]
height = [x]
velocity = [v]


for j in range(N):
    t = t + dt
    x = np.sin(-omega * t)
    v = v - omega*x* dt
    time.append(t)
    height.append(x)
    velocity.append(v)
plt.plot(time, height, 'ro')
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
#plt.plot(time, xi + vi*time - 0.5*g*time**2, 'b-')
#plt.plot(time, np.sin(-omega*x*time), 'b-')
plt.show()
