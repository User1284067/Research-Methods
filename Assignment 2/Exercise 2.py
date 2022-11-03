import numpy as np
import scipy as sp
import random as rd
import matplotlib.pyplot as plt


a=np.random.rand(10,10).round(2)
print('the 10 by 10 array is ')
print(a)
print('\n')



print('mean is ')
print(np.mean(a).round(2))
print('\n')

print('stdev is ')
print(np.std(a).round(2))
print('\n')

a=np.random.rand(100,100).round(2)
print('the 100 by 100 array is ')
print(a)
print('\n')

print('mean is ')
print(np.mean(a).round(2))
print('\n')

print('stdev is ')
print(np.std(a).round(2))
print('\n')


# for a uniform distrubtion, the is inverse of the square root of 12 multiplied by the difference between the maximum and minimum. 
#Thus for the function np.random.rand give an array of fractional value so the maximum is 1 and the minimum is 0.
#This gives us the standard deviation to be 1/sqrt(12)=0.29



