import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt


a=np.random.rand(rd.randint(1,4),rd.randint(1,4)).round(2)
b=np.random.rand(4,4).round(2)

def diagonal_check(array):
    a=1
    if len(array)==array[0].size:
        for i in range(len(array)):
            a=a*array[i,i]
        return print("the array is:\n" +str(array)+ "\n and the trace is: "+str(a.round(2)))
    else:
        return print("invalid dimensions")
    
diagonal_check(a)
diagonal_check(b)