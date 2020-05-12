# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:59:20 2020

@author: 汪嘉川
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
# make array of all susceptible population
population = np. zeros ( (100 , 100) )
# start with one infected person
outbreak = np.random. choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# mapping
plt.figure ( figsize =(6 ,4) , dpi=150) 
plt.imshow( population , cmap='viridis', interpolation='nearest' )
# Define variables
beta = 0.3
gamma = 0.05
# find the infected points
for i in range (0,100):
    infected = np.where(population==1)
# Simulation of spread based on each infection point
    for i in range(len(infected[0])):
        x = infected[0][i]
        y = infected[1][i]
# Process the eight neighbour points
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
# Limit the spread at the picture border
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    infected = np.where(population==1)
# Process recovered points
    for i in range(len(infected[0])):
        x = infected[0][i]
        y = infected[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-gamma,gamma])[0] + 1   
    plt.figure ( figsize =(6 ,4) , dpi=150) 
    plt.imshow( population , cmap='viridis', interpolation='nearest')