# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:04:57 2020

@author: 汪嘉川
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
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
r = [0,10,20,30,40,50,60,70,80,90,100] # different vaccination rates
# Simulation
for v in range(0,11):
    p = [0]
    I = [1]
    S = [9999-r[v]*100]
    if S[0] < 0:
        S = [0]
        I = [0]
    s = str(r[v])+'%'
    for i in range(0,t):
        result_1 = np.random.choice(range(2),S[i],p=[1-beta*(I[i]/N),beta*(I[i]/N)])
        n1 = np.sum(result_1 == 1)
        result_2 = np.random.choice(range(2),I[i],p=[1-gamma,gamma])
        n2 = np.sum(result_2 == 1)
        S.append(S[i]-n1)
        I.append(I[i]+n1-n2)
        R.append(R[i]+n2)
        p.append(i)
#mapping
    plt.plot(p, I, label=s,color=cm.viridis(100))
plt.legend(loc = 'upper right')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.show()