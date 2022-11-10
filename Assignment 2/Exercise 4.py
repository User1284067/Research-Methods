import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt
import os as os
import re as re

print(os.getcwd())
sunspots_lst= open("sunspots.txt", "r").readlines()


month=[]
sunspots=[]


#intial code before modification
'''
for i in range(len(sunspots_lst)):
    split=re.split(r"\t|\n",sunspots_lst[i],2)
    m,s,*_=split
    month.append(float(m))
    sunspots.append(float(s)) 
'''

    
    
for i in range(1000):
    split=re.split(r"\t|\n",sunspots_lst[i],2)
    m,s,*_=split
    month.append(float(m))
    sunspots.append(float(s)) 
    
    
print(sunspots)
mean_sunspots=[]
for i in range(1000):
    j=0
    y=0
    while j<=i:
        y=0.1*(y+j)
        j=j+1
    mean_sunspots.append(y) #I dont know why this didnt work but oh well


plt.plot(month,sunspots)
plt.plot(month,mean_sunspots)
plt.title("sunspots vs time")
plt.xlabel("time (months)")
plt.ylabel("sunspots")
plt.show()



