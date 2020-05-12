# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:04:57 2020

@author: 汪嘉川
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
# define basic variables
N = 10000 # the total number of people in the population
beta = 0.3 # infection probability
gamma = 0.05 # recovery probability
t = 1000 # time points
S = [9999]
I = [1]
R = [0]
p=[0]
result_1 = []
result_2 = []
# simulation
for i in range(0,t):
    result_1 = np.random.choice(range(2),S[i],p=[1-beta*(I[i]/N),beta*(I[i]/N)])
    n1 = np.sum(result_1 == 1)
    result_2 = np.random.choice(range(2),I[i],p=[1-gamma,gamma])
    n2 = np.sum(result_2 == 1)
    S.append(S[i]-n1)
    I.append(I[i]+n1-n2)
    R.append(R[i]+n2)
    p.append(i)
# mapping
y1=S
y2=I
y3=R
plt.plot(p, y1, label='susceptible')
plt.plot(p, y2, label='infected')
plt.plot(p, y3, label='recovered')
plt.xlabel('Time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend(loc = 'upper right')
plt.show