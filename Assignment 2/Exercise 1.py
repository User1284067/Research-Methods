import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt


a=np.random.rand(4,4).round(2)
print("the array is ")
print(a)


print('every element of the second row is ')
for i in range(len(a)):
    print(a[1,i])


print('every element of the third column is ')
for i in range(a.size):
    print(a[i,2])
    
    
for i in range(2):
    for j in range(2):
        a[i,j]=0.21
print(a)
