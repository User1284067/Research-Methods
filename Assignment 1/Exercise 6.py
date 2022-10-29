import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt


turns=[0,1,2,3,4,5,6,7,8,9,10]
position=[0,-2,-11,-15,-24,-32,-40,-50,-52,-62,-65]
fit=[]
for i in turns:
    fit.append(-7*i+3)

plt.plot (turns,position)
plt.plot(turns,fit)

plt.title("position vs turns")

plt.xlabel("turns")
plt.ylabel("position")
plt.show()